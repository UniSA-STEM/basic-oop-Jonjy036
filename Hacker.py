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
        self.__rig = None
        self.__trace_level = 0

# Define Getters
    def get_name(self) -> str:
        return self.__name
    def get_inventory(self) -> list:
        return self.__inventory
    def get_rig(self) -> list:
        return self.__rig
    def get_trace_level(self) -> int:
        return self.__trace_level

# Define Setters
    def set_rig(self, rig):
        self.__rig = rig
    def set_trace_level(self, trace_level):
        self.__trace_level = trace_level

# Define Methods