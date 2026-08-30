import random
import time
import player

enemy_health = {
    "Lesser Goblin": 50,
    "Angry Beggar": 40,
    "Wolf Pup": 30
}

enemy_min_damage = {
    "Lesser Goblin": 3,
    "Angry Beggar": 7,
    "Wolf Pup": 15
}
enemy_max_damage = {
    "Lesser Goblin": 11,
    "Angry Beggar": 13,
    "Wolf Pup": 50
}

enemy_xp = {
    "Lesser Goblin": 15,
    "Angry Beggar": 20,
    "Wolf Pup": 25
}

current_fightable_enemies = ["Lesser Goblin", "Angry Beggar", "Wolf Pup"]

current_enemy = None
current_enemy_health = 0
current_enemy_damage = 0

def start_combat():
    global current_enemy_health, current_enemy_damage, current_enemy

    current_enemy = random.choice(current_fightable_enemies)
    if current_enemy in enemy_health:
        current_enemy_health = enemy_health[current_enemy]
        current_enemy_damage = random.randint(enemy_min_damage[current_enemy], enemy_max_damage[current_enemy])
        print(f"You stumble upon a {current_enemy} !")
        print(f"Enemy HP: {current_enemy_health}")
        input("\n [Press Enter to continue]")
        return current_enemy
    else:
        print("Unknown enemy. Cannot start combat.")
        return None

def do_combat():
    global current_enemy_health, current_enemy

    while current_enemy_health > 0 and player.player_data["hp"] > 0:
        p_class = player.player_data["class"]
        res_info = player.CLASS_RESOURCES.get(p_class, {"name": "Resource", "max": 100})
        res_name = res_info["name"]
        
        if "resource_val" not in player.player_data:
            player.player_data["resource_val"] = res_info["max"]

        # 1. COMBAT STATUS DISPLAY
        print(f"\n--- COMBAT ---")
        print(f"Your HP: {player.player_data['hp']}")
        print(f"{res_name}: {player.player_data['resource_val']}/{res_info['max']}")
        print(f"Enemy HP: {current_enemy_health}")
        print("----------------")

        # 2. DISPLAY ACTIONS
        print("Choose your action:")
        print("[1] Attack")
        print("[2] Defend")

        unlocked_specials = player.get_unlocked_abilities(player.player_data)
        if unlocked_specials:
            print("Special Abilities:")
            for index, ability in enumerate(unlocked_specials, start=3):
                name, req_lvl, mult, cost = ability
                print(f"[{index}] {name} (Cost: {cost} {res_name} | {mult}x Dmg)")

        action = input("> ").strip()
        action_taken = True

        # 3. HANDLE ACTIONS
        if action == "1":
            damage_dealt = int(random.randint(player.player_min_damage, player.player_max_damage) * player.current_damage_multiplier)
            current_enemy_health -= damage_dealt
            print(f"\nYou dealt {damage_dealt} damage to the enemy!")

        elif action == "2":
            print("\nYou brace yourself for the enemy's attack.")
            player.player_data["brace_multiplier"] = player.player_data.get("brace_multiplier", 1.0)

        elif unlocked_specials and action.isdigit() and 3 <= int(action) < 3 + len(unlocked_specials):
            ability_idx = int(action) - 3
            name, req_lvl, mult, cost = unlocked_specials[ability_idx]

            if player.player_data["resource_val"] >= cost:
                player.player_data["resource_val"] -= cost
                
                base_damage = random.randint(player.player_min_damage, player.player_max_damage)
                total_damage = int(base_damage * mult)
                current_enemy_health -= total_damage
                
                print(f"\nYou used {name}! (-{cost} {res_name})")
                print(f"It dealt {total_damage} damage!")
            else:
                print(f"\nNot enough {res_name}! You need {cost} but only have {player.player_data['resource_val']}.")
                action_taken = False

        else:
            print("\nInvalid action. Please choose again.")
            action_taken = False

        # 4. ENEMY TURN
        if action_taken and current_enemy_health > 0:
            time.sleep(2)
            damage_taken = random.randint(enemy_min_damage[current_enemy], enemy_max_damage[current_enemy])
            player.player_data["hp"] -= damage_taken
            print(f"The enemy attacks you for {damage_taken} damage!")
            time.sleep(1.5)

    # 5. COMBAT RESOLUTION
    if player.player_data["hp"] <= 0:
        print("\nYou have been defeated!")
    elif current_enemy_health <= 0:
        xp_gained = enemy_xp[current_enemy]
        player.player_data["xp"] += xp_gained
        print("\nYou have defeated the enemy!")
        print(f"You gained {xp_gained} XP!")
        player.check_level_up()
        current_enemy = None