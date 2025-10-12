"""
File: Rig.py
Description: Class code for 'Rig' class for the OOP Basic Programming assignment
Author: Jozef Jones
ID: 110484756
Username: JONJY036
This is my own work as defined by the University's Academic Misconduct Policy.
"""
# Define class, __init__ and __str__
class Rig:
    def __init__(self, name: str):
        self.__name = name
        self.__damage = 0
        self.__broken = False
        self.__storage = []
        self.__data_spike = 2
        self.__removable_drive = 1
        self.__upgrade_level = 0

# Define Getters
    def get_name(self):
        return self.__name
    def get_damage(self):
        return self.__damage
    def get_broken(self):
        return self.__broken
    def get_storage(self):
        return self.__storage
    def get_data_spike(self):
        return self.__data_spike
    def get_removable_drive(self):
        return self.__removable_drive
    def get_upgrade_level(self):
        return self.__upgrade_level

# Define Setters
    def set_damage(self, damage):
        self.__damage = damage
    def set_broken(self, broken):
        self.__broken = broken
    def set_storage(self, storage):
        self.__storage = storage
    def set_data_spike(self, data_spike):
        self.__data_spike = data_spike
    def set_removable_drive(self, removable_drive):
        self.__removable_drive = removable_drive
    def set_upgrade_level(self, upgrade_level):
        self.__upgrade_level = upgrade_level

# Define Methods