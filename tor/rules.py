#!/usr/bin/env python3
# encoding: utf-8

import fractions
import itertools
import random

strategy = "BFWHGFBC"

tower = 12
playtime_s = 20 * 60
health_max = 100
coins = 0
growth = fractions.Fraction(1, 80)
length = 12
cut = 1
delta = 1

health_drop = fractions.Fraction(length / health_max)
coin_for_hair = 1  # per metre
coin_for_health = fractions.Fraction(1, 40)
growth_for_coin = fractions.Fraction(1, 400)

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
            health = max(0, health - max(0, health_drop * (tower - length)))
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
        yield (n, locn, int(length), coins, int(health), cut)

if __name__ == "__main__":
    print(*operate(), sep="\n")
