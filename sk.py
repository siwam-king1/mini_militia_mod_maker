import re
from colorama import Fore, init

init()

RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
RESET = Fore.RESET

colored_text = f"""{YELLOW}

███████╗██╗██╗    ██╗ █████╗ ███╗   ███╗██╗  ██╗██╗███╗   ██╗ ██████╗  ██╗
██╔════╝██║██║    ██║██╔══██╗████╗ ████║██║ ██╔╝██║████╗  ██║██╔════╝ ███║
███████╗██║██║ █╗ ██║███████║██╔████╔██║█████╔╝ ██║██╔██╗ ██║██║  ███╗╚██║
╚════██║██║██║███╗██║██╔══██║██║╚██╔╝██║██╔═██╗ ██║██║╚██╗██║██║   ██║ ██║
███████║██║╚███╔███╔╝██║  ██║██║ ╚═╝ ██║██║  ██╗██║██║ ╚████║╚██████╔╝ ██║
╚══════╝╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═╝
                                                                          

{GREEN}PRIVATE TOOL BY SIWAMKING{RESET}
"""

print(colored_text)

file_dir = input(f"{YELLOW}Please enter the directory path of the dump file to be processed:{RESET} ")

output_txt_path = input(f"{YELLOW}Please enter the path to save the output text file:{RESET} ")


def extract_keyword(target_string):

    parts = target_string.split("_")
    keyword = parts[-2].lower() + parts[-1]


    return keyword


target_strings = [
    "_ZN20ApplicationInterface16checkQuitEarlyAdEP20QuitAdCheckInterface",
    "_ZN11AppDelegate36applicationDidEnterBackgroundAndroidEPN7cocos2d8CCObjectE",
    "_ZN14PlayerLobbyLAN4initEv",
    "_ZN18GameCustomizeLayer9addPlayerEPN7cocos2d8CCObjectE",
    "_ZN22SoldierLocalController9addDamageEfNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEib",
    "_ZN10IapManager18isProductPurchasedENSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE",
    "_ZN12ItemPurchase15isItemPurchasedENSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE",
    "_ZN22SoldierLocalController8hasPowerEv",
    "_ZN6Weapon16getRoundsPerFireEv",
    "_ZN6Weapon7getAmmoEv",
    "_ZN6Weapon7getClipEv",
    "_ZN6Weapon13getReloadTimeEv",
    "_ZN10MapManager16getGravityFactorEv",
    "_ZN6Weapon11isDualWieldEv",
    "_ZN6Weapon22isDualWieldPrimaryOnlyEv",
    "_ZN10MapManager18addStaticBodyShapeEii",
    "_ZN5Enemy12canSeeTargetEv",
    "_ZN13WeaponFactory12isLaserSightE8ItemType",
    "_ZN14SoldierManager13respawnPlayerEPN7cocos2d8CCObjectE",
    "_ZN14NetworkManager16sendPositionDataEfb",
    "_ZN9Explosion11applyDamageEf",
    "_ZN8GasCloud11applyDamageEf",
    "_ZN10PlasmaBall11applyDamageEf",
    "_ZN17LeaderBoardBridge15calcPlayerSkillEv",
    "_ZN17LeaderBoardBridge20getCachedPlayerSkillEv",
    "_ZN20ApplicationInterface9getOSTypeEv",
    "_ZN6Weapon14getBulletSpeedEv",
    "_ZN22SoldierLocalController10updateStepEf6cpVectS0_f",
    "_ZN6Weapon8getRangeEv",
    "_ZN6Weapon12getZoomScaleEv",
    "_ZN13WeaponFactory23createRandomStartWeaponEv",
    "_ZN14SoldierManager11spawnPlayerEv",
    "_ZN13SurvivalStage9playRoundEf",
    "_ZN14EffectsManager11onExplosionEPN7cocos2d8CCObjectE",
    "_ZN9PROXYNADE14updateItemStepEf",
    "_ZN9ProxyMine10updateItemStepEf",
    "_ZN6Joypad4fireEv",
    "_ZN6Weapon20getRandomFiringAngleEv",
    "_ZN13WeaponManager22getWeaponForSpawnPointEPN7cocos2d12CCDictionaryE",
    "_ZN13WeaponFactory18createRandomWeaponEv",
    "_ZN13WeaponManager14setSpawnPeriodEPN7cocos2d12CCDictionaryEf",
    "_ZN14NetworkManager13isLocalLeaderEv",
    "_ZN18GameCustomizeLayer7addTimeEPN7cocos2d8CCObjectE",
    "_ZN18GameCustomizeLayer7subTimeEPN7cocos2d8CCObjectE",
    "_ZN22SoldierLocalController9throwDualEv",
    "_ZN3HUD9onGrenadeEPN7cocos2d8CCObjectE",
    "_ZN3HUD7onPunchEPN7cocos2d8CCObjectE",
    "_ZN3SAW14updateItemStepEf",
    "_ZN14NetworkManager16sendWeaponChangeEPN7cocos2d8CCObjectE",
    "_ZN17ProjectileManager10addGrenadeE6cpVectfS0_bNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEi",
    "_ZN17ProjectileManager9addRocketE6cpVectfS0_P6WeaponbNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE",
    "_ZN17ProjectileManager6addSawE6cpVectfS0_P6WeaponbNSt6__ndk112basic"
]


try:
    with open(output_txt_path, 'w') as txt_file:
        file_path = file_dir
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    for target_string in target_strings:
                        if target_string in line:
                            hex_numbers = re.findall(r'0x[\da-fA-F]+', line)
                            keyword = extract_keyword(target_string)
                            txt_file.write(f"Function = {target_string}\n")
                            if hex_numbers:
                                txt_file.write("Offset Found:\n")
                                if len(set(hex_numbers)) == 1:
                                    txt_file.write(f"{hex_numbers[0]}\n")
                                else:
                                    for hex_num in hex_numbers:
                                        txt_file.write(f"{hex_num}\n")
                            txt_file.write("\n")
                            break
        except FileNotFoundError:
            print(f"File not found at path: {file_path}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

except FileNotFoundError:
    print(f"Output text file path not found: {output_txt_path}")
except Exception as e:
    print(f"An error occurred while writing to the text file: {str(e)}")
