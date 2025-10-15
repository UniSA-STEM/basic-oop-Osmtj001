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

#Returns the user with the Rig's condition based on damage & upgrade level. If the rig is on or exceeds 2 damage the broken value will be updated to 'True' for the rig
    def rigCondition(self):

        if self.damageCounter == 0:
            return (f'Pristine ({self.upgradeLevel})')
        elif self.damageCounter == 1:
            return (f'Damaged ({self.upgradeLevel})')
        elif self.damageCounter >= (self.upgradeLevel + 2):
            self.broken = True
            return (f'Broken ({self.upgradeLevel})')

#Function which will be called when taking damage. Will update prior rigCondition function & display new damage/ condition
    def takeDamage(self):

        if self.broken == True:
            print(f'{self.name} is already broken')


        self.damageCounter += 1
        print(f'{self.name}: Taking {self.damageCounter} damage')

        if self.upgradeLevel == 0 and self.damageCounter >= 2:
            self.broken = True
            print(f'{self.name} has been critically damaged and no longer function. {self.name} is now broken')

        elif self.upgradeLevel == 1 and self.damageCounter >= 3:
            self.broken = True
            print(f'{self.name} has been critically damaged and no longer function. {self.name} is now broken')

        elif self.upgradeLevel == 2 and self.damageCounter >= 4:
            self.broken = True
            print(f'{self.name} has been critically damaged and no longer function. {self.name} is now broken')

        print(f'{self.name} Current Condition: {self.rigCondition()}')

#Function to prompt the user if they would like to repair for 1x CryptoToken. If not, the user is returned out of the function. Function will call on the user inventory & update if a token is taken
    def rigRepair(self, hacker):


        token = next((a for a in hacker.inventory if a.name.lower() == 'cryptotoken'), None)

        if not token:
            print(f'{hacker.name} has insufficient tokens to repair {self.name}')
            return


        if not self.broken:
            print(f'{self.name} is not in need of repair')

        elif self.broken:
            repair= input(f'{self.name} is broken, would you like to use 1x CryptoToken to repair?')
            while repair not in ('yes', 'no'):
                repair= input('Please enter yes or no if you would like to use 1x CryptoToken to repair?').lower()

            if repair == 'yes':
                hacker.inventory.remove(token)
                self.damageCounter = 0
                self.broken = False
                print(f'{self.name} has been repaired using 1x CryptoToken')
                print(f'Condition restored back to: {self.rigCondition()}')

            else:
                print(f'{self.name} has not been repaired')
            return





