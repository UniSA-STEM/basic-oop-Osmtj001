"""
File: main.py
Description: <This main module will contain code which allows the user to interact with the programme. This will call upon functions & data from other associated Modules.>
Author: <Trent Osmond>
ID: <110316757>
Username: <Osmtj001>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
#Initialises all required files
from Hacker import Hacker
from Rig import Rig
from Asset import Asset
import random

Jane = Hacker('Jane')
Steve = Hacker('Steve')

rig1 = Rig('Orion')
rig2 = Rig('Didox')

Jane.rigAcquisition(rig1)
Steve.rigAcquisition(rig2)

rig1.generateAsset(Jane)
rig2.generateAsset(Steve)
rig2.generateAsset(Steve)
rig2.generateAsset(Steve)

Jane.storeInRig()
Steve.storeInRig()

Steve.encryption('CryptoToken')

Steve.upgradeRig()
Jane.rigRetrival()

print(Steve)