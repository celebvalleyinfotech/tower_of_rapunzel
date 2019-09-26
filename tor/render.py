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

import functools


def element_as_list_item(element):
    if hasattr(element.dialogue, "persona"):
        return f"""
<li style="animation-duration: {element.duration}s; animation-delay: {element.offset}s">
<blockquote class="line">
<header class="{'persona' if hasattr(element.dialogue.persona, '_name') else ''}">
{ element.dialogue.persona._name if hasattr(element.dialogue.persona, '_name') else ''}
</header>
<p class="speech">{ element.dialogue.text }</p>
</blockquote>
</li>
        """
    elif hasattr(element.dialogue, "loop"):
        return """
<li>
<audio
    src="/audio/{0.dialogue.resource}"
    autoplay="autoplay" preload="auto"
>
</audio>
</li>""".format(element)
    else:
        return ""


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


def body_to_html(state, frame=[], options=[]):
    labels = {
        "balcony": "On the Balcony",
        "broomer": "At the Broom shop",
        "butcher": "In the Butcher's",
        "chamber": "The Chamber",
        "chemist": "The Chemist",
        "inbound": "Foot of the Tower",
        "outward": "Foot of the Tower",
        "stylist": "At the Stylist",
    }
    return f"""
<main class="grid-front">
<h1>{labels[state.area]}</h1>
<ul class="mod-dialogue">
{{0}}
</ul>
</main>
<nav class="grid-steer">
{{1}}
{{2}}
{{3}}
</nav>
<section class="grid-dash">
<dl class="mod-stats">
<dt>Health</dt>
<dd>{int(state.health_n)}</dd>
<dt>Coins</dt>
<dd>{state.coins_n}</dd>
</dl>
</section>"""


@functools.lru_cache()
def base_to_html(refresh=None):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
{'<meta http-equiv="refresh" content="{0}">'.format(refresh) if refresh is not None else ''}
<meta http-equiv="X-UA-Compatible" content="ie=edge">
<link rel="stylesheet" href="/css/blmst.css" />
</head>
<body>
{{0}}
</body>
</html>"""
