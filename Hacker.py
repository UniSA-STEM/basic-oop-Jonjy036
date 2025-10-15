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

from Rig import Rig


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
        if self.__rig is None:
            rig_name = 'No Rig'
        else:
            rig_name = self.__rig.get_name()

        if len(self.__inventory) == 0:
            inv_string = 'EMPTY'
        else:
            inv_items = []
            for asset in self.__inventory:
                inv_items.append(asset.get_name())
            inv_string = ', '.join(inv_items)

        return (
            f'\nHacker: {self.__name}\n'
            f'Rig: {rig_name}\n'
            f'Trace level: {self.__trace_level}\n'
            f'Inventory: {inv_string}\n'
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

    # Allows the hacker to purchase a rig at the expense of 1 crypto token.
    def aquire_rig(self):
        token_in_inventory = False
        asset_to_remove = None

        # Search for any assets in inventory with 'Crypto Token' in the name.
        for asset in self.__inventory:
            if asset.get_name().startswith('Crypto Token'):
                token_in_inventory = True
                asset_to_remove = asset

        # If token found, name the rig and remove token, otherwise print error message
        if token_in_inventory:
            rig_name = input('Enter a name for your new Rig: ')
            new_rig = Rig(rig_name)
            self.set_rig(new_rig)
            self.__inventory.remove(asset_to_remove)
            print(f'You now own a Rig! The rig is called: {rig_name}\n')
        else:
            print('you have no crypto tokens. You cannot purchase a rig!\n')

    # Identify any other active hackers.
    def find_target(self):
        print('Available Hackers to attack are:')
        for hacker in Hacker.hacker_list:
            if hacker != self:
                print(hacker.get_name())
        print('-------\n')

    # Launch data Spike attack.
    def launch_data_spike(self):
        # Validate that a rig is present.
        if self.get_rig() is None:
            print('You have no rig to launch an attack')
            print('-------\n')
            return

        # Search rig storage for data spikes.
        data_spikes = []
        for asset in self.get_rig().get_storage():
            if asset.get_name().startswith('Data Spike'):
                data_spikes.append(asset)

        # Display message showing number (or absence) of data spikes.
        if not data_spikes:
            print('You have no data spikes in the rig storage')
            print('-------\n')
            return
        else:
            print(f'You have {len(data_spikes)} data spikes in the rig storage')
            print('-------\n')

        # Request target name.
        target_name = input('Enter a target name to launch Data Spike attack at: \n')

        # Validation of target input.
        target_hacker = None
        for hacker in Hacker.hacker_list:
            if hacker.get_name() == target_name and hacker != self:
                target_hacker = hacker

        # if target exists, launch attack and remove data spike.
        if target_hacker:
            data_spike_for_attack = data_spikes[0]
            print(f'Launching Data Spike attack against{target_hacker.get_name()}\n')
            self.__rig.get_storage().remove(data_spike_for_attack)

            # If target has no rig display message. If rig does exist, apply damage.
            target_rig = target_hacker.get_rig()
            if target_rig is None:
                print(f'{target_hacker.get_name()} has no rig!! you wasted a Data Spike!!!!')
            else:
                spike_damage = 1
                new_damage = target_rig.get_damage() + spike_damage
                target_rig.set_damage(new_damage)
                print(f'{target_hacker.get_name()} was hit and {spike_damage} damage was caused.\n')
                print('-------\n')

                # check to see if rig is 'broken'
                if new_damage >= 2:
                    target_rig.set_broken(True)
                    print(f'{target_hacker.get_name()} now has a broken rig!!!')
                    print('*******\n')

        # If no target exists by the input name display message.
        else:
            print(f' there is no hacker by the name of {target_name}\n')

    def extract_unsecured_assets(self, broken_rig):
        if not broken_rig.get_broken():
            print('This rig is not broken. You cannot extract assets!!')
            return

        unsecured_assets = []
        for asset in broken_rig.get_storage():
            if not asset.get_encrypted():
                unsecured_assets.append(asset)

        if len(unsecured_assets) > 0:
            for asset in unsecured_assets:
                broken_rig.get_storage().remove(asset)
                self.get_rig().get_storage().append(asset)
            print(f'\n{self.get_name()}, You have successfully extracted {len(unsecured_assets)}!!\n')

    def encrypt_asset(self):

# def decrypt_asset(self):
# TBC

# def upgrade_rig(self):
# TBC

# def scan_inventory(self):
# TBC

# def store_asset(self, rig_name, asset):
# TBC

# def retrieve_asset(self, rig_name, asset):
# TBC
