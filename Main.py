"""
File: main.py
Description: The main program code for the OOP Basic Programming assignment
Author: Jozef Jones
ID: 110484756
Username: JONJY036
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Hacker import Hacker
#from Rig import Rig
#from Asset import Asset

# Basic early checks on Hacker Instantiation, aquire_rig,
# find_target and launch_data_spike methods.

hacker1 = Hacker('Joe')
print(str(hacker1))

hacker2 = Hacker('j')
print(str(hacker2))

hacker1.aquire_rig()
hacker2.aquire_rig()

hacker1.find_target()
hacker2.find_target()

hacker1.launch_data_spike()
hacker1.launch_data_spike()
hacker1.launch_data_spike()

print(str(hacker1))
print(hacker1.get_rig())

