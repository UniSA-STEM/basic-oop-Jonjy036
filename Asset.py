"""
File: Asset.py
Description: Class code for 'Asset' class for the OOP Basic Programming assignment
Author: Jozef Jones
ID: 110484756
Username: JONJY036
This is my own work as defined by the University's Academic Misconduct Policy.
"""
# Define class, __init__ and __str__
class Asset:
    def __init__(self, name: str, description: str, encrypted: bool = False):
        self.__name = name
        self.__description = description
        self.__encrypted = encrypted

# Define Getters
    def get_name(self):
        return self.__name
    def get_description(self):
        return self.__description
    def get_encrypted(self):
        return self.__encrypted

# Define Setters
    def set_encrypted(self, encrypted):
        self.__encrypted = encrypted

# Define Methods