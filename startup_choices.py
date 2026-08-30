import random
import player
import enemy
import sys
import time

def charcter_creation():
    while True:
        choice = input("Would you like to begin character creation? (y/n): ").lower().strip()    
        if choice == 'y':
            print("Beginning character creation...")
            break  
        elif choice == 'n':
            print("chud")
            sys.exit()  
        else:
            print("Invalid choice. Please type 'y/n' to continue or exit.")

    name = input("What is your name adventurer? ").strip()
    player.player_data["name"] = name
    print(f'Greetings {name}! Your character build has started.')

    while True:
        print("\nChoose your Race:")
        print("1. Human")
        print("2. Elf")
        print("3. Iksar")
        print("4. Mutated Octopus")
        print("5. Dwarf")
        
        race_choice = input("Enter the number of your selected race: ").strip()

        races = {
            '1': 'Human',
            '2': 'Elf', 
            '3': 'Iksar', 
            '4': 'Mutated Octopus', 
            '5': 'Dwarf'
        }
        
        if race_choice in races:
            selected_race = races[race_choice]
            player.player_data["race"] = selected_race
            
            print(f"\nYou have selected: {selected_race}!")
            time.sleep(1.5)
            break
        else:
            print("Invalid choice. Please select a valid race! (1-5).")

    while True:
        print("\nChoose your class:")
        print("1. Warrior")
        print("2. Mage")
        print("3. Bard")
        
        class_choice = input("Enter the number of your chosen class: ").strip()

        if class_choice == '1':
            player.player_data["class"] = "Warrior"
            player.player_data["hp"] = player.Warrior_Base_health
            player.player_data["max_hp"] = player.Warrior_Base_health
            player.player_data["brace_multiplier"] = player.warrior_brace_multiplier
            print("You are now a Warrior! Use your brute force and anger to overpower your enemies!")
            time.sleep(1.5)
            break
        elif class_choice == '2':
            player.player_data["class"] = "Mage"
            player.player_data["hp"] = player.Mage_Base_health
            player.player_data["max_hp"] = player.Mage_Base_health
            player.player_data["brace_multiplier"] = player.mage_brace_multiplier
            print("You are now a Mage! Use magical spells to deal damage to your enemies!")
            time.sleep(1.5)
            break
        elif class_choice == '3':
            player.player_data["class"] = "Bard"
            player.player_data["hp"] = player.Bard_Base_health
            player.player_data["max_hp"] = player.Bard_Base_health
            player.player_data["brace_multiplier"] = player.bard_brace_multiplier
            print("You are now a Bard! Use your insturment to sing/play songs and defeat those who appose you!")
            time.sleep(1.5)
            break
        else:
            print("Invalid choice. Please select a valid class.")

    # Dynamically look up resource setup from CLASS_RESOURCES
    p_class = player.player_data["class"]
    res_info = player.CLASS_RESOURCES.get(p_class, {"name": "Resource", "max": 100})
    
    player.player_data["Bar_Name"] = res_info["name"]
    base_res = res_info["max"]
    
    # Bonus resource value for Human Mage
    if player.player_data["race"] == "Human" and p_class == "Mage":
        base_res += player.Human_Mage_Bar_Base_Value

    player.player_data["resource_val"] = base_res
    player.player_data["Bar_Value"] = base_res
