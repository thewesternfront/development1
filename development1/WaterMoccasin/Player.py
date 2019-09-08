#!/usr/bin/python

"""
Author: Troy West
Date: 3/17/2019
Purpose: Create 'Player' that derives from 'Character'
"""
import water_moccasin.Character


class Player(water_moccasin.Character):

    def showDetails(self):
        print(
            "Character Details: " + self.cname + " " + self.crace + " " + self.cclass + " " + str(
                self.chitpoints) + " " + str(self.cmagicpoints))
