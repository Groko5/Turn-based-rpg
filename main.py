import sys
import player
import enemy
import startup_choices
import events

def start_menu():
    while True:
        print("\n=== WELCOME TO *MUD NAME HERE* ===")
        print("1. Start New Game")
        print("2. Load Game")
        print("3. Exit")

        choice = input("\nSelect an option (1/2/3): ").strip()
        if choice == '1':
            player.reset_player()
            print("Starting a new game...")
            startup_choices.charcter_creation()
            return True
        elif choice == '2':
            print("Attempting to load game...")
            return True
        elif choice == '3':
            print("chud")
            sys.exit()

           

#basic commands to be run through the whole game
def get_input(prompt):
    
    while True:
        user_choice = input(prompt).lower().strip()
        
        if user_choice == 'help':
            print("=== COMMAND LIST ===")
            print(" 'help': Show this menu")
            print(" 'quit': Exit the game")
            print(" 'y' / 'n': Confirm choices\n")
            continue  
        
        elif user_choice in ['quit', 'exit']:
            print("chud")
            sys.exit()
            
        return user_choice

if __name__ == "__main__":
    game_active = start_menu()

    while game_active:
        if player.player_data["hp"] <= 0:
            print("You have no health left. Game over.")
            break

        enemy.start_combat()
        enemy.do_combat()

        if player.player_data["hp"] <= 0:
            print("You have been defeated in combat. Game over.")
            sys.exit()
        
        cont = input("\nWould you like to search for another enemy? (y/n): ").strip().lower()
        if cont != 'y':
            print("Thanks for playing!")
            break







