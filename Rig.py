"""
File: Rig.py
Description: <This module contains data for the 'rig' and all associated functions.>
Author: <Trent Osmond>
ID: <110316757>
Username: <Osmtj001>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

#Class for rig & user input
class Rig:

    def __init__(self, name, damageCounter, broken, storage, dataSpikes, removableDrive, upgradeLevel):
        self.name = name
        self.damageCounter = 0
        self.broken = False
        self.storage = []
        self.dataSpikes = 2
        self.removableDrive = 1
        self.upgradeLevel = 0