"""
File: Rig.py
Description: Class code for 'Rig' class for the OOP Basic Programming assignment
Author: Jozef Jones
ID: 110484756
Username: JONJY036
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
import random

# Define class, __init__ and __str__
class Rig:
    def __init__(self, name: str):
        self.__name = name
        self.__damage = 0
        self.__broken = False
        self.__storage = []
        self.__upgrade_level = 0

        data_spike1 = Asset('Data Spike', 'A digital item used in battles')
        data_spike2 = Asset('Data Spike', 'A digital item used in battles')
        removable_drive = Asset('Removable Drive', 'Hardware used to extract assets')

        self.__storage.append(data_spike1)
        self.__storage.append(data_spike2)
        self.__storage.append(removable_drive)

    def __str__(self):
        return (
            f'Name: {self.__name}\n'
            f'Damage: {self.__damage}\n'
            f'Broken: {self.__broken}\n'
            f'Storage: {self.__storage}\n'
            f'Upgrade level: {self.__upgrade_level}\n'
        )

    # Define Getters
    def get_name(self):
        return self.__name
    def get_damage(self):
        return self.__damage
    def get_broken(self):
        return self.__broken
    def get_storage(self):
        return self.__storage
    def get_upgrade_level(self):
        return self.__upgrade_level

    # Define Setters
    def set_damage(self, damage):
        self.__damage = damage
    def set_broken(self, broken):
        self.__broken = broken
    def set_storage(self, storage):
        self.__storage = storage
    def set_upgrade_level(self, upgrade_level):
        self.__upgrade_level = upgrade_level

    # Define Methods
    def repair_rig(self):
        # TBC

    def upgrade_rig(self):
        # TBC

    def generate_asset(self):
        # TBC

    def check_condition(self):
        # TBC