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


import itertools

from turberfield.dialogue.model import SceneScript
from turberfield.dialogue.types import Persona
from turberfield.dialogue.types import Stateful

import tor
import tor.rules

version = tor.__version__


class Narrator(Stateful): pass
class Character(Stateful, Persona): pass
class Butcher(Character): pass

ensemble = [
    Narrator(),
    Butcher(name="Mr Ricky Butcher"),
]

episodes = [

    SceneScript.Folder(
        pkg="tor",
        description="Dialogue on the balcony.",
        metadata={
            "area": "balcony",
        },
        paths=[
            "dialogue/balcony/brooms.rst",
            "dialogue/balcony/rapunzel.rst",
            "dialogue/balcony/money.rst",
            "dialogue/balcony/witches.rst",
            "dialogue/balcony/comedy.rst",
            "dialogue/balcony/progress.rst",
            "dialogue/balcony/injuries.rst"
        ],
        interludes=itertools.repeat(tor.rules.apply_rules)
    ),

    SceneScript.Folder(
        pkg="tor",
        description="Dialogue at the broomer.",
        metadata={
            "area": "broomer",
        },
        paths=[
            "dialogue/broomer/brooms.rst",
            "dialogue/broomer/rapunzel.rst",
            "dialogue/broomer/money.rst",
            "dialogue/broomer/witches.rst",
            "dialogue/broomer/comedy.rst",
            "dialogue/broomer/progress.rst",
            "dialogue/broomer/injuries.rst"
        ],
        interludes=itertools.repeat(tor.rules.apply_rules)
    ),

    SceneScript.Folder(
        pkg="tor",
        description="Dialogue at the butcher.",
        metadata={
            "area": "butcher",
        },
        paths=[
            "dialogue/butcher/brooms.rst",
            "dialogue/butcher/rapunzel.rst",
            "dialogue/butcher/money.rst",
            "dialogue/butcher/witches.rst",
            "dialogue/butcher/comedy.rst",
            "dialogue/butcher/progress.rst",
            "dialogue/butcher/injuries.rst"
        ],
        interludes=itertools.repeat(tor.rules.apply_rules)
    ),

    SceneScript.Folder(
        pkg="tor",
        description="Dialogue in the chamber.",
        metadata={
            "area": "chamber",
        },
        paths=[
            "dialogue/chamber/brooms.rst",
            "dialogue/chamber/rapunzel.rst",
            "dialogue/chamber/money.rst",
            "dialogue/chamber/witches.rst",
            "dialogue/chamber/comedy.rst",
            "dialogue/chamber/progress.rst",
            "dialogue/chamber/injuries.rst"
        ],
        interludes=itertools.repeat(tor.rules.apply_rules)
    ),

    SceneScript.Folder(
        pkg="tor",
        description="Dialogue on the balcony.",
        metadata={
            "area": "chemist",
        },
        paths=[
            "dialogue/chemist/brooms.rst",
            "dialogue/chemist/rapunzel.rst",
            "dialogue/chemist/money.rst",
            "dialogue/chemist/witches.rst",
            "dialogue/chemist/comedy.rst",
            "dialogue/chemist/progress.rst",
            "dialogue/chemist/injuries.rst"
        ],
        interludes=itertools.repeat(tor.rules.apply_rules)
    ),

    SceneScript.Folder(
        pkg="tor",
        description="Dialogue while inbound.",
        metadata={
            "area": "inbound",
        },
        paths=[
            "dialogue/inbound/brooms.rst",
            "dialogue/inbound/rapunzel.rst",
            "dialogue/inbound/money.rst",
            "dialogue/inbound/witches.rst",
            "dialogue/inbound/comedy.rst",
            "dialogue/inbound/progress.rst",
            "dialogue/inbound/injuries.rst"
        ],
        interludes=itertools.repeat(tor.rules.apply_rules)
    ),

    SceneScript.Folder(
        pkg="tor",
        description="Dialogue on the outward.",
        metadata={
            "area": "outward",
        },
        paths=[
            "dialogue/outward/brooms.rst",
            "dialogue/outward/rapunzel.rst",
            "dialogue/outward/money.rst",
            "dialogue/outward/witches.rst",
            "dialogue/outward/comedy.rst",
            "dialogue/outward/progress.rst",
            "dialogue/outward/injuries.rst"
        ],
        interludes=itertools.repeat(tor.rules.apply_rules)
    ),

    SceneScript.Folder(
        pkg="tor",
        description="Dialogue at the stylist.",
        metadata={
            "area": "stylist",
        },
        paths=[
            "dialogue/stylist/brooms.rst",
            "dialogue/stylist/rapunzel.rst",
            "dialogue/stylist/money.rst",
            "dialogue/stylist/witches.rst",
            "dialogue/stylist/comedy.rst",
            "dialogue/stylist/progress.rst",
            "dialogue/stylist/injuries.rst"
        ],
        interludes=itertools.repeat(tor.rules.apply_rules)
    ),
]
