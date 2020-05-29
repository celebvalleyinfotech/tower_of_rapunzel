#!/usr/bin/env python3
# encoding: utf-8

# This file is part of Tower of Rapunzel.
#
# Tower of Rapunzel is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Tower of Rapunzel is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Tower of Rapunzel.  If not, see <http://www.gnu.org/licenses/>.

"""
A text-based web game for PyWeek 28.

"""
import argparse
import asyncio
from collections import deque
from collections import namedtuple
import functools
import math
import random
import sys

from aiohttp import web
import pkg_resources

from turberfield.dialogue.matcher import Matcher
from turberfield.dialogue.model import Model
from turberfield.dialogue.performer import Performer

import tor
from tor.presenter import Presenter
import tor.render
import tor.rules
import tor.story
from tor.story import Character
from tor.story import Hanging
from tor.story import Narrator
from tor.story import Occupation


async def get_frame(request):
    presenter = request.app["presenter"]
    location = presenter.narrator.state.area
    entities = [
        i for i in presenter.ensemble
        if getattr(i, "area", location) == location
    ]
    #narrator = next(i for i in entities if isinstance(i, Narrator))
    #narrator.state = presenter.game["state"]
    for character in (i for i in entities if isinstance(i, Character)):
        character.set_state(random.randrange(10))

    frame = presenter.next_frame(entities)
    buys = ["Spend 1c", "Spend 2c", "Spend 3c"] if location == "butcher" else []
    cuts = ["Cut less", "Cut same", "Cut more"] if location == "chamber" else []
    hops = tor.rules.topology[location]
    elements = list(Presenter.react(frame))
    return web.Response(
        text = tor.render.base_to_html(
            #refresh=math.ceil(Presenter.refresh(frame))
            refresh=None
        ).format(
            tor.render.body_to_html(presenter.narrator.state, frame=frame).format(
                "\n".join(
                    tor.render.element_as_list_item(element)
                    for element in frame
                ),
                "\n".join(
                    tor.render.option_as_list_item(n, option, path="/hop/")
                    for n, option in enumerate(hops)
                ),
                "\n".join(
                    tor.render.option_as_list_item(n + 1, option, path="/buy/")
                    for n, option in enumerate(buys)
                ),
                "\n".join(
                    tor.render.option_as_list_item(n, option, path="/cut/")
                    for n, option in enumerate(cuts)
                ),
            )
        ),
        content_type="text/html"
    )


async def post_buy(request):
    buy = request.match_info["buy"]
    if not tor.rules.choice_validator.match(buy):
        raise web.HTTPUnauthorized(reason="User sent invalid buy code.")
    else:
        presenter = request.app["presenter"]
        presenter.frames.clear()
        rv = tor.rules.apply_rules(
            None, None, None, tor.rules.Settings, presenter.narrator.state, buy=int(buy)
        )
        presenter.narrator.state = tor.rules.State(**rv)
        raise web.HTTPFound("/")


async def post_cut(request):
    cut = request.match_info["cut"]
    if not tor.rules.choice_validator.match(cut):
        raise web.HTTPUnauthorized(reason="User sent invalid cut code.")
    else:
        presenter = request.app["presenter"]
        presenter.frames.clear()
        cut_d = {
            0: -tor.rules.Settings.CUT_D,
            1: 0,
            2: tor.rules.Settings.CUT_D,
        }.get(int(cut), tor.rules.Settings.CUT_D)

        rv = tor.rules.apply_rules(
            None, None, None, tor.rules.Settings, presenter.narrator.state, cut=cut_d
        )
        presenter.narrator.state = tor.rules.State(**rv)
        raise web.HTTPFound("/")


async def post_hop(request):
    hop = request.match_info["hop"]
    if not tor.rules.choice_validator.match(hop):
        raise web.HTTPUnauthorized(reason="User sent invalid hop.")
    else:
        index = int(hop)
        presenter = request.app["presenter"]
        location = presenter.narrator.state.area
        destination = tor.rules.topology[location][index]
        #presenter.game["metadata"]["area"] = destination
        presenter.narrator.state = presenter.narrator.state._replace(area=destination)
        presenter.frames.clear()
        if destination not in ("butcher", "chamber"):
            rv = tor.rules.apply_rules(
                None, None, None, tor.rules.Settings, presenter.narrator.state
            )
            if not rv:
                print("Game Over", file=sys.stderr)
                rapunzel = next(
                    i for i in presenter.ensemble
                    if isinstance(i, Character) and i.get_state(Occupation) == Occupation.teenager
                )
                rapunzel.set_state(Hanging.club)
            else:
                presenter.narrator.state = tor.rules.State(**rv)
        raise web.HTTPFound("/")


def build_app(args):
    app = web.Application()
    app.add_routes([
        web.get("/", get_frame),
        web.post("/buy/{{buy:{0}}}".format(tor.rules.choice_validator.pattern), post_buy),
        web.post("/cut/{{cut:{0}}}".format(tor.rules.choice_validator.pattern), post_cut),
        web.post("/hop/{{hop:{0}}}".format(tor.rules.choice_validator.pattern), post_hop),
    ])
    app.router.add_static(
        "/css/",
        pkg_resources.resource_filename("tor", "static/css")
    )
    game = {
        "metadata": {"area": "balcony"},
        "state": tor.rules.State(
            "balcony",
            tor.rules.Settings.HAIR_M,
            tor.rules.Settings.HAIR_D,
            tor.rules.Settings.CUT_M,
            tor.rules.Settings.COINS_N,
            tor.rules.Settings.HEALTH_MAX
        ),
    }
    app["presenter"] = Presenter(tor.story.ensemble)
    return app


def main(args):
    app = build_app(args)
    return web.run_app(app, host=args.host, port=args.port)

def parser(description=__doc__):
    rv = argparse.ArgumentParser(description)
    rv.add_argument(
        "--version", action="store_true", default=False,
        help="Print the current version number.")
    rv.add_argument(
        "--host", default="127.0.0.1",
        help="Set an interface on which to serve."
    )
    rv.add_argument(
        "--port", default=8080, type=int,
        help="Set a port on which to serve."
    )
    return rv


def run():
    p = parser()
    args = p.parse_args()

    rv = 0
    if args.version:
        sys.stdout.write(tor.__version__)
        sys.stdout.write("\n")
    else:
        rv = main(args)

    if rv == 2:
        sys.stderr.write("\n Missing command.\n\n")
        p.print_help()

    sys.exit(rv)


if __name__ == "__main__":
    run()
