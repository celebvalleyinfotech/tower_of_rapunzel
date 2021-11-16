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
import unittest

from turberfield.dialogue.matcher import Matcher

from tor.drama import Tower
import tor.rules
import tor.types


class RulesTests(unittest.TestCase):

    folders = [
        next(
            i for i in Tower.folders
            if i.metadata["area"] == a
        )
        for a in (
            "balcony", "outward",
            "stylist", "chemist", "butcher", "broomer",
            "inbound", "balcony", "chamber"
        )
    ]

    settings = tor.rules.Settings

    @staticmethod
    def pathway(folders, n_cycles):
        return itertools.chain.from_iterable(
            itertools.repeat(folders, n_cycles)
        )

    def simulate(self, folders, n_cycles=1):
        matcher = Matcher(folders)
        state = tor.rules.State(
            folders[0].metadata["area"],
            self.settings.HAIR_M,
            self.settings.HAIR_D,
            self.settings.CUT_M,
            0,
            self.settings.COINS_N,
            self.settings.HEALTH_MAX
        )
        folder = folders[0]
        for f in self.pathway(folders, n_cycles):
            metadata = state._asdict()
            rv = tor.rules.apply_rules(folder, None, [], self.settings, state)
            if rv:
                metadata.update(rv)
            else:
                continue
            metadata["area"] = f.metadata["area"]
            folder = next(matcher.options(metadata))
            state = tor.rules.State(**metadata)
            yield state

    def test_single_cycle(self):
        states = list(self.simulate(self.folders))
        self.assertEqual("balcony", states[0].area)
        self.assertEqual("chamber", states[-1].area)

    def test_competition(self):
        # Bronze: 20, Silver: 25: Gold: 30
        runs = [
            list(self.simulate(self.folders, 16))
            for i in range(1000)
        ]
        ranking = sorted(runs, key=lambda x: x[-1].coins_n, reverse=True)
        self.assertGreaterEqual(ranking[-1][-1].coins_n, 0)
        self.assertLess(ranking[-1][-1].coins_n, 2)
        self.assertGreater(ranking[0][-1].coins_n, 25)
        self.assertLess(ranking[0][-1].coins_n, 42)

    def test_topology(self):
        for location, options in tor.rules.topology.items():
            if location == "chamber":
                self.assertIn("balcony", options)
            elif location == "balcony":
                self.assertIn("chamber", options)
                self.assertIn("outward", options)
            elif location == "outward":
                self.assertIn("balcony", options)
                self.assertIn("stylist", options)
                self.assertIn("chemist", options)
                self.assertIn("butcher", options)
                self.assertIn("broomer", options)
            elif location in (
                "broomer", "butcher", "chemist", "stylist"
            ):
                self.assertIn("broomer", list(options) + [location])
                self.assertIn("butcher", list(options) + [location])
                self.assertIn("chemist", list(options) + [location])
                self.assertIn("stylist", list(options) + [location])
                self.assertIn("inbound", list(options) + [location])

    def test_validation(self):
        validator = tor.rules.choice_validator
        self.assertTrue(validator.match("0"))
        self.assertTrue(validator.match("001"))
        self.assertTrue(validator.match("101"))
        self.assertFalse(validator.match("a"))
        self.assertFalse(validator.match("1a1"))
        self.assertFalse(validator.match("0x11"))
        self.assertFalse(validator.match(""))
