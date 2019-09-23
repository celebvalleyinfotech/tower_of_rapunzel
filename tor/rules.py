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

strategy = "BFWHGFBC"

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

State = namedtuple("State", ["location", "hair_m", "chop_m", "coins_n", "health_n"])

def pathway(n_cycles=int(playtime_s / 9 / len(strategy))):
    return itertools.chain.from_iterable(itertools.repeat(strategy, n_cycles))

def operate(coins=coins, cut=cut, growth=growth, health=health_max, length=length):
    for n, locn in enumerate(pathway()):
        if locn == "C":
            # Rapunzel's hair is ?m long. How much do you want to cut?
            # NB: Waiting allows it to grow.
            choice = random.choice([delta, 0 , -delta])
            cut = max(0, cut + choice)
            length = max(0, length - cut)
        elif locn == "F":
            if n == 1:
                damage = health_drop * (tower - length)
                health = max(0, health - max(0, damage))
            if health == 0:
                return
        elif locn == "W":
            coins += coin_for_hair * cut
        elif locn == "H":
            cost = min(coins, int((health_max - health) * coin_for_health))
            coins -= cost
            health += cost / coin_for_health
        elif locn == "G":
            choice = random.choice([i * coin_for_hair for i in (0, 1, 2, 5)])
            cost = min(coins, choice)
            coins -= cost
            growth += cost * growth_for_coin

        length += length * growth
        yield State(locn, int(length), cut, coins, int(health))

if __name__ == "__main__":
    n_runs = 5000
    runs = [list(operate()) for i in range(n_runs)]
    ranking = sorted(runs, key=lambda x: x[-1].coins_n, reverse=True)
    outcomes = [i[-1].coins_n for i in ranking]
    pprint.pprint(ranking[0])
    try:
        print(
            *statistics.quantiles(outcomes, n=n_runs // 4, method="inclusive"),
            sep="\n",
            file=sys.stderr
        )
    except AttributeError:
        pass
    # Bronze: 15, Silver: 20: Gold: 25
