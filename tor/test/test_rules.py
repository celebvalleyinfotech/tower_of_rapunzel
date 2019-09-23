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

import fractions
import itertools
import unittest

from turberfield.dialogue.matcher import Matcher
from turberfield.dialogue.model import SceneScript

from tor.rules import call_rules
from tor.rules import State


class RulesTests(unittest.TestCase):

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

    @staticmethod
    def pathway(folders, n_cycles):
        return itertools.chain.from_iterable(
            itertools.repeat(folders, n_cycles)
        )

    def setUp(self):
        self.folders = [
            SceneScript.Folder(
                pkg="tor",
                description="",
                metadata={"area": locn},
                paths=[],
                interludes=itertools.repeat(call_rules)
            ) for locn in "BFWHGfBC"
        ]

    def simulate(self, folders, n_cycles=1):
        matcher = Matcher(folders)
        state = State(
            folders[0].metadata["area"],
            self.length, self.growth, self.cut,
            self.coins, self.health_max
        )
        folder = folders[0]
        for f in self.pathway(folders, n_cycles):
            metadata = state._asdict()
            interlude = next(folder.interludes)
            metadata.update(interlude(folder, None, [], state))
            metadata["area"] = f.metadata["area"]
            folder = next(matcher.options(metadata))
            state = State(**metadata)
            yield state

    def test_single(self):
        states = list(self.simulate(self.folders))
        self.assertEqual("B", states[0].area)
        self.assertEqual("C", states[-1].area)

    def test_many(self):
        runs = [list(self.simulate(self.folders, 16)) for i in range(5000)]
        ranking = sorted(runs, key=lambda x: x[-1].coins_n, reverse=True)
        print(ranking[0])

