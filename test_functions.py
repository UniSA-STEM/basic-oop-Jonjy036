"""
File: test_functions.py
Description: file to define test functions for assessment 1a - Basic Programming.
Author: Jozef Jones
ID: 110484756
Username: JONJY036
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Hacker import Hacker
from Asset import Asset

# Basic early checks on Hacker Instantiation, aquire_rig,
# find_target and launch_data_spike methods.
# Test extraction of assets and validation of empty target inventory.
def basic_test_and_attack():
    hacker1 = Hacker('Joe')
    print(str(hacker1))

    hacker2 = Hacker('j')
    print(str(hacker2))

    hacker1.aquire_rig('Beast')
    hacker2.aquire_rig('Destroyer')

    hacker1.find_target()
    hacker2.find_target()

    hacker1.launch_data_spike()
    hacker1.launch_data_spike()
    hacker1.launch_data_spike()

    print(str(hacker1))
    print(hacker1.get_rig())

def encrypt_decrypt_test_1_hacker():
    hacker = Hacker('Joe')

    hacker.aquire_rig('Beast')
    token1 = Asset('Crypto Token', 'A token used to aquire or repair rigs')
    chip1 = Asset('Security Chip', 'a chip used to encrypt/decrypt assets')
    chip2 = Asset('Security Chip', 'a chip used to encrypt/decrypt assets')
    chip3 = Asset('Security Chip', 'a chip used to encrypt/decrypt assets')

    hacker.get_inventory().append(token1)
    hacker.get_inventory().append(chip1)
    hacker.get_inventory().append(chip2)
    hacker.get_rig().get_storage().append(chip3)

    print(hacker)
    print(hacker.get_rig())

    hacker.encrypt_asset()

    print(hacker)
    print(hacker.get_rig())

    hacker.decrypt_asset()

    print(hacker)
    print(hacker.get_rig())
