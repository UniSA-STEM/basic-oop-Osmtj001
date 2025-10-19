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
    print('\n' + '=' * 20)
    print(f'{label}')
    print('=' * 20)
    function()

#Test definitions for different scenarios
def test_no_rig():
    h = Hacker('Superman')
    target = Rig('Lex Luther')
    print(h)
    h.attack('Lex Luther')

if __name__ == '__main__':
    normalizerformat(test_no_rig, 'Test without a rig')