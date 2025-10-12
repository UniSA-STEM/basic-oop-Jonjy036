"""
File: Hacker.py
Description: Class code for 'Hacker' class for the OOP Basic Programming assignment
Author: Jozef Jones
ID: 110484756
Username: JONJY036
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
import random

# Define class, __init__ and __str__
class Hacker:
    hacker_list = []

    def __init__(self, name: str):
        self.__name = name
        self.__inventory = []
        self.__rig = None
        self.__trace_level = 0
        Hacker.hacker_list.append(self)

        crypto_token = Asset('Crypto Token', 'Digital currency used to purchase rigs')

        self.__inventory.append(crypto_token)

    def __str__(self):
        return (
            f'Hacker: {self.__name}'
            f'Rig: {self.__rig.name}'
            f'Trace level: {self.__trace_level}'
            f'Inventory: {self.__inventory}'
        )

    # Define Getters
    def get_name(self):
        return self.__name
    def get_inventory(self):
        return self.__inventory
    def get_rig(self):
        return self.__rig
    def get_trace_level(self):
        return self.__trace_level

    # Define Setters
    def set_rig(self, rig):
        self.__rig = rig
    def set_trace_level(self, trace_level: int):
        self.__trace_level = trace_level

    # Define Methods
    def aquire_rig(self):
        # TBC

    def launch_data_spike(self, target):
        # TBC

    @classmethod
    def find_target(cls):
        # TBC

    def extract_unsecured_assets(self, rig):
        # TBC

    def encrypt_asset(self):
        # TBC

    def decrypt_asset(self):
        # TBC

    def upgrade_rig(self):
        # TBC

    def scan_inventory(self):
        # TBC

    def store_asset(self, rig_name, asset):
        # TBC

    def retrieve_asset(self, rig_name, asset):
        # TBC

