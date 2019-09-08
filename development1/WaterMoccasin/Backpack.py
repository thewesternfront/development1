#!/usr/bin/python

"""
Author: Troy West
Date: 3/17/2019
Purpose: Create a Backpack to store Character Items
The Items will be Python Objects that are returned
after indexing the item type with a string descriptor
"""

import Item as Item


class Backpack:
    # backpack dictionary
    backpack = {}

    def addItemToBackpack(self, itemadd):
        print("adding item")
        ikey = itemadd.itemname
        print(ikey)
        ivalue = itemadd
        print(ivalue)
        self.backpack.update({ikey: ivalue})

    def getItemFromBackpack(self, itemget):
        print("getting item")
        return self.backpack.get(itemget.itemname)

    def findItemInBackpack(self, iname):
        finditem = Item
        print("finding item")
        finditem = self.backpack.get(iname)
        return finditem
