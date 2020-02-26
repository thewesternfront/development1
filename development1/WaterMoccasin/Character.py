#!/usr/bin/python

"""
Author: Troy West
Date: 3/16/2019
Purpose: Create Character
"""
from Backpack import Backpack


class Character:

    # Constructor
    def __init__(self, chname, chrace, chclass, chhitpoints, chmagicpoints):
        self.charactername = chname
        self.characterrace = chrace
        self.characterclass = chclass
        self.characterhitpoints = chhitpoints
        self.charactermagicpoints = chmagicpoints
        self.characterbackpack = Backpack

    def showDetails(self):
        print("Character Details: " + self.charactername + " " + self.characterrace + " " + self.characterclass + " " +
              str(self.charactermagicpoints) + " " + str(self.charactermagicpoints))

    # Setters
    def setName(self, newname):
        self.charactername = newname

    def setRace(self, newrace):
        self.characterrace = newrace

    def setClass(self, newclass):
        self.characterclass = newclass

    def setHitPoints(self, newhitpoints):
        self.characterhitpoints = newhitpoints

    def setMagicPoints(self, newmagicpoints):
        self.charactermagicpoints = newmagicpoints

    # Getters
    def getName(self):
        return self.charactername

    def getRace(self):
        return self.characterrace

    def getClass(self):
        return self.characterclass

    def getHitPoints(self):
        return self.characterhitpoints

    def getMagicPoints(self):
        return self.charactermagicpoints
