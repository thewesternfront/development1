#!/usr/bin/python

"""
Author: Troy West
Date: 3/16/2019
Purpose: Create Character
"""

import random
from Logger import Logger
from Character import Character

class BattleEngine:


    def calculatePlayerStats(self):
        pass

    def engineTest(self, opponents):

        logger = Logger()

        # These should be generated from character stats and dice rolls ...
        attack = 50
        defense = 35
        basedamage = 50
        crit = 0


        # calculate critical damage
        crit = (random.choice([0.5, 0.6, 0.7, 0.9, 0.9, 1.0]))

        print("Basic battle")
        damage = (attack/defense) * basedamage * crit
        print(f"you did {damage} damage")
        logger.logEvent(f"you did {damage} damage", "DEBUG")

        # Log passed in opponent name
        logger.logEvent(opponents[0].charactername, "DEBUG")


