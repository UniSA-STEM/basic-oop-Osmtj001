"""
File: Asset.py
Description: <This module contains assets which are called upon by the 'main' module.>
Author: <Trent Osmond>
ID: <110316757>
Username: <Osmtj001>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
#Will represent assets within the Main Module. These assets can become encrypted, and used by hackers within the main Module or stores in the Rigs
class Asset:

#Allows user to enter assets with a description. Assets by default are not encrypted
    def __init__(self, name:str, description:str):
        self.name = name
        self.description = description
        self.encrypted = False

#Allows user to encrypt assets, print statement will advise user if encryption has been successful, and if asset was already encrypted
    def encrypt(self):

        if self.encrypted == False:
            self.encrypted = True
            print(f'{self.name} Has been encrypted within the Main Module.')

        else:
            print(f'{self.name} Has been already been encrypted within the Main Module.')


#Allows user to decrypt assets. Will advise user if function is successful, or if asset was already decrypted
    def decrypt(self):
        if self.encrypted == True:
            print(f'{self.name} Has been decrypted within the Main Module.')
        else:
            print(f'{self.name} Has been already been decrypted within the Main Module.')

#Returns clean string of asset either encrypted, or with no encryption change
    def __str__(self):
        if self.encrypted == True:
            return f'{self.name}: {self.description} [Encrypted]'
        else:
            return f'{self.name}: {self.description}'

