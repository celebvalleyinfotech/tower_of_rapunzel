#!/usr/bin/env python3
# encoding: UTF-8

# This file is part of Addison Arches.
#
# Addison Arches is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Addison Arches is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Addison Arches.  If not, see <http://www.gnu.org/licenses/>.

import datetime
import functools
from turberfield.dialogue.model import Model

from tor.presentor import Presenter


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


def animated_still_to_html(anim):
    return f"""
<div style="animation-duration: {anim.duration}s; animation-delay: {anim.delay}s">
<img src="/img/{anim.element.resource}" alt="{anim.element.package} {anim.element.resource}" />
</div>"""


def audio_to_html(elem):
    return f"""<div>
<audio src="/audio/{elem.resource}" autoplay="autoplay" preload="auto" >
</audio>
</div>"""


def location_to_html(locn, path="/"):
    return f"""
<form role="form" action="{path}hop" method="post" name="{locn.id.hex}" >
    <input id="hop-{locn.id.hex}" name="location_id" type="hidden" value="{locn.id.hex}" />
    <button type="submit">{locn.label}</button>
</form>"""

def option_as_list_item(n, option, path="/"):
    labels = {
        "balcony": "Onto the Balcony",
        "broomer": "Broom shop",
        "butcher": "Go round the Butcher's",
        "chamber": "Into the Chamber",
        "chemist": "Pop to the Chemist",
        "inbound": "Foot of the Tower",
        "outward": "Climb down",
        "stylist": "Visit the Stylist",
    }
    return f"""
<form role="form" action="{path}{n}" method="post" name="choice" >
    <button type="submit">{labels.get(option, option)}</button>
</form>"""


def frame_to_html(state, frame, final=False):
    narrator = None
    ts = datetime.datetime.now()
    #spot = narrator.get_state(Spot) if narrator else None
    spot = None
    dialogue = "\n".join(animated_line_to_html(i) for i in frame[Model.Line])
    stills = "\n".join(animated_still_to_html(i) for i in frame[Model.Still])
    audio = "\n".join(audio_to_html(i) for i in frame[Model.Audio])
    return f"""
{audio}
<section class="fit-banner">
<h1><span>Blue</span><span>Monday</span><span>78</span></h1>
<h2>{ts.strftime("%H:%M:%S %p") if ts else ""}</h2>
<h2>{ts.strftime("%a %d %b") if ts else ""}</h2>
</section>
<aside class="fit-photos">
{stills}
</aside>
<div class="fit-speech">
<main>
{'<h1>{0}</h1>'.format(spot.value[-1].capitalize().replace("_", " ")) if spot is not None else ''}
<ul class="obj-dialogue">
{dialogue}
</ul>
</main>
<nav>
<ul>
{{0}}
</ul>
</nav>
</div>"""


def titles_to_html(config=None, url_pattern=Presenter.validation["url"].pattern):
    assembly_widget = f"""
    <label for="input-assembly-url" id="tip-assembly-url">Assembly URL</label>
    <input
    name="assembly_url"
    type="url"
    id="input-assembly-url"
    aria-describedby="tip-assembly-url"
    placeholder="http://"
    pattern="{ url_pattern }"
    title="This server can import JSON data from a URL endpoint. If correctly formatted, that data will be used to initialise your story."
    >""" if config and config.getboolean("assembly", "enable_user", fallback=False) else ""

    return f"""
<section class="fit-banner">
<h1><span>Blue</span><span>Monday</span><span>78</span></h1>
<h2>An Addison Arches episode</h2>
</section>
<div class="fit-speech">
<main>
<h1>Start a new story.</h1>
<p class="obj-speech">You can get the code for this story from
<a href="https://github.com/tundish/blue_monday_78">GitHub</a>.</p>
</main>
<nav>
<ul>
<li><form role="form" action="/" method="POST" name="titles" class="grid-flash mod-titles">
    <fieldset>
    { assembly_widget }
    <button type="submit">Go</button>
    </fieldset>
</form></li>
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
<title>Blue Monday 78: Pilot episode</title>
<link rel="stylesheet" href="/css/bfost.css" />
</head>
<body>
<style type="text/css">
{{0}}
</style>
{{1}}
</body>
</html>"""
