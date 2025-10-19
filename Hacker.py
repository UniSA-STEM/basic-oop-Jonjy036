"""
File: Hacker.py
Description: Class code for 'Hacker' class for the OOP Basic Programming assignment
Author: Jozef Jones
ID: 110484756
Username: JONJY036
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
from Rig import Rig


# Define class, __init__ and __str__.
class Hacker:
    EXPOSED = 5
    hacker_list = []

    def __init__(self, name: str):
        self.__name = name
        self.__inventory = []
        self.__rig = None
        self.__trace_level = 0
        self.__exposed_status = False
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
                inv_items.append(str(asset))
            inv_string = '\n'.join(inv_items)

        return (
            f'\n*** Hacker Info ***\n'
            f'Hacker: {self.__name}\n'
            f'Rig: {rig_name}\n'
            f'Trace level: {self.__trace_level}\n'
            f'Inventory: \n{inv_string}\n'
        )

    # Define Getters.
    def get_name(self):
        return self.__name

    def get_inventory(self):
        return self.__inventory

    def get_rig(self):
        return self.__rig

    def get_trace_level(self):
        return self.__trace_level

    def get_exposed_status(self):
        return self.__exposed_status

    # Define Setters.
    def set_rig(self, rig):
        self.__rig = rig

    def set_trace_level(self, trace_level: int):
        self.__trace_level = trace_level
        if self.__trace_level >= Hacker.EXPOSED:
            self.__exposed_status = True
        else:
            self.__exposed_status = False

    # Allows the hacker to purchase a rig at the expense of 1 crypto token.
    def aquire_rig(self, name):
        token_in_inventory = False
        asset_to_remove = None

        # Search for any assets in inventory with 'Crypto Token' in the name.
        for asset in self.__inventory:
            if asset.get_name().startswith('Crypto Token'):
                token_in_inventory = True
                asset_to_remove = asset

        # If token found, name the rig and remove token, otherwise print error message.
        if token_in_inventory:
            new_rig = Rig(name)
            self.set_rig(new_rig)
            self.__inventory.remove(asset_to_remove)
            print(f'You now own a Rig! The rig is called: {name}\n')
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

        current_trace_level = self.get_trace_level()
        if current_trace_level >= Hacker.EXPOSED:
            print('You are Exposed. You cannot launch an attack!')
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
            print('You cannot launch an attack')
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

        # If target exists, launch attack and remove data spike.
        if target_hacker:
            data_spike_for_attack = data_spikes[0]
            print(f'Launching Data Spike attack against {target_hacker.get_name()}\n')
            self.__rig.get_storage().remove(data_spike_for_attack)

            # If target has no rig, display message. If rig does exist, apply damage.
            target_rig = target_hacker.get_rig()
            if target_rig is None:
                print(f'{target_hacker.get_name()} has no rig!! you wasted a Data Spike!!!!')
            else:
                spike_damage = 6

                target_upgrade_level = target_rig.get_upgrade_level()
                damage_reduction = target_upgrade_level * 1  # Reduction level 1 per level between 0 an 5.

                if damage_reduction >= spike_damage:
                    reduced_damage = 0  # Cannot have negative damage.
                elif damage_reduction == 0:
                    reduced_damage = spike_damage
                else:
                    reduced_damage = spike_damage - damage_reduction

                new_damage = target_rig.get_damage() + reduced_damage
                target_rig.set_damage(new_damage)

                print(f'{target_hacker.get_name()} was hit and {reduced_damage} damage was caused.')
                print('-------\n')

                new_trace_level = self.get_trace_level() + 1
                self.set_trace_level(new_trace_level)
                if new_trace_level >= Hacker.EXPOSED:
                    print('You have now been exposed. you can no longer launch attacks!')
                    print('-------\n')
                    return

                # Check to see if rig is 'broken'.
                target_rig.broken_status_check()

                if target_rig.get_broken():
                    print(f'{target_hacker.get_name()} now has a broken rig!!!')
                    print('*******\n')

                    self.extract_unsecured_assets(target_rig)

        # If no target exists by the input name display message.
        else:
            print(f' there is no hacker by the name of {target_name}\n')

    def extract_unsecured_assets(self, broken_rig):
        current_trace_level = self.get_trace_level()
        if current_trace_level >= Hacker.EXPOSED:
            print('You have been exposed. you cannot complete extraction')
            return

        if not broken_rig.get_broken():
            print('This rig is not broken. You cannot extract assets!!')
            print('-------\n')
            return

        # Search rig storage for removable drive.
        removable_drives = []
        for asset in self.get_rig().get_storage():
            if asset.get_name().startswith('Removable Drive'):
                removable_drives.append(asset)

        if not removable_drives:
            print('You have no removable drives in the rig storage')
            print('-------\n')
            return
        else:
            print(f'You have {len(removable_drives)} removable drives in the rig storage')
            print('-------\n')

        # Start attack phase of the method.
        print('COMMENCING ATTACK!!!')
        print('-------')
        print('-------')

        # Create list of viable targets.
        unsecured_assets = []
        for asset in broken_rig.get_storage():
            if not asset.get_encrypted():
                unsecured_assets.append(asset)

        # If viable targets, extract to own storage. If none, extraction fails.
        if len(unsecured_assets) > 0:
            own_rig_storage = self.get_rig().get_storage()
            own_rig_capacity = self.get_rig().get_storage_capacity()

            extracted_count = 0
            for asset in unsecured_assets:
                if len(own_rig_storage) < own_rig_capacity:
                    broken_rig.get_storage().remove(asset)
                    self.get_rig().get_storage().append(asset)
                    extracted_count += 1
                else:
                    print('Rig Storage full. You cannot extract any more items.')

            if extracted_count > 0:
                print(f'\n{self.get_name()}, You have successfully extracted {len(unsecured_assets)}!!\n')
            else:
                print('There were no unsecured assets. You leave with nothing!')
        new_trace_level = self.get_trace_level() + 1
        if new_trace_level >= Hacker.EXPOSED:
            print('You have now been exposed.')
            print('-------\n')

    # Define Encryption method.
    def encrypt_asset(self):
        # Check for Security Chips and where they are located.
        chips_in_inv = []
        for asset in self.get_inventory():
            if asset.get_name().startswith('Security Chip'):
                chips_in_inv.append(asset)

        chips_in_rig = []
        if self.get_rig() is not None:
            for asset in self.get_rig().get_storage():
                if asset.get_name().startswith('Security Chip'):
                    chips_in_rig.append(asset)

        # If no chips exist, encryption method ends.
        if len(chips_in_rig) == 0 and len(chips_in_inv) == 0:
            print(f'You have no Security Chips in either your inventory or rig storage!')
            return

        # If chip/s exists, select where to use them from.
        # Chips exist in both Rig Storage and Hacker Inventory.
        if len(chips_in_inv) > 0 and len(chips_in_rig) > 0:
            print('you have Security Chips in your inventory and rig storage!')
            location = input('Which location would you like to use? (inv/sto): ')
            if location.lower() == 'inv' or location.lower() == 'sto':
                use_from_location = location.lower()
            else:
                print('Invalid selection. Encryption cancelled!')
                return

        # Chips only exist in Inventory.
        elif len(chips_in_inv) > 0:
            choice = input('Security chip found in your inventory only. use this? (y/n): ')
            if choice.lower() == 'y' or choice.lower() == 'yes':
                use_from_location = 'inv'
            else:
                print('Invalid selection. Encryption cancelled!')
                return

        # Chips only exist in Rig Storage.
        else:
            choice = input('Security chip found in your storage only. use this? (y/n): ')
            if choice.lower() == 'y' or choice.lower() == 'yes':
                use_from_location = 'sto'
            else:
                print('Invalid selection. Encryption cancelled!')
                return

        # Chip location defines where it can be used. inv->inv or storage->storage.
        if use_from_location == 'inv':
            target_location = self.get_inventory()
        else:
            target_location = self.get_rig().get_storage()

        # List of unsecured assets in location.
        unsecured_assets = []
        for asset in target_location:
            if not asset.get_encrypted():
                unsecured_assets.append(asset)

        # Display unsecured assets (if any).
        if len(unsecured_assets) == 0:
            print('You have no unsecured assets in the chosen location.')
            return
        else:
            print(f'here are the unsecured assets from {use_from_location}:')
            for asset in unsecured_assets:
                print(f'- {asset.get_name()}')

            # Select which asset to secure.
            asset_to_encrypt = input('please enter the UUID suffix of the asset to encrypt: ')

            selected_asset = None
            if len(asset_to_encrypt) != 5:
                print('invalid UUID. Encryption Cancelled!!')
            else:
                for asset in unsecured_assets:
                    if asset_to_encrypt in asset.get_name():
                        selected_asset = asset

                if selected_asset is not None:
                    selected_asset.set_encrypted(True)
                    print(f'You have encrypted {selected_asset.get_name()}!')
                else:
                    print('No matching UUID found. Encryption cancelled!')

    # Define the decrypt_asset method.
    def decrypt_asset(self, opponent_rig=None):
        # Check for Security Chips and where they are located.
        chips_in_inv = []
        for asset in self.get_inventory():
            if asset.get_name().startswith('Security Chip'):
                chips_in_inv.append(asset)

        chips_in_rig = []
        if self.get_rig() is not None:
            for asset in self.get_rig().get_storage():
                if asset.get_name().startswith('Security Chip'):
                    chips_in_rig.append(asset)

        # If no chips exist, Decryption method ends.
        if len(chips_in_rig) == 0 and len(chips_in_inv) == 0:
            print(f'You have no Security Chips in either your inventory or rig storage!')
            return

        # If chip/s exists, select where to use them from.
        # Chips exist in both Rig Storage and Hacker Inventory.
        if len(chips_in_inv) > 0 and len(chips_in_rig) > 0:
            print('you have Security Chips in your inventory and rig storage!')
            location = input('Which location would you like to use? (inv/sto): ')
            if location.lower() == 'inv' or location.lower() == 'sto':
                use_from_location = location.lower()
            else:
                print('Invalid selection. Decryption cancelled!')
                return

        # Chips only exist in Inventory.
        elif len(chips_in_inv) > 0:
            choice = input('Security chip found in your inventory only. use this? (y/n): ')
            if choice.lower() == 'y' or choice.lower() == 'yes':
                use_from_location = 'inv'
            else:
                print('Invalid selection. Decryption cancelled!')
                return

        # Chips only exist in Rig Storage.
        else:
            choice = input('Security chip found in your storage only. use this? (y/n): ')
            if choice.lower() == 'y' or choice.lower() == 'yes':
                use_from_location = 'sto'
            else:
                print('Invalid selection. Decryption cancelled!')
                return

        # Chip location defines where it can be used. inv->inv or storage->storage.
        if use_from_location == 'inv':
            target_location = self.get_inventory()
        else:
            target_location = self.get_rig().get_storage()

        # Identification of hacker opponent.
        opponent_owner = None
        for hacker in Hacker.hacker_list:
            if opponent_rig is not None and hacker.get_rig() == opponent_rig:
                opponent_owner = hacker

        # List of secured assets in location.
        my_secured_assets = []
        for asset in target_location:
            if asset.get_encrypted():
                my_secured_assets.append(('self', asset))

        # List of secure assets in opponent's rig.
        opponent_secured_assets = []
        if opponent_rig and opponent_rig.get_broken():
            if opponent_owner is not None:
                for asset in opponent_rig.get_storage():
                    if asset.get_encrypted():
                        opponent_secured_assets.append((opponent_owner, asset))
            else:

                # If opponent not found, fallback option.
                for asset in opponent_rig.get_storage():
                    if asset.get_encrypted():
                        opponent_secured_assets.append(('opponent', asset))

        # Combine lists of secure assets.
        all_secured_assets = []
        for item in my_secured_assets:
            all_secured_assets.append(item)
        for item in opponent_secured_assets:
            all_secured_assets.append(item)

        if len(all_secured_assets) == 0:
            print('No encrypted assets to decrypt!')
            return
        else:
            print('Here are the secured assets available for decryption:')
            for owner, asset in all_secured_assets:
                if isinstance(owner, str):
                    owner_name = owner
                else:
                    owner_name = owner.get_name()
                print(f'- {asset.get_name()} (Owner: {owner_name})')

        # Select which asset to decrypt.
        asset_to_decrypt = input('please enter the UUID suffix of the asset to decrypt: ')

        selected_asset = None
        if len(asset_to_decrypt) != 5:
            print('invalid UUID. Encryption Cancelled!!')
            print('---------/n')
            return
        else:
            for owner, asset in all_secured_assets:
                if asset_to_decrypt in asset.get_name():
                    selected_asset = asset

            if selected_asset is not None:
                selected_asset.set_encrypted(False)
                print(f'You have decrypted {selected_asset.get_name()}!')
            else:
                print('No matching UUID found. Decryption cancelled!')

    # Define the upgrade_rig method.
    def upgrade_rig(self):
        max_level = 5

        # Validation check for rig existence.
        if self.get_rig() is None:
            print('You have no rig to upgrade!')
            print('-------\n')
            return

        if self.get_rig().get_upgrade_level() >= max_level:
            self.get_rig().set_upgrade_level(max_level)
            print('\nYou are at MAX LEVEL!!')
            print('You cannot upgrade you rig any further.\n')
            return

        if self.get_rig().get_broken() is True:
            print('\nYour Rig is Broken!\n')
            print('You cannot upgrade while broken!')
            print('-------\n')
            return

        # Check for hardware patches.
        hardware_patches = []
        for asset in self.get_inventory():
            if asset.get_name().startswith('Hardware Patch'):
                hardware_patches.append(asset)

        if not hardware_patches:
            print('You have no Hardware Patches in your inventory!')
            print('-------\n')
            return
        else:
            # If hardware patch exists, check if user wants to continue upgrade.
            print(f'You have {len(hardware_patches)} Hardware Patches in your inventory!')
            use_patch = input('Would you like to use one? (y/n): ')
            if use_patch.lower() == 'y' or use_patch.lower() == 'yes':
                patch_to_use = hardware_patches[0]
                self.get_inventory().remove(patch_to_use)

                # Increase rig level by 1 per upgrade.
                current_level = self.get_rig().get_upgrade_level()
                current_level += 1
                self.get_rig().set_upgrade_level(current_level)

                print(f'Your rig has now been upgraded. the new level is: {current_level}')
                print('-------\n')
            else:
                print('Upgrade cancelled.)')
                print('-------\n')

    # Define the scan_inventory method. Parameter is asset name (Security Chip/Crypto Token/Hardware Patch).
    def scan_inventory(self, asset_name):
        # Validation check for existence of named asset.
        found = []
        for asset in self.get_inventory():
            if asset_name in asset.get_name():
                found.append(asset)

        if len(found) == 0:
            print('No matching assets found in inventory!')
            return

        # Print list of matching assets.
        print('Here are the assets matching your search:')
        for asset in found:
            print(f'- {asset.get_name()}')

        # Check to see if the user wants to remove an asset. Remove selected asset.
        want_to_remove = input('Would you like to remove an asset? (y/n): ')
        if want_to_remove.lower() == 'y' or want_to_remove.lower() == 'yes':
            asset_to_delete = input('Please enter the UUID of the asset to delete: ')
            if len(asset_to_delete) == 5:
                selected_asset = None
                for asset in found:
                    if asset_to_delete in asset.get_name():
                        selected_asset = asset
                if selected_asset is not None:
                    self.get_inventory().remove(selected_asset)
                    print(f'You have removed {selected_asset.get_name()} from your inventory!')
                else:
                    print('No matching UUID found. Deletion cancelled!')
            else:
                print('Invalid UUID length. Deletion cancelled!')
        else:
            print('Deletion cancelled!')

    # Define store_asset method. Asset transfers from inventory to rig storage.
    def store_asset(self, asset_to_store: Asset):

        # Validation check for rig existence.
        if self.get_rig() is None:
            print('You have no rig to store assets in!')
            return

        inv = self.get_inventory()
        sto = self.get_rig().get_storage()

        # Check inventory for any assets matching parameter. (It can only be Security Chips).
        if asset_to_store not in inv:
            print('No matching assets found in inventory!')
            return

        # Check storage capacity.
        if len(sto) >= self.get_rig().get_storage_capacity():
            print('Your storage is full. You cannot store any more assets!!')
            return

        if not asset_to_store.get_name().startswith('Security Chip'):
            print('you can only transfer Security chips!')
            print('Store action Cancelled!')
            print('-------\n')
            return

        inv.remove(asset_to_store)
        sto.append(asset_to_store)

    # Define retieve asset. Same logic, opposite direction to 'store_asset'.
    def retrieve_asset(self, asset_to_retrieve: Asset):
        if self.get_rig() is None:
            print('You have no rig to retrieve assets from!')
            return

        inv = self.get_inventory()
        sto = self.get_rig().get_storage()

        if asset_to_retrieve not in sto:
            print('No matching assets found in storage!')
            return

        if not asset_to_retrieve.get_name().startswith('Security Chip'):
            print('you can only transfer Security chips!')
            print('Retrieve action Cancelled!')
            print('-------\n')
            return

        sto.remove(asset_to_retrieve)
        inv.append(asset_to_retrieve)

    def trace_reduction(self):
        if self.get_trace_level() > 0:
            print(f'\nYou have a trace level of {self.get_trace_level()}!')
            print('Reducing now\n')
            self.set_trace_level(self.get_trace_level() - 1)
            print(f'Your new trace level is {self.get_trace_level()}!\n')
