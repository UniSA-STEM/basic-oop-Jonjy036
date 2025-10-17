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

# Define class, __init__ and __str__.
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

        if len(self.__storage) == 0:
            store_string = 'EMPTY'
        else:
            store_items = []
            for asset in self.__storage:
                store_items.append(str(asset))
            store_string = '\n'.join(store_items)

        return (
            f'*** Rig Info ***\n'
            f'Name: {self.__name}\n'
            f'Damage: {self.__damage}\n'
            f'Broken: {self.__broken}\n'
            f'Storage: \n{store_string}\n'
            f'Upgrade level: {self.__upgrade_level}\n'
        )

    # Define Getters.
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

    # Define Setters.
    def set_damage(self, damage):
        self.__damage = damage
    def set_broken(self, broken):
        self.__broken = broken
    def set_storage(self, storage):
        self.__storage = storage
    def set_upgrade_level(self, upgrade_level):
        self.__upgrade_level = upgrade_level

    # Define repair_rig.
    def repair_rig(self, hacker):
        if hacker.get_rig() is None:
            print('\nNo rig found')
            print('Repair Cancelled')
            print('---------\n')
            return

        # Check if the rig has any damage to be repaired.
        if self.get_damage() == 0:
            print('\nthere is no damage to fix. Happy days!')
            print('repair cancelled')
            print('---------\n')
        else:
            tokens = []
            for asset in hacker.get_inventory():
                if asset.get_name().startswith('Crypto Token'):
                    tokens.append(asset)

            # Check is token exist to perform repair.
            if len(tokens) == 0:
                print('\nyou have no tokens to repair the rig with.')
                print('Repair cancelled')
                print('---------\n')
            else:
                print(f'You have {len(tokens)} tokens to repair the rig with.')
                print(f'Your damage is {self.get_damage()}.')

                # Manual validation to continue repair action.
                repair = input('would you like to use a token to repair your rig? (y/n): ')

                if repair.lower() == 'y' or repair.lower() == 'yes':
                    print('\nYou have chosen to repair your rig!')
                    self.set_damage(0)
                    self.set_broken(False)
                    print(f'\nDamage = {self.get_damage()}.')
                    print(f'Broken = {self.get_broken()}.')
                    print('\nRepair Complete')
                    print('---------\n')

                else:
                    print('\nRepair cancelled')
                    print('---------\n')

    # Define method for asset generation.
    def generate_asset(self, hacker):

        # Validate if rig exists.
        if hacker.get_rig() is None:
            print('\nNo rig found')
            print('Asset generation Cancelled')
            print('---------\n')
            return

        # lists for asset names and asset descriptions.
        asset_names = [
            'Crypto Token',
            'Data Spike',
            'Hardware Patch',
            'Removable Drive',
            'Security Chip'
        ]
        asset_descriptions = [
            'Digital currency used to purchase rigs',
            'A digital item used in battles',
            'A patch used to upgrade rigs',
            'Hardware used to extract assets'
            'a chip used to encrypt/decrypt assets'
        ]

        # Ensure that the correct description is matched with the correct name.
        index = random.randint(0, len(asset_names) - 1)
        asset_name = asset_names[index]
        asset_description = asset_descriptions[index]

        new_asset = Asset(asset_name, asset_description)

        # Define the location the Asset is created in.
        if asset_name in ['Crypto Token', 'Hardware Patch']:
            hacker.get_inventory().append(new_asset)
        else:
            self.get_storage().append(new_asset)


    #def check_condition(self):
        # TBC