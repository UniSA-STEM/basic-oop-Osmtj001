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

#Initialising Hacker & Rig for simulation. The hacker & rig names are not case sensitive
print('***Initial Assignment of Hacker Name & Rig Name***')
Jane = Hacker('Jane')
Steve = Hacker('Steve')
rig1 = Rig('Orion')
rig2 = Rig('Didox')

#Assigns the Rig to a Hacker. In this case Rig1 has been assigned to Jane
print('***Rig Acquisition by the Hacker***')
Jane.rigAcquisition(rig1)
Steve.rigAcquisition(rig2)

#Generating assets for Rig storage. All items which cannot go into rig storage will be allocated to the Hackers inventory
print('***Rig 1 & 2 have generated assets***')
rig1.generateAsset(Jane)
rig1.generateAsset(Jane)
rig1.generateAsset(Jane)
rig1.generateAsset(Jane)
rig2.generateAsset(Steve)
rig2.generateAsset(Steve)
rig2.generateAsset(Steve)

#This will find a specific item & store it within the hacker inventory. If no asset is given, all items will be transferred
print('***Functionality for storing items in Rig***')
Jane.storeInRig('Security Chip')
Steve.storeInRig()

#Takes a Crypto Token (if stores with inventory) & Encrypts with the use of 1x Security Chip (if available)
print('***Encryption of item***')
Steve.encryption('CryptoToken')

print('***Upgrading of Rig***')
Steve.upgradeRig()

Steve.attack(rig1)

print('***Retrival of all asstets from Rig***')
Steve.rigRetrival('Security Chip')