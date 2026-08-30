# default player data on creation
DEFAULT_PLAYER = {
    "name": "Unknown",
    "class": "Novice",
    "race": "Unknown",
    "level": 1,
    "xp": 1,
    "hp": 100,
    "max_hp": 100,
    "gold": 10,
    "inventory": ["wooden stick"],
    "Equipped items": [],
    "Bar_Name": "None",
    "Bar_Value": 0,
    "resource_val": 0
}

LEVEL_REQUIREMENTS = {
    1: 0,
    2: 100,
    3: 200,
    4: 400,
    5: 650,
    7: 800,
    9: 1000,
    10: 1250
}

CLASS_ABILITIES = {
    "Warrior": [
        ("Over-Head Strike", 1, 1.2, 20),
        ("Primal Rage", 3, 1.5, 40),
        ("Unleash Fury", 5, 2.0, 50)
    ],
    "Mage": [
        ("Spark", 1, 2.0, 15),
        ("Fireball", 3, 2.5, 30),
        ("Thousdand Needles", 5, 3.0, 50),
        ("Nuke", 10, 100.0, 100)
    ],
    "Bard": [
        ("Annoying Melody", 1, 1.5, 15),
        ("Chord of Terror", 3, 1.8, 25),
        ("Heart Attack", 5, 2.5, 35)
    ]
}

CLASS_RESOURCES = {
    "Warrior": {"name": "Rage", "max": 100},
    "Mage": {"name": "Mana", "max": 50},
    "Bard": {"name": "Inspiration", "max": 75}
}

Warrior_Base_health = 150
Mage_Base_health = 75
Bard_Base_health = 100

Human_Mage_Bar_Base_Value = 10

current_damage_multiplier = 1.0

warrior_brace_multiplier = 0.7
mage_brace_multiplier = 0.95
bard_brace_multiplier = 0.8

player_min_damage = 5
player_max_damage = 10

player_data = DEFAULT_PLAYER.copy()

def reset_player():
    global player_data
    player_data = DEFAULT_PLAYER.copy()

def check_level_up():
    while True:
        current_lvl = player_data["level"]
        next_lvl = current_lvl + 1
    
        if next_lvl not in LEVEL_REQUIREMENTS or player_data["xp"] < LEVEL_REQUIREMENTS[next_lvl]:
            break
        
        player_data["level"] += 1
        player_data["max_hp"] += 15
        player_data["hp"] = player_data["max_hp"]  # Heal to full
        
        print("\n" + "=" * 30)
        print(f"!! LEVEL UP !! You are now Level {player_data['level']}!")
        print(f"Your Max HP increased to {player_data['max_hp']}!")

        p_class = player_data["class"]
        new_skills = []
        
        if p_class in CLASS_ABILITIES:
            # Unpacks 4 items to match CLASS_ABILITIES structure
            for skill_name, req_level, mult, cost in CLASS_ABILITIES[p_class]:
                if req_level == player_data["level"]:
                    new_skills.append(skill_name)
        
        if new_skills:
            print("! NEW ABILITY UNLOCKED !")
            for skill in new_skills:
                print(f"  -> {skill}")
                
        print("=" * 30 + "\n")

def get_unlocked_abilities(p_data):
    p_class = p_data.get("class", "Warrior")
    p_level = p_data.get("level", 1)
    
    unlocked = []
    if p_class in CLASS_ABILITIES:
        for ability in CLASS_ABILITIES[p_class]:
            req_level = ability[1]
            if p_level >= req_level:
                unlocked.append(ability) 
                
    return unlocked