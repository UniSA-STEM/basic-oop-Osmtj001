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
    def __init__(self, name):
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

    def exposed(self):
        if self.traceLevel >= self.traceThreshold:
            return 'Exposed'

    #Allows Hacker to purchase rig. If hacker has insufficient tokens and error will be displayed
    def rigAcquisition(self, rig):

        if self.rig is not None:
            print(f'{self.name} already has a rig.')
            return

        token = next((item for item in self.inventory if item.name.lower() == 'cryptotoken'), None)
        if not token:
            print(f'{self.name} does not have enough CryptoToken to acquire a rig.')
            return

        self.inventory.remove(token)
        self.rig = rig
        print(f'{self.name} acquired rig: {rig.name}.')

    #Function to allow rig to launch attack, while consuming 1x data spike. If the Hacker does not have a rig, or has insufficient data spikes and error will be returned.
    def attack(self, targetRig):

        if not self.rig:
            print(f'{self.name} does not have a rig to attack from.')

        if self.exposed() == 'Exposed':
            print(f'{self.name} is exposed and cannot launch an attack as their trace level is {self.traceLevel}.')

        dataSpike = [a for a in self.rig.storage if a.name.lower().replace(" ", "") == 'dataspike']

        if not dataSpike:
            print(f'{self.name} does not have sufficient Data Spikes to launch an attack.')
            return

        dataSpike = dataSpike[0]
        self.rig.storage.remove(dataSpike)
        print(f'{self.name} and their rig {self.rig.name} have launched a Data Spike at {targetRig.name}.')
        targetRig.takeDamage()

        self.traceLevel += 1
        print(f'Trace Level is now {self.traceLevel}.')

        if targetRig.broken:
            print(f'{targetRig.name} is broken, would you like to proceed with data extraction?.')

            removableDrive = [a for a in self.rig.storage if a.name.lower().replace(" ", "") == 'removabledrive']
            removableDrive = [a for a in self.inventory if a. name.lower().replace(" ", "") == 'removabledrive']
            if not removableDrive:
                print(f'{self.rig.name} does not contain a removable drive. Extraction not available.')
                return

        extraction = input(f'Would you like to use 1x Removable Drive to extract assets from {targetRig.name}? (y/n) ')
        while extraction not in ('y', 'n'):
            extraction = input('Please enter "y" or "n": ')

        if extraction == 'n':
            print('Extraction has been cancelled.')
            return

        removableDrive = removableDrive[0]
        if removableDrive in self.rig.storage:
            self.rig.storage.remove(removableDrive)
        else: self.inventory.remove(removableDrive)

        extractedAssets = []
        for asset in list(targetRig.storage):
            if not asset.encrypted:
                targetRig.storage.remove(asset)
                self.inventory.append(asset)
                extractedAssets.append(asset)

        if extractedAssets:
            print(f'Assets have been extracted from {targetRig.name}.')
            for item in extractedAssets:
                print(f' - {item.name}')

        else:
            print(f'{self.name} does not have any assets to extract.')

    #Function to encrypt assets within inventory or rig storage
    def encryption(self, assetName):
        if not self.rig and not self.inventory:
            print(f'{self.name} does not have any assets to encrypt.')
            return

        asset = next(
            (a for a in self.inventory + (self.rig.storage if self.rig else [])
             if a.name.lower().replace(" ", "") == assetName.lower().replace(" ", "")),
            None
        )

        if not asset:
            print(f' Unable to locate asset "{assetName}" to encrypt.')
            return

        chip = next((a for a in self.inventory if a.name.lower().replace(" ", "") == 'securitychip'), None)
        if not chip:
            print(f' {self.name} does not have an available Security Chip for asset encryption')
            return

        if asset.encrypted:
            print(f'{asset.name} is already encrypted')
            return

        self.inventory.remove(chip)
        asset.encrypted = True
        print(f'{asset.name} has been encrypted with the use of 1x Security Chip.')

    #Reverse or prior function. Allows user to decrypt assets
    def decryption(self, assetName):
        if not self.rig and not self.inventory:
            print(f'{self.name} does not have any assets to decrypt.')
            return

        asset = next(
            (a for a in self.inventory + (self.rig.storage if self.rig else [])
             if a.name.lower().replace(" ", "") == assetName.lower().replace(" ", "")),
            None
        )

        if not asset:
            print(f' Unable to locate asset "{assetName}" to decrypt.')
            return

        chip = next((a for a in self.inventory if a.name.lower().replace(" ", "") == 'securitychip'), None)
        if not chip:
            print(f' {self.name} does not have an available Security Chip for asset decryption')
            return

        if not asset.encrypted:
            print(f'{asset.name} is not encrypted')
            return

        self.inventory.remove(chip)
        asset.encrypted = False
        print(f'{asset.name} has been decrypted with the use of 1x Security Chip.')


    def formatting(self, s:str):
        return s.lower().replace(" ", "").replace('-', '')

    def findAsset(self, container: list, assetName: str):
        key = self.formatting(assetName)
        return next((a for a in container if self.formatting(a.name) == key), None)

    def storeInRig(self, assetName: str = None):
        if not self.rig:
            print(f'{self.name} does not have any assets to store in Rig.')
            return

        allowedItems = {'dataspike', 'removabledrive', 'securitychip'}

        moved = []

        if assetName:
            asset = self.findAsset(self.inventory, assetName)
            if not asset:
                print(f' {self.name} does not have {assetName} in Inventory.')
                return
            if self.formatting(asset.name) not in allowedItems:
                print(f' {assetName} cannot be stored in Rig.')
                return

            self.inventory.remove(asset)
            self.rig.storage.append(asset)
            moved.append(assetName)
        else:
            availableAssets = [a for a in list(self.rig.storage) if self.formatting(a.name) in allowedItems]
            if not availableAssets:
                print('No items located within Inventory are allowed to be stored in Rig.')
                return
            for asset in availableAssets:
                self.inventory.remove(asset)
                self.rig.storage.append(asset)
                moved.append(asset)

        if moved:
            print(f' Stored to {self.rig.name}: {', '.join(a.name for a in moved)}")
        return moved


    #String function to display key variables from 'Hacker' class
    def __str__(self):
        rigName = self.rig.name if self.rig else 'None'
        exposed = 'Exposed' if self.exposed() else 'Not Exposed'
        return (
        f'Hacker: {self.name}{exposed}\n'
        f'Rig: {self.rig.name}\n'
        f'Trace Level: {self.traceLevel}\n'
        f'Inventory: {self.inventoryList()}'
          )
