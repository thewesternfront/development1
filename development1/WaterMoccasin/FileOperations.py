#!/usr/bin/python

"""
Author: Troy West
Date: 3/21/2019
Purpose: File Operations for Saving and Loading the game and other miscellaneous file operations
"""

from water_moccasin.Item import Item

"""
dump a Python Dictionary to a file in json format
"""


class FileOperations:

    def writeFile(self, mylist):
        f = open('/Users/cymru/Desktop/sample.json', 'w')

        for items in mylist:
            f.write(items + "\n")
        f.close()

    def readFile(self, mylist):
        newitem = Item("", "", "", "")
        cnt = 0
        with open('/Users/cymru/Desktop/sample.json') as fp:
            lines = fp.read().splitlines()

        fp.close()
        return mylist
