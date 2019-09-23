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
                metadata={"location": locn},
                paths=[],
                interludes=itertools.repeat(call_rules)
            ) for locn in "BFWHGfBC"
        ]

    def test_single(self):
        matcher = Matcher(self.folders)
        folder = next(matcher.options(self.folders[0].metadata))
        state = State(
            folder.metadata["location"],
            self.length, self.growth, self.cut,
            self.coins, self.health_max
        )
        for metadata in [i.metadata for i in self.folders]:
            folder = next(matcher.options(metadata))
            interlude = next(folder.interludes)
            metadata = state._asdict()
            metadata.update(interlude(folder, None, [], **state._asdict()))
            state = State(**metadata)
            print(state)
