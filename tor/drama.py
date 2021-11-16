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

from turberfield.dialogue.matcher import Matcher

from balladeer import Drama
from balladeer import SceneScript

import tor.rules
from tor.types import Character
from tor.types import Hanging
from tor.types import Narrator
from tor.types import Occupation


class Tower(Drama):

    folders = [

        SceneScript.Folder(
            pkg="tor.dialogue.balcony",
            description="Dialogue on the balcony.",
            metadata={
                "area": "balcony",
            },
            paths=["view.rst"],
            interludes=None
        ),

        SceneScript.Folder(
            pkg="tor.dialogue.broomer",
            description="Dialogue at the broomer.",
            metadata={
                "area": "broomer",
            },
            paths=["brooms.rst"],
            interludes=None
        ),

        SceneScript.Folder(
            pkg="tor.dialogue.butcher",
            description="Dialogue at the butcher.",
            metadata={
                "area": "butcher",
            },
            paths=["meat.rst"],
            interludes=None
        ),

        SceneScript.Folder(
            pkg="tor.dialogue.chamber",
            description="Dialogue in the chamber.",
            metadata={
                "area": "chamber",
            },
            paths=["rap.rst"],
            interludes=None
        ),

        SceneScript.Folder(
            pkg="tor.dialogue.chemist",
            description="Dialogue at the chemist.",
            metadata={
                "area": "chemist",
            },
            paths=["pills.rst"],
            interludes=None
        ),

        SceneScript.Folder(
            pkg="tor.dialogue.inbound",
            description="Dialogue while inbound.",
            metadata={
                "area": "inbound",
            },
            paths=["jump.rst"],
            interludes=None
        ),

        SceneScript.Folder(
            pkg="tor.dialogue.outward",
            description="Dialogue on the outward.",
            metadata={
                "area": "outward",
            },
            paths=[
                "fall.rst",
                "death.rst",
            ],
            interludes=None
        ),

        SceneScript.Folder(
            pkg="tor.dialogue.stylist",
            description="Dialogue at the stylist.",
            metadata={
                "area": "stylist",
            },
            paths=["wigs.rst"],
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

    @property
    def ensemble(self):
        return self.population

    @property
    def folder(self):
        location = self.narrator.state.area
        selector = {"area": location}
        matcher = Matcher(self.folders)
        return next(matcher.options(selector))

    @property
    def narrator(self):
        return next((i for i in self.ensemble if isinstance(i, Narrator)), None)

