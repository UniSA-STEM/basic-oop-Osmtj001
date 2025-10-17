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


    def rigAcquisition(self, rig):

        if self.rig is not None:
            print(f'{self.name} already has a rig.')
            return

        token = next((item for item in self.inventory if item.name.lower() == 'cryptotoken'), None)
        if not token:
            print(f'{self.name} does not have enough CryptoToken to acquire a rig.')
            return

    #String function to display key variables from 'Hacker' class
    def __str__(self):
        rigName = self.rig.name if self.rig else 'None'
        exposed = 'Exposed' if self.Exposed() else 'Not Exposed'
        return (
        f'Hacker: {self.name}{exposed}\n'
        f'Rig: {rig.name}\n'
        f'Trace Level: {self.traceLevel}\n'
        f'Inventory: {self.inventoryList()}'
          )
