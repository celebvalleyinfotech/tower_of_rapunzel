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

import enum
import itertools

from turberfield.dialogue.model import SceneScript
from turberfield.dialogue.types import DataObject
from turberfield.dialogue.types import Persona
from turberfield.dialogue.types import Stateful

import tor
import tor.rules

version = tor.__version__


class At(enum.Enum):
    crib = 0
    club = 1


class Narrator:

    state = None

    @property
    def coins_n(self):
        return format(self.state.coins_n)

    @property
    def hair_m(self):
        return "{0:.1f}".format(float(self.state.hair_m))


class Character(Stateful, Persona): pass
class Butcher(Character): pass
class Broomer(Character): pass
class Chemist(Character): pass
class Stylist(Character): pass
class Rapunzel(Character): pass

ensemble = [
    Narrator(),
    Rapunzel(name="Rapunzel").set_state(At.crib),
    Broomer(name="Hickory McFly"),
    Butcher(name="Ricky Butcher"),
    Chemist(name="Poppy Pills"),
    Stylist(name="Wigmore Watkins"),
]

episodes = [

    SceneScript.Folder(
        pkg="tor",
        description="Dialogue on the balcony.",
        metadata={
            "area": "balcony",
        },
        paths=[
            "dialogue/balcony/view.rst",
        ],
        interludes=itertools.repeat(None)
    ),

    SceneScript.Folder(
        pkg="tor",
        description="Dialogue at the broomer.",
        metadata={
            "area": "broomer",
        },
        paths=[
            "dialogue/broomer/brooms.rst",
        ],
        interludes=itertools.repeat(None)
    ),

    SceneScript.Folder(
        pkg="tor",
        description="Dialogue at the butcher.",
        metadata={
            "area": "butcher",
        },
        paths=[
            "dialogue/butcher/meat.rst",
        ],
        interludes=itertools.repeat(None)
    ),

    SceneScript.Folder(
        pkg="tor",
        description="Dialogue in the chamber.",
        metadata={
            "area": "chamber",
        },
        paths=[
            "dialogue/chamber/rap.rst",
        ],
        interludes=itertools.repeat(None)
    ),

    SceneScript.Folder(
        pkg="tor",
        description="Dialogue at the chemist.",
        metadata={
            "area": "chemist",
        },
        paths=[
            "dialogue/chemist/pills.rst",
        ],
        interludes=itertools.repeat(None)
    ),

    SceneScript.Folder(
        pkg="tor",
        description="Dialogue while inbound.",
        metadata={
            "area": "inbound",
        },
        paths=[
            "dialogue/inbound/jump.rst",
        ],
        interludes=itertools.repeat(None)
    ),

    SceneScript.Folder(
        pkg="tor",
        description="Dialogue on the outward.",
        metadata={
            "area": "outward",
        },
        paths=[
            "dialogue/outward/fall.rst",
            "dialogue/outward/death.rst",
        ],
        interludes=itertools.repeat(None)
    ),

    SceneScript.Folder(
        pkg="tor",
        description="Dialogue at the stylist.",
        metadata={
            "area": "stylist",
        },
        paths=[
            "dialogue/stylist/wigs.rst",
        ],
        interludes=itertools.repeat(None)
    ),
]
