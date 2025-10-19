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

#Normalizer to easily format functions upon output at a later stage
def normalizerformat(function, label):
    print('\n' + '=' * 30)
    print(f'{label}')
    print('=' * 30)
    function()
    input('\nPress Enter to continue...')

#Test definitions for different scenarios
def testNoRig():
    h = Hacker('Superman')
    target = Rig('Lex Luther')
    print(h)
    h.attack('Lex Luther')

def testNoDataspike():
    h = Hacker('Superman')
    h.rig = Rig('SuperRig')
    target = Rig('Lex Luther')
    print(h)
    print(h.rig)
    h.attack('Lex Luther')

def testAttack():
    h = Hacker('Superman')
    h.rig = Rig('SuperRig')
    h.rig.storage.append(Asset('Data Spike', 'Used in battles.'))
    target = Rig('Lex Luther')
    print('Before Attack Launched')
    print(h)
    print(target)
    h.attack(target)
    print('After Attack')
    print(h)
    print(target)

def testAttackExtraction():
    h = Hacker('Superman')
    h.rig = Rig('SuperRig')
    h.rig.storage.append(Asset('Data Spike', 'Used in battles.'))
    h.rig.storage.append(Asset('Data Spike', 'Used in battles.'))
    h.rig.storage.append(Asset("Removable Drive", 'Found in rigs and used for extraction.'))
    target = Rig('Lex Luther')
    target.broken = False
    target.storage.append(Asset('CryptoToken', 'Used to acquire or repair rigs.'))
    a = Asset('Kryptonite', 'Supermans biggest weakness')
    a.encrypt = False
    target.storage.append(a)
    print('Before Attack Launched')
    print(h)
    print(target)
    h.attack(target)
    h.attack(target)
    print('After Attack')
    print(h)


#Calls the above functions with the formatting from Normalizer to return a clean output of tests run
if __name__ == '__main__':
    normalizerformat(testNoRig, 'Test without a rig')
    normalizerformat(testNoDataspike, 'Test without a dataspike')
    normalizerformat(testAttack, 'Simulation of full attack')
    normalizerformat(testAttackExtraction, 'Simulation with extraction')