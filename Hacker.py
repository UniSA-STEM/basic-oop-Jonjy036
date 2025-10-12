"""
File: Hacker.py
Description: Class code for 'Hacker' class for the OOP Basic Programming assignment
Author: Jozef Jones
ID: 110484756
Username: JONJY036
This is my own work as defined by the University's Academic Misconduct Policy.
"""
# Define class, __init__ and __str__
class Hacker:
    def __init__(self, name: str):
        self.__name = name
        self.__inventory = []
        self.__crypto_token = 1
        self.__rig = None
        self.__trace_level = 0

# Define Getters
    def get_name(self):
        return self.__name
    def get_inventory(self):
        return self.__inventory
    def get_crypto_token(self):
        return self.__crypto_token
    def get_rig(self):
        return self.__rig
    def get_trace_level(self):
        return self.__trace_level

# Define Setters
    def set_crypto_token(self, crypto_token: int):
        self.__crypto_token = crypto_token
    def set_rig(self, rig):
        self.__rig = rig
    def set_trace_level(self, trace_level: int):
        self.__trace_level = trace_level

# Define Methods