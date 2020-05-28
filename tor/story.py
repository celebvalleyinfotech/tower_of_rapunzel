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
import math
import pprint

from turberfield.dialogue.model import SceneScript
from turberfield.dialogue.types import DataObject
from turberfield.dialogue.types import Persona
from turberfield.dialogue.types import Stateful

import tor
import tor.rules

version = tor.__version__


class Hanging(enum.Enum):
    crib = enum.auto()
    club = enum.auto()


class Occupation(enum.Enum):
    butcher = enum.auto()
    broomer = enum.auto()
    chemist = enum.auto()
    stylist = enum.auto()
    teenager = enum.auto()


class Narrator(DataObject):

    state = None
    settings = None

    @property
    def coins_n(self):
        return format(self.state.coins_n)

    @property
    def damage_bars(self):
        damage = max(0, (
            self.settings.TOWER_M - self.state.hair_m
        ) * self.settings.HEALTH_D)
        bars = 10 * damage / self.settings.HEALTH_MAX
        return round(bars)

    @property
    def hair_m(self):
        return "{0:.1f}".format(float(self.state.hair_m))

    @property
    def health_n(self):
        return "{0:.1f}".format(float(self.state.health_n))


class Character(Stateful, Persona):
    pass


ensemble = [
    Narrator(settings=tor.rules.Settings),
    Character(name="Rapunzel").set_state(Occupation.teenager, Hanging.crib),
    Character(name="Hickory McFly").set_state(Occupation.broomer),
    Character(name="Ricky Butcher").set_state(Occupation.butcher),
    Character(name="Poppy Pills").set_state(Occupation.chemist),
    Character(name="Wigmore Watkins").set_state(Occupation.stylist),
]


folders = [

    SceneScript.Folder(
        pkg="tor",
        description="Dialogue on the balcony.",
        metadata={
            "area": "balcony",
        },
        paths=[
            "dialogue/balcony/view.rst",
        ],
        interludes=None
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
        interludes=None
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
        interludes=None
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
        interludes=None
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
        interludes=None
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
        interludes=None
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
        interludes=None
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
        interludes=None
    ),
]

if __name__ == "__main__":
    pprint.pprint(folders)
