"""
File: main.py
Description: The main program code for the OOP Basic Programming assignment
Author: Jozef Jones
ID: 110484756
Username: JONJY036
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Hacker import Hacker
from Rig import Rig
from Asset import Asset

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
