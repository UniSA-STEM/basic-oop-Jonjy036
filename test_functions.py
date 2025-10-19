"""
File: test_functions.py
Description: file to define test functions for assessment 1a - Basic Programming.
Author: Jozef Jones
ID: 110484756
Username: JONJY036
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Hacker import Hacker
from Asset import Asset

# Basic Hacker method tests.
def basic_test_and_attack():
    hacker1 = Hacker('Joe')
    print(str(hacker1))

    hacker2 = Hacker('j')
    print(str(hacker2))

    hacker1.aquire_rig('Beast')
    hacker2.aquire_rig('Destroyer')

    hacker1.find_target()
    hacker2.find_target()

    hacker1.launch_data_spike()
    hacker1.launch_data_spike()
    hacker1.launch_data_spike()

    print(str(hacker1))
    print(hacker1.get_rig())

    print(str(hacker2))
    print(hacker2.get_rig())

def encrypt_decrypt_test_1_hacker():
    hacker = Hacker('Joe')

    hacker.aquire_rig('Beast')
    token1 = Asset('Crypto Token', 'A token used to aquire or repair rigs')
    chip1 = Asset('Security Chip', 'a chip used to encrypt/decrypt assets')
    chip2 = Asset('Security Chip', 'a chip used to encrypt/decrypt assets')
    chip3 = Asset('Security Chip', 'a chip used to encrypt/decrypt assets')

    hacker.get_inventory().append(token1)
    hacker.get_inventory().append(chip1)
    hacker.get_inventory().append(chip2)
    hacker.get_rig().get_storage().append(chip3)

    print(hacker)
    print(hacker.get_rig())

    hacker.encrypt_asset()

    print(hacker)
    print(hacker.get_rig())

    hacker.decrypt_asset()

    print(hacker)
    print(hacker.get_rig())

def basic_extraction_test():
    hacker = Hacker('Joe')
    hacker.aquire_rig('Beast')

    hacker2 = Hacker('j')
    hacker2.aquire_rig('The Harbinger of Digital Death')

    print(hacker.get_rig())
    print(hacker2.get_rig())

    hacker2.get_rig().set_broken(True)

    hacker.extract_unsecured_assets(hacker2.get_rig())

    print(hacker.get_rig())
    print(hacker2.get_rig())

def decrypt_enemy():
    hacker = Hacker('Joe')
    opponent = Hacker('j')

    hacker.aquire_rig('Beast')
    opponent.aquire_rig('The Harbinger of Digital Death')

    token1 = Asset('Crypto Token', 'A token used to aquire or repair rigs')
    chip1 = Asset('Security Chip', 'A chip used to encrypt/decrypt assets')
    chip2 = Asset('Security Chip', 'A chip used to encrypt/decrypt assets')
    chip3 = Asset('Security Chip', 'A chip used to encrypt/decrypt assets')

    hacker.get_inventory().append(token1)
    hacker.get_inventory().append(chip1)
    hacker.get_inventory().append(chip2)
    hacker.get_rig().get_storage().append(chip3)

    encrypted_asset = Asset('Security Chip', 'a chip used to encrypt/decrypt assets', encrypted=True)
    opponent.get_rig().get_storage().append(encrypted_asset)

    print(hacker)
    print(hacker.get_rig())

    print(opponent)
    print(opponent.get_rig())

    hacker.launch_data_spike()
    hacker.launch_data_spike()

    hacker.decrypt_asset(opponent_rig=opponent.get_rig())

    print(hacker)
    print(hacker.get_rig())

    print(opponent)
    print(opponent.get_rig())

def basic_upgrade_test():
    hacker = Hacker('Joe')
    hacker.aquire_rig('Beast')

    print(hacker.get_rig())

    patch1 = Asset('Hardware Patch', 'A patch used to upgrade rigs')
    patch2 = Asset('Hardware Patch', 'A patch used to upgrade rigs')
    patch3 = Asset('Hardware Patch', 'A patch used to upgrade rigs')
    patch4 = Asset('Hardware Patch', 'A patch used to upgrade rigs')
    patch5 = Asset('Hardware Patch', 'A patch used to upgrade rigs')

    hacker.get_inventory().append(patch1)
    hacker.get_inventory().append(patch2)
    hacker.get_inventory().append(patch3)
    hacker.get_inventory().append(patch4)
    hacker.get_inventory().append(patch5)

    print(hacker.get_rig())

    hacker.upgrade_rig()
    print(hacker.get_rig())

    hacker.upgrade_rig()
    print(hacker.get_rig())

    hacker.upgrade_rig()
    print(hacker.get_rig())

    hacker.upgrade_rig()
    print(hacker.get_rig())

    hacker.upgrade_rig()
    print(hacker.get_rig())

    hacker.get_rig().check_condition()

def basic_store_and_retrieve_test():
    hacker = Hacker('Joe')
    hacker.aquire_rig('Beast')

    print(hacker.get_rig())

    token1 = Asset('Crypto Token', 'A token used to aquire or repair rigs')
    chip1 = Asset('Security Chip', 'a chip used to encrypt/decrypt assets')
    chip2 = Asset('Security Chip', 'a chip used to encrypt/decrypt assets')
    chip3 = Asset('Security Chip', 'a chip used to encrypt/decrypt assets')

    hacker.get_inventory().append(token1)
    hacker.get_inventory().append(chip1)
    hacker.get_inventory().append(chip2)
    hacker.get_rig().get_storage().append(chip3)

    print('Baseline check')
    print('-----------')
    print(hacker)
    print(hacker.get_rig())

    hacker.store_asset(chip1)

    print('after first store. should be successful.')
    print('-----------')
    print(hacker)
    print(hacker.get_rig())

    hacker.store_asset(chip2)

    print('after second store. should be successful.')
    print('-----------')
    print(hacker)
    print(hacker.get_rig())

    hacker.store_asset(token1)
    print('after third store. should fail.')
    print('-----------')

    print(hacker)
    print(hacker.get_rig())

    hacker.retrieve_asset(chip1)

    print('after first retrieve. should be successful.')
    print('-----------')
    print(hacker)
    print(hacker.get_rig())

    hacker.retrieve_asset(token1)

    print('after second retrieve. should fail.')
    print('-----------')
    print(hacker)
    print(hacker.get_rig())

def basic_scan_inventory():
    hacker = Hacker('Joe')

    hacker.aquire_rig('Beast')

    token1 = Asset('Crypto Token', 'A token used to aquire or repair rigs')
    chip1 = Asset('Security Chip', 'A chip used to encrypt/decrypt assets')
    chip2 = Asset('Security Chip', 'A chip used to encrypt/decrypt assets')
    chip3 = Asset('Security Chip', 'A chip used to encrypt/decrypt assets')

    hacker.get_inventory().append(token1)
    hacker.get_inventory().append(chip1)
    hacker.get_inventory().append(chip2)
    hacker.get_rig().get_storage().append(chip3)

    print(hacker)
    print(hacker.get_rig())

    hacker.scan_inventory('Security Chip')

    print(hacker)
    print(hacker.get_rig())

# Basic Rig method tests.
def basic_repair_rig_test():
    hacker = Hacker('Joe')

    hacker.aquire_rig('Beast')

    hacker.get_rig().set_damage(5)
    hacker.get_rig().set_broken(True)

    crypto_token = Asset('Crypto Token', 'Digital currency used to purchase rigs')
    hacker.get_inventory().append(crypto_token)

    print(hacker.get_rig())

    rig = hacker.get_rig()
    rig.repair_rig(hacker)

    print(hacker.get_rig())

def basic_generate_asset_test():
    hacker = Hacker('Joe')
    hacker.aquire_rig('rig1')

    print(hacker)
    print(hacker.get_rig())

    hacker.get_rig().generate_asset(hacker)
    print(hacker)
    print(hacker.get_rig())

def basic_check_condition_test():
    hacker = Hacker('Joe')
    hacker.aquire_rig('Beast')

    print(hacker)
    print(hacker.get_rig())

    print('check1')
    hacker.get_rig().set_damage(7)
    hacker.get_rig().set_upgrade_level(4)

    hacker.get_rig().check_condition()

    print('check2')
    hacker.get_rig().set_damage(2)
    hacker.get_rig().set_upgrade_level(3)

    hacker.get_rig().check_condition()

    print('check3')
    hacker.get_rig().set_damage(10)
    hacker.get_rig().set_upgrade_level(1)

    hacker.get_rig().check_condition()

    print('check4')
    hacker.get_rig().set_damage(1)
    hacker.get_rig().set_upgrade_level(6)

    hacker.get_rig().check_condition()

# Larger test run
def main_test_pogram():
    # Create Hacker 1 and print __str__.
    hacker1 = Hacker('Joe')
    print(hacker1)

    # Create Hacker 1 and print __str__.
    hacker2 = Hacker('j')
    print(hacker2)

    # Both hackers Aquire rigs.
    hacker1.aquire_rig('Beast')
    hacker2.aquire_rig('Destroyer')

    spike1 = Asset('Data Spike', 'A digital item used in battles')
    spike2 = Asset('Data Spike', 'A digital item used in battles')
    spike3 = Asset('Data Spike', 'A digital item used in battles')
    patch1 = Asset('Hardware Patch', 'A patch used to upgrade rigs')
    patch2 = Asset('Hardware Patch', 'A patch used to upgrade rigs')
    patch3 = Asset('Hardware Patch', 'A patch used to upgrade rigs')
    patch4 = Asset('Hardware Patch', 'A patch used to upgrade rigs')
    patch5 = Asset('Hardware Patch', 'A patch used to upgrade rigs')
    patch6 = Asset('Hardware Patch', 'A patch used to upgrade rigs')

    hacker1.get_rig().get_storage().append(spike1)
    hacker1.get_rig().get_storage().append(spike2)
    hacker1.get_rig().get_storage().append(spike3)
    hacker2.get_inventory().append(patch1)
    hacker2.get_inventory().append(patch2)

    # Check hacker2 base level rig info.
    print(hacker2.get_rig())

    # Hacker 1 finds available targets.
    hacker1.find_target()

    # Hacker 1 launches initial strikes.
    hacker1.launch_data_spike()
    hacker1.launch_data_spike()

    # Check hacker 2 rig damage level.
    print(hacker2.get_rig())

    # Upgrade rig and check details.
    hacker2.upgrade_rig()
    hacker2.upgrade_rig()
    print(hacker2.get_rig())

    hacker1.launch_data_spike()
    hacker1.launch_data_spike()

    print(hacker2.get_rig())

    # Try to upgade (Broken Rig).
    hacker2.upgrade_rig()

    # Repair without a token.
    rig = hacker2.get_rig()
    rig.repair_rig(hacker2)
    print(hacker2.get_rig())

    # Add token and repair.
    token1 = Asset('Crypto Token', 'Digital currency used to purchase rigs')
    hacker2.get_inventory().append(token1)

    hacker2.get_inventory().append(patch3)
    hacker2.get_inventory().append(patch4)

    rig = hacker2.get_rig()
    rig.repair_rig(hacker2)
    print(hacker2.get_rig())

    # Increase to max upgrade level. (not enough patches)
    hacker2.upgrade_rig()
    hacker2.upgrade_rig()
    hacker2.upgrade_rig()
    print(hacker2.get_rig())

    hacker2.get_inventory().append(patch5)
    hacker2.get_inventory().append(patch6)

    # Increase to max upgrade level
    hacker2.upgrade_rig()
    print(hacker2.get_rig())

    # Launch Attack while exposed.
    hacker1.launch_data_spike()
    print(hacker1)

    hacker1.trace_reduction()

    hacker1.launch_data_spike()
    print(hacker2.get_rig())
    hacker2.upgrade_rig()

    # Attempt to upgrade beyond limit.
    hacker2.upgrade_rig()
    print(hacker2.get_rig())

    print(hacker2)
    print(hacker2.get_rig())
