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
import tor.rules
import tor.story
from tor.story import At
from tor.story import Character
from tor.story import Narrator
from tor.story import Rapunzel
import tor.render


class Presentation:

    Element = namedtuple(
        "Element",
        ["source", "dialogue", "shot", "offset", "duration"]
    )

    @staticmethod
    def build_frames(source, seq, dwell, pause):
        """Generate a new Frame on each Shot and FX item"""
        shot = None
        frame = []
        offset = 0
        for item in seq:
            if isinstance(item, (Model.Audio, Model.Shot)):
                if frame and shot and shot != item:
                    yield frame
                    frame = []
                    offset = 0

                if isinstance(item, Model.Shot):
                    shot = item
                else:
                    frame.append(Presentation.Element(
                        source, item, shot,
                        item.offset / 1000,
                        item.duration / 1000
                    ))

            elif isinstance(item, Model.Line):
                durn = pause + dwell * item.text.count(" ")
                frame.append(Presentation.Element(
                    source, item, shot, offset, durn
                ))
                offset += durn
            elif not isinstance(item, Model.Condition):
                frame.append(Presentation.Element(
                    source, item, shot, offset, 0
                ))
        else:
            if any(
                isinstance(
                    i.dialogue, (Model.Audio, Model.Line)
                )
                for i in frame
            ):
                yield frame

    @staticmethod
    def next_frame(game, entities, dwell=0.3, pause=1):
        while not game["frames"]:
            location = game["state"].area
            matcher = Matcher(tor.story.episodes)
            folders = list(matcher.options(game["metadata"]))
            performer = Performer(folders, entities)
            folder, index, script, selection, interlude = performer.next(
                folders, entities
            )
            scene = performer.run(react=False)
            frames = list(Presentation.build_frames(
                folder.paths[index], scene,
                dwell=dwell, pause=pause
            ))
            game["frames"].extend(frames)

        return game["frames"].popleft()

    @staticmethod
    def react(game, frame):
        for element in frame:
            event = element.dialogue
            if (
                isinstance(event, Model.Property) and
                event.object is not None
            ):
                setattr(event.object, event.attr, event.val)

            yield element

    @staticmethod
    def refresh(frame, min_val=8):
        try:
            return max(
                [min_val] +
                [i.offset + i.duration for i in frame if i.duration]
            )
        except ValueError:
            return None


async def get_frame(request):
    game = request.app.game
    location = game["state"].area
    entities = [
        i for i in tor.story.ensemble
        if getattr(i, "area", location) == location
    ]
    narrator = next(i for i in entities if isinstance(i, Narrator))
    narrator.state = game["state"]
    for character in (i for i in entities if isinstance(i, Character)):
        character.set_state(random.randrange(10))

    frame = Presentation.next_frame(game, entities)
    buys = ["Spend 1c", "Spend 2c", "Spend 3c"] if location == "butcher" else []
    cuts = ["Cut less", "Cut same", "Cut more"] if location == "chamber" else []
    hops = tor.rules.topology[location]
    elements = list(Presentation.react(game, frame))
    return web.Response(
        text = tor.render.base_to_html(
            #refresh=math.ceil(Presentation.refresh(frame))
            refresh=None
        ).format(
            tor.render.body_to_html(game["state"], frame=frame).format(
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
        game = request.app.game
        game["frames"].clear()
        rv = tor.rules.apply_rules(
            None, None, None, tor.rules.Settings, game["state"], buy=int(buy)
        )
        game["state"] = tor.rules.State(**rv)
        raise web.HTTPFound("/")


async def post_cut(request):
    cut = request.match_info["cut"]
    if not tor.rules.choice_validator.match(cut):
        raise web.HTTPUnauthorized(reason="User sent invalid cut code.")
    else:
        game = request.app.game
        game["frames"].clear()
        cut_d = {
            0: -tor.rules.Settings.CUT_D,
            1: 0,
            2: tor.rules.Settings.CUT_D,
        }.get(int(cut), tor.rules.Settings.CUT_D)

        rv = tor.rules.apply_rules(
            None, None, None, tor.rules.Settings, game["state"], cut=cut_d
        )
        game["state"] = tor.rules.State(**rv)
        raise web.HTTPFound("/")


async def post_hop(request):
    hop = request.match_info["hop"]
    if not tor.rules.choice_validator.match(hop):
        raise web.HTTPUnauthorized(reason="User sent invalid hop.")
    else:
        index = int(hop)
        game = request.app.game
        location = game["state"].area
        destination = tor.rules.topology[location][index]
        game["metadata"]["area"] = destination
        game["state"] = game["state"]._replace(area=destination)
        game["frames"].clear()
        if destination not in ("butcher", "chamber"):
            rv = tor.rules.apply_rules(
                None, None, None, tor.rules.Settings, game["state"]
            )
            if not rv:
                print("Game Over", file=sys.stderr)
                rapunzel = next(
                    i for i in tor.story.ensemble
                    if isinstance(i, Rapunzel)
                )
                rapunzel.set_state(At.club)
            else:
                game["state"] = tor.rules.State(**rv)
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
    app.game = {
        "metadata": {"area": "balcony"},
        "state": tor.rules.State(
            "balcony",
            tor.rules.Settings.HAIR_M,
            tor.rules.Settings.HAIR_D,
            tor.rules.Settings.CUT_M,
            tor.rules.Settings.COINS_N,
            tor.rules.Settings.HEALTH_MAX
        ),
        "frames": deque([])
    }
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
