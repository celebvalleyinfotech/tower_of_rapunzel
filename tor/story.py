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


class Progress(enum.Enum):
    a = 0
    b = 1
    c = 2
    d = 3
    e = 5
    f = 10
    g = 12
    h = 15
    i = 20
    j = 25
    k = 30
    l = 35
    m = 40

class Theme(enum.Enum):
    brooms = 0
    comedy = 1
    injuries = 2
    money = 3
    progress = 4
    rapunzel = 5
    witches = 6

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
class Stylist(Character): pass
class Rapunzel(Character): pass

ensemble = [
    #Narrator().set_state(Theme.brooms).set_state(Progress.a),
    Narrator(),
    Rapunzel(name="Rapunzel"),
    Broomer(name="Hickory McFly"),
    Butcher(name="Ricky Butcher"),
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
            "dialogue/balcony/brooms.rst",
            "dialogue/balcony/rapunzel.rst",
            "dialogue/balcony/money.rst",
            "dialogue/balcony/witches.rst",
            "dialogue/balcony/comedy.rst",
            "dialogue/balcony/progress.rst",
            "dialogue/balcony/injuries.rst"
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
            "dialogue/butcher/brooms.rst",
            "dialogue/butcher/rapunzel.rst",
            "dialogue/butcher/money.rst",
            "dialogue/butcher/witches.rst",
            "dialogue/butcher/comedy.rst",
            "dialogue/butcher/progress.rst",
            "dialogue/butcher/injuries.rst"
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
            "dialogue/chemist/brooms.rst",
            "dialogue/chemist/rapunzel.rst",
            "dialogue/chemist/money.rst",
            "dialogue/chemist/witches.rst",
            "dialogue/chemist/comedy.rst",
            "dialogue/chemist/progress.rst",
            "dialogue/chemist/injuries.rst"
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
            "dialogue/inbound/brooms.rst",
            "dialogue/inbound/rapunzel.rst",
            "dialogue/inbound/money.rst",
            "dialogue/inbound/witches.rst",
            "dialogue/inbound/comedy.rst",
            "dialogue/inbound/progress.rst",
            "dialogue/inbound/injuries.rst"
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
            "dialogue/outward/brooms.rst",
            "dialogue/outward/rapunzel.rst",
            "dialogue/outward/money.rst",
            "dialogue/outward/witches.rst",
            "dialogue/outward/comedy.rst",
            "dialogue/outward/progress.rst",
            "dialogue/outward/injuries.rst"
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
