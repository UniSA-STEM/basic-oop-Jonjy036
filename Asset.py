"""
File: Asset.py
Description: Class code for 'Asset' class for the OOP Basic Programming assignment
Author: Jozef Jones
ID: 110484756
Username: JONJY036
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import uuid
# Define class, __init__ and __str__
class Asset:
    def __init__(self, name: str, description: str, encrypted: bool = False):
        unique_id = str(uuid.uuid4()) [:5]      # Unique ID to add to name.
        self.__name = f'{name}-{unique_id}'     # Create a unique asset name to manage lists.
        self.__description = description
        self.__encrypted = encrypted

    def __str__(self):
        if self.__encrypted == True:
            return f'{self.__name}: {self.__description} [Encrypted]'
        else:
            return f'{self.__name}: {self.__description}'

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