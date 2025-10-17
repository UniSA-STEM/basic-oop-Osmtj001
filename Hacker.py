"""
File: Hacker.py
Description: <This module contains data for the 'Hacker' alongside code which will allow the hackers to perform functions.>
Author: <Trent Osmond>
ID: <110316757>
Username: <Osmtj001>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

#Import 'Asset' file to call functions from
from Asset import Asset

class Hacker:

    #Initializing hacker function. Will contain required values for the hacker class
    def __innit__(self, name):
        self.name = name
        self.inventory = [Asset('CryptoToken')]
        self.rig = None
        self.traceLevel = 0
        self.traceThreshold = 5

    #Function which will return a list of items contained within the hacker inventory. If nothing is in the inventory, the user is advised
    def inventoryList(self):
        if not self.inventory:
            return 'Inventory is empty'
        return ', '.join(str(item) for item in self.inventory)

    def Exposed(self):
        if self.traceLevel >= self.traceThreshold:
            return 'Exposed'

