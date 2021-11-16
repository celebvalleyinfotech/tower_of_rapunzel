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

from balladeer import Drama
from balladeer import SceneScript

from tor.types import Character
from tor.types import Narrator


class Tower(Drama):

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.population = [
            Narrator(
                settings=tor.rules.Settings,
                state=tor.rules.State(
                    "balcony",
                    tor.rules.Settings.HAIR_M,
                    tor.rules.Settings.HAIR_D,
                    tor.rules.Settings.CUT_M,
                    0,
                    tor.rules.Settings.COINS_N,
                    tor.rules.Settings.HEALTH_MAX
                ),
            ),
            Character(name="Rapunzel").set_state(Occupation.teenager, Hanging.crib),
            Character(name="Mr Hickory McFly").set_state(Occupation.broomer),
            Character(name="Mr Ricky Butcher").set_state(Occupation.butcher),
            Character(name="Ms Poppy Pills").set_state(Occupation.chemist),
            Character(name="Mr Wigmore Watkins").set_state(Occupation.stylist),
        ]


