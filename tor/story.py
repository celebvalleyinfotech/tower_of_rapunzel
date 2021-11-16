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

from balladeer import Settings
from balladeer import Story

from turberfield.dialogue.model import Model

import tor.rules
from tor.types import version


class Rapunzel(Story):

    def __init__(self, cfg=None, **kwargs):
        super().__init__(**kwargs)

        self.definitions = {
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
