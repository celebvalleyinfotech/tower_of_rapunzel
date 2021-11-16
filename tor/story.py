#!/usr/bin/env python3
# encoding: UTF-8

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

from collections import defaultdict
from collections import deque
from collections import namedtuple
import copy
from datetime import datetime
import itertools
import functools
import logging
import math
import re
import sys

from balladeer import DataObject
from balladeer import Renderer
from balladeer import Settings
from balladeer import Story

from turberfield.dialogue.model import Model
from turberfield.dialogue.model import SceneScript
from turberfield.dialogue.performer import Performer
import turberfield.utils

import tor
from tor.types import Narrator
from tor.types import version


class Rapunzel(Story):

    def __init__(self, cfg=None, **kwargs):
        super().__init__(**kwargs)

        definitions = {
            "creamy": "hsl(50, 0%, 100%, 1.0)",
            "pebble": "hsl(13, 0%, 30%, 1.0)",
            "claret": "hsl(13, 80%, 55%, 1.0)",
            "blonde": "hsl(50, 80%, 35%, 1.0)",
            "bubble": "hsl(320, 100%, 50%, 1.0)",
            "forest": "hsl(76, 80%, 35%, 1.0)",
            "rafter": "hsl(36, 20%, 18%, 1.0)",
            "titles": '"AA Paro", sans-serif',
            "mono": ", ".join([
                "SFMono-Regular", "Menlo", "Monaco",
                "Consolas", '"Liberation Mono"',
                '"Courier New"', "monospace"
            ]),
            "system": ", ".join([
                "BlinkMacSystemFont", '"Segoe UI"', '"Helvetica Neue"',
                '"Apple Color Emoji"', '"Segoe UI Emoji"', '"Segoe UI Symbol"',
                "Arial", "sans-serif"
            ]),
        }
        self.settings = Settings(**self.definitions)
        self.context = kwargs.get("context", None)

    @staticmethod
    def animated_line_to_html(anim):
        return f"""
    <li style="animation-delay: {anim.delay:.2f}s; animation-duration: {anim.duration:.2f}s">
    <blockquote class="obj-line">
    <header class="{'obj-persona' if hasattr(anim.element.persona, '_name') else 'obj-entity'}">
    { '{0.firstname} {0.surname}'.format(anim.element.persona.name) if hasattr(anim.element.persona, 'name') else ''}
    </header>
    <p class="obj-speech">{ anim.element.text }</p>
    </blockquote>
    </li>"""


    @staticmethod
    def animated_still_to_html(anim):
        return f"""
    <div style="animation-duration: {anim.duration}s; animation-delay: {anim.delay}s">
    <img src="/img/{anim.element.resource}" alt="{anim.element.package} {anim.element.resource}" />
    </div>"""


    @staticmethod
    def animated_audio_to_html(anim):
        return f"""<div>
    <audio src="/audio/{anim.element.resource}" autoplay="autoplay"
    preload="auto" {'loop="loop"' if anim.element.loop and int(anim.element.loop) > 1 else ""}>
    </audio>
    </div>"""


    @staticmethod
    def location_to_html(locn, path="/"):
        return f"""
    <form role="form" action="{path}hop" method="post" name="{locn.id.hex}" >
        <input id="hop-{locn.id.hex}" name="location_id" type="hidden" value="{locn.id.hex}" />
        <button type="submit">{locn.label}</button>
    </form>"""


    @staticmethod
    def option_as_list_item(n, option, path="/"):
        labels = tor.rules.motion
        return f"""
    <li><form role="form" action="{path}{n}" method="post" name="choice" >
        <button type="submit">{labels.get(option, option)}</button>
    </form></li>"""

    def render_animated_frame_to_html(self, state, frame, final=False):
        labels = tor.rules.labels
        location = state.area
        dialogue = "\n".join(self.animated_line_to_html(i) for i in frame[Model.Line])
        stills = "\n".join(self.animated_still_to_html(i) for i in frame[Model.Still])
        audio = "\n".join(self.animated_audio_to_html(i) for i in frame[Model.Audio])
        hops = "\n".join(
            self.option_as_list_item(n, option, path="/hop/")
            for n, option in enumerate(tor.rules.topology[location])
        )
        buys = "\n".join(
            self.option_as_list_item(n + 1, option, path="/buy/")
            for n, option in enumerate(tor.rules.offers.get(location, []))
        )
        cuts = "\n".join(
            self.option_as_list_item(n, option, path="/cut/")
            for n, option in enumerate(tor.rules.actions.get(location, []))
        )
        return f"""
    {audio}
    <section class="fit-vista">
    <h1>Tower of Rapunzel</h1>
    <h2>{version}</h2>
    {stills}
    </section>
    <div class="fit-speech">
    <main>
    <h1>{labels[state.area]}</h1>
    <ul class="obj-dialogue">
    {dialogue}
    </ul>
    </main>
    </div>
    <div class="fit-control">
    <nav>
    <ul>
    {hops}
    {buys}
    {cuts}
    </ul>
    </nav>
    </div>"""


def dict_to_css(mapping=None, tag=":root"):
    mapping = mapping or {}
    entries = "\n".join("--{0}: {1};".format(k, v) for k, v in mapping.items())
    return f"""{tag} {{
{entries}
}}"""


@functools.lru_cache()
def body_html(refresh=None):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
{'<meta http-equiv="refresh" content="{0}">'.format(refresh) if refresh is not None else ''}
<meta http-equiv="X-UA-Compatible" content="ie=edge">
<title>Tower of Rapunzel</title>
<link rel="stylesheet" href="/css/bfost.css" />
</head>
<body>
<style type="text/css">
{{0}}
</style>
{{1}}
</body>
</html>"""

class Presenter:

    Animation = namedtuple("Animation", ["delay", "duration", "element"])

    @staticmethod
    def animate_audio(seq):
        """ Generate animations for audio effects."""
        yield from (
            Presenter.Animation(asset.offset, asset.duration, asset)
            for asset in seq
        )

    @staticmethod
    def animate_lines(seq, dwell, pause):
        """ Generate animations for lines of dialogue."""
        offset = 0
        for line in seq:
            duration = pause + dwell * line.text.count(" ")
            yield Presenter.Animation(offset, duration, line)
            offset += duration

    @staticmethod
    def animate_stills(seq):
        """ Generate animations for still images."""
        yield from (
            Presenter.Animation(still.offset / 1000, still.duration / 1000, still)
            for still in seq
        )

    @staticmethod
    def refresh_animations(frame, min_val=8):
        rv = min_val
        for typ in (Model.Line, Model.Still, Model.Audio):
            try:
                last_anim = frame[typ][-1]
                rv = max(rv, math.ceil(last_anim.delay + last_anim.duration))
            except IndexError:
                continue
        return rv

    def __init__(self, dialogue, ensemble=None):
        self.frames = [
            defaultdict(list, dict(
                {k: list(v) for k, v in itertools.groupby(i.items, key=type)},
                name=i.name, scene=i.scene
            ))
            for i in getattr(dialogue, "shots", [])
        ]
        self.ensemble = ensemble
        self.log = logging.getLogger(str(getattr(ensemble[0], "id", "")) if ensemble else "")
        self.ts = datetime.utcnow()

    @property
    def pending(self) -> int:
        return len([
            frame for frame in self.frames
            if all([Performer.allows(i) for i in frame[Model.Condition]])
        ])

    @property
    def narrator(self):
        return next((i for i in self.ensemble if isinstance(i, Narrator)), None)

    def dialogue(self, folders, ensemble, strict=True, roles=2):
        """ Return the next selected scene script as compiled dialogue."""
        for folder in folders:
            for script in SceneScript.scripts(**folder._asdict()):
                with script as dialogue:
                    try:
                        selection = dialogue.select(ensemble, roles=roles)
                    except Exception as e:
                        self.log.error("Unable to process {0.fP}".format(script))
                        self.log.exception(e)
                        continue

                    if selection and all(selection.values()):
                        self.log.debug("Selection made strictly")
                    elif not strict and any(selection.values()):
                        self.log.debug("Selection made")
                    else:
                        continue

                    try:
                        return dialogue.cast(selection).run()
                    except Exception as e:
                        self.log.error("Unable to run {0.fP}".format(script))
                        self.log.exception(e)
                        continue

    def frame(self, dwell=0.3, pause=1, react=True):
        """ Return the next shot of dialogue as an animated frame."""
        while True:
            try:
                frame = self.frames.pop(0)
            except IndexError:
                self.log.debug("No more frames.")
                raise

            if all([Performer.allows(i) for i in frame[Model.Condition]]):
                frame[Model.Line] = list(
                    self.animate_lines(frame[Model.Line], dwell, pause)
                )
                frame[Model.Audio] = list(self.animate_audio(frame[Model.Audio]))
                frame[Model.Still] = list(self.animate_stills(frame[Model.Still]))
                for p in frame[Model.Property]:
                    if react and p.object is not None:
                        setattr(p.object, p.attr, p.val)
                for m in frame[Model.Memory]:
                    if react and m.object is None:
                        m.subject.set_state(m.state)
                    try:
                        if m.subject.memories[-1].state != m.state:
                            m.subject.memories.append(m)
                    except AttributeError:
                        m.subject.memories = deque([m], maxlen=6)
                    except IndexError:
                        m.subject.memories.append(m)
                return frame
