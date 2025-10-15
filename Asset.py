"""
File: Asset.py
Description: <This module contains assets which are called upon by the 'main' module.>
Author: <Trent Osmond>
ID: <110316757>
Username: <Osmtj001>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Asset:


#Will represent assets within the Main Module. These assets can become encrypted, and used by hackers within the main Module or stores in the Rigs

    def __init__(self, name:str, description:str):
        self.name = name
        self.description = description
        self.encrypted = False


    def encrypt(self):

        if self.encrypted == False:
            self.encrypted = True
            print(f'{self.name} Has been encrypted within the Main Module.')

        else:
            print(f'{self.name} Has been already been encrypted within the Main Module.')


    def decrypt(self):
        if self.encrypted == True:
            print(f'{self.name} Has been decrypted within the Main Module.')
        else:
            print(f'{self.name} Has been already been decrypted within the Main Module.')