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

from collections import namedtuple
import fractions
import random
import re

from turberfield.dialogue.model import SceneScript

choice_validator = re.compile("\d+$")


class Settings:
    COINS_N = 0
    CUT_D = 1
    CUT_M = 1
    HAIR_C = 1
    HAIR_D = fractions.Fraction(1, 80)
    HAIR_D_C = fractions.Fraction(1, 800)
    HAIR_M = 12
    HEALTH_C = fractions.Fraction(1, 40)
    HEALTH_MAX = 100
    TOWER_M = 12
    HEALTH_D = fractions.Fraction(HEALTH_MAX / TOWER_M)

topology = {
    "balcony": ("chamber", "outward"),
    "broomer": ("butcher", "chemist", "inbound", "stylist"),
    "butcher": ("broomer", "chemist", "inbound", "stylist"),
    "chamber": ("balcony",),
    "chemist": ("broomer", "butcher", "inbound", "stylist"),
    "inbound": ("balcony", "broomer", "butcher", "chemist", "stylist"),
    "outward": ("balcony", "broomer", "butcher", "chemist", "stylist"),
    "stylist": ("broomer", "butcher", "chemist", "inbound"),
}

State = namedtuple(
    "State",
    ["area", "hair_m", "hair_d", "cut_m", "coins_n", "health_n"]
)

def apply_rules(
    folder, index, entities, settings, state, choice=None
):
    if state.area == "chamber":
        choice = (
            choice if choice is not None
            else random.choice([settings.CUT_D, 0 , -settings.CUT_D])
        )
        cut = max(0, state.cut_m + choice)
        state = state._replace(cut_m=cut, hair_m=max(0, state.hair_m - cut))
    elif state.area == "outward":
        damage = settings.HEALTH_D * (settings.TOWER_M - state.hair_m)
        state = state._replace(health_n=max(0, state.health_n - max(0, damage)))
        if state.health_n == 0:
            return {}
    elif state.area == "stylist":
        state = state._replace(
            coins_n=state.coins_n + settings.HAIR_C * state.cut_m
        )
    elif state.area == "chemist":
        cost = min(
            state.coins_n,
            int((settings.HEALTH_MAX - state.health_n) * settings.HEALTH_C)
        )
        state = state._replace(
            coins_n=state.coins_n - cost,
            health_n=int(state.health_n + cost / settings.HEALTH_C)
        )
    elif state.area == "butcher":
        choice = (
            choice if choice is not None
            else random.choice(
                [i * settings.HAIR_C for i in (0, 1, 2, 5)]
            )
        )
        cost = min(state.coins_n, choice)
        state = state._replace(
            coins_n=state.coins_n - cost,
            hair_d=state.hair_d + cost * settings.HAIR_D_C
        )
    elif state.area == "inbound":
        # Game will check it's possible to get back up.
        pass

    state = state._replace(hair_m=state.hair_m + state.hair_m * state.hair_d)
    return state._asdict()
