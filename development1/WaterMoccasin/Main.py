#!/usr/bin/python

"""
Author: Troy West
Date: 3/16/2019
Purpose: Main
"""

from WaterMoccasin.Backpack import Backpack
from WaterMoccasin.Character import Character
from WaterMoccasin.Item import Item
from WaterMoccasin.Logger import Logger


def createCharacter():
    troy = Character("Troy", "Welsh", "Mesmer", 100, 100)
    troy.showDetails()

    # createa single item
    troysweapon = Item("Staff Of Ice", "Staff", 3, 4)
    troystunic = Item("Tunic Of Ice", "Armor", 10, 10)

    # add item to backpack dict
    troy.characterbackpack.addItemToBackpack(Backpack, troysweapon)
    troy.characterbackpack.addItemToBackpack(Backpack, troystunic)

    # get the entire Item Object by Item Class Name
    newweapon = troy.characterbackpack.getItemFromBackpack(Backpack, troysweapon)
    print("This is the name of my new item")
    print(newweapon.itemname)
    # get the entire Item Object by Item Class Name
    newarmor = troy.characterbackpack.getItemFromBackpack(Backpack, troystunic)
    print("This is the name of my new item")
    print(newarmor.itemname)

    # get the entire object by Dict index - a string value
    newitem = troy.characterbackpack.findItemInBackpack(Backpack, "Tunic Of Ice")
    print(newitem.itemname)
    print(newitem.itemsize)


def main():
    logs = Logger()
    print("main method")
    createCharacter()
    logs.logEvent("this is a new event", 'DEBUG')



if __name__ == "__main__":
    main()
