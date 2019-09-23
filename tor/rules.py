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
from collections import OrderedDict
import random
from collections import namedtuple
import fractions
import itertools
import pprint
import random
import statistics
import sys

from turberfield.dialogue.model import SceneScript

folders = [
    SceneScript.Folder(
        pkg="tor",
        description="",
        metadata={"location": locn},
        paths=[],
        interludes=None
    ) for locn in "BFWHGfBC"
]

tower = 12
playtime_s = 20 * 60
health_max = 100
coins = 0
growth = fractions.Fraction(1, 80)
length = 12
cut = 1
delta = 1

health_drop = fractions.Fraction(health_max / length)
coin_for_hair = 1  # per metre
coin_for_health = fractions.Fraction(1, 40)
growth_for_coin = fractions.Fraction(1, 800)

State = namedtuple(
    "State",
    ["area", "hair_m", "hair_d", "cut_m", "coins_n", "health_n"]
)

def apply_rules(folder, index, entities, state, choice=None):
    area = folder.metadata["area"]
    if area == "C":
        choice = (
            choice if choice is not None
            else random.choice([delta, 0 , -delta])
        )
        cut = max(0, state.cut_m + choice)
        state = state._replace(cut_m=cut, hair_m=max(0, state.hair_m - cut))
    elif area == "F":
        damage = health_drop * (tower - state.hair_m)
        state = state._replace(health_n=max(0, state.health_n - max(0, damage)))
        if state.health_n == 0:
            return {}
    elif area == "W":
        state = state._replace(
            coins_n=state.coins_n + coin_for_hair * state.cut_m
        )
    elif area == "H":
        cost = min(
            state.coins_n,
            int((health_max - state.health_n) * coin_for_health)
        )
        state = state._replace(
            coins_n=state.coins_n - cost,
            health_n=int(state.health_n + cost / coin_for_health)
        )
    elif area == "G":
        choice = (
            choice if choice is not None
            else random.choice([i * coin_for_hair for i in (0, 1, 2, 5)])
        )
        cost = min(state.coins_n, choice)
        state = state._replace(
            coins_n=state.coins_n - cost,
            hair_d=state.hair_d + cost * growth_for_coin
        )
    elif area == "f":
        # Game will check it's possible to get back up.
        pass

    state = state._replace(hair_m=state.hair_m + state.hair_m * state.hair_d)
    return state._asdict()
