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
A web-native single-puzzle text adventure for PyWeek 28 and NarraScope 2020.

"""
import argparse
from collections import deque
import random
import sys

from aiohttp import web
import pkg_resources

import tor
from tor.drama import Tower
from tor.story import Rapunzel
import tor.rules
from tor.types import Character
from tor.types import Hanging
from tor.types import Occupation


async def get_frame(request):
    story = request.app["story"][0]

    animation = None
    while not animation:
        try:
            frame = story.presenter.frames.pop(0)
            animation = story.presenter.animate(
                frame, dwell=story.presenter.dwell, pause=story.presenter.pause
            )
        except IndexError:
            story.presenter = story.represent("")
    else:
        story.animation = animation

    refresh = story.presenter.pending and story.presenter.refresh_animations(story.animation, min_val=2)

    title = story.presenter.metadata.get("project", ["Tower of Rapunzel"])[0]
    rv = story.render_body_html(title=title, next_="/", refresh=refresh).format(
        '<link rel="stylesheet" href="/css/bfost.css" />',
        story.render_dict_to_css(vars(story.settings)),
        story.render_animated_frame_to_html(
            story.context.narrator.state, story.animation, final=not story.presenter.pending
        )
    )

    return web.Response(text=rv, content_type="text/html")


async def post_buy(request):
    buy = request.match_info["buy"]
    if not tor.rules.choice_validator.match(buy):
        raise web.HTTPUnauthorized(reason="User sent invalid buy code.")

    story = request.app["story"][0]
    narrator = story.context.narrator

    prize = int(buy) * 10
    if narrator.state.area == "broomer" and narrator.state.coins_n >= prize:
        # Detect win condition
        broomer = next(
            i for i in story.context.ensemble
            if isinstance(i, Character) and i.get_state(Occupation) == Occupation.broomer
        )
        broomer.set_state(prize)
        narrator.state = narrator.state._replace(coins_n=narrator.state.coins_n - prize)
        print("Win achieved.", file=sys.stderr)
    else:
        rv = tor.rules.apply_rules(
            None, None, None, tor.rules.Settings, story.context.narrator.state, buy=int(buy)
        )
        story.context.narrator.state = tor.rules.State(**rv)

    story.presenter = story.represent("")
    raise web.HTTPFound("/")


async def post_cut(request):
    cut = request.match_info["cut"]
    if not tor.rules.choice_validator.match(cut):
        raise web.HTTPUnauthorized(reason="User sent invalid cut code.")
    else:
        story = request.app["story"][0]
        cut_d = {
            0: -tor.rules.Settings.CUT_D,
            1: 0,
            2: tor.rules.Settings.CUT_D,
        }.get(int(cut), tor.rules.Settings.CUT_D)

        rv = tor.rules.apply_rules(
            None, None, None, tor.rules.Settings, story.context.narrator.state, cut=cut_d
        )
        story.context.narrator.state = tor.rules.State(**rv)
        story.presenter = story.represent("")
        raise web.HTTPFound("/")


async def post_hop(request):
    hop = request.match_info["hop"]
    if not tor.rules.choice_validator.match(hop):
        raise web.HTTPUnauthorized(reason="User sent invalid hop.")
    else:
        index = int(hop)
        story = request.app["story"][0]
        location = story.context.narrator.state.area
        destination = tor.rules.topology[location][index]
        story.context.narrator.state = story.context.narrator.state._replace(area=destination)

        entities = [
            i for i in story.context.ensemble
            if getattr(i, "area", destination) == destination
        ]
        for character in (i for i in entities if isinstance(i, Character)):
            character.set_state(random.randrange(10))

        if destination not in ("butcher", "chamber"):
            rv = tor.rules.apply_rules(
                None, None, None, tor.rules.Settings, story.context.narrator.state
            )
            if rv:
                story.context.narrator.state = tor.rules.State(**rv)
            else:
                print("Game Over", file=sys.stderr)
                rapunzel = next(
                    i for i in story.context.ensemble
                    if isinstance(i, Character) and i.get_state(Occupation) == Occupation.teenager
                )
                rapunzel.set_state(Hanging.club)

        story.presenter = story.represent("")
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
    app.router.add_static(
        "/img/",
        pkg_resources.resource_filename("tor", "static/img")
    )
    app.router.add_static(
        "/audio/",
        pkg_resources.resource_filename("tor", "static/audio")
    )
    app.router.add_static(
        "/fonts/",
        pkg_resources.resource_filename("tor", "static/fonts")
    )
    story = Rapunzel(context=Tower())
    story.presenter = story.represent("")
    app["story"] = deque([story], maxlen=1)
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
