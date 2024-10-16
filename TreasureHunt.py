def start_game():
    inventory = []
    current_room = 'entrance'

    def show_inventory():
        if inventory:
            print("Your inventory:", ", ".join(inventory))
        else:
            print("Your inventory is empty.")

    while True:
        if current_room == 'entrance':
            print("\nYou are at the entrance of a mysterious land.")
            print("Where do you want to go? (forest/cave/meadow)")
            show_inventory()
            choice = input("> ").lower()
            if choice == 'forest':
                current_room = 'forest'
            elif choice == 'cave':
                current_room = 'cave'
            elif choice == 'meadow':
                current_room = 'meadow'
            else:
                print("Invalid choice.")

        elif current_room == 'forest':
            print("\nYou are in a dark, misty forest.")
            if 'lantern' not in inventory:
                print("You find an old lantern on the ground.")
                print("Do you want to take it? (yes/no)")
                choice = input("> ").lower()
                if choice == 'yes':
                    inventory.append('lantern')
                    print("You picked up the lantern.")
            print("Go back to entrance? (yes/no)")
            choice = input("> ").lower()
            if choice == 'yes':
                current_room = 'entrance'

        elif current_room == 'cave':
            print("\nYou are at the mouth of a dark cave.")
            if 'lantern' in inventory:
                print("Your lantern illuminates a path deeper into the cave.")
                print("Do you want to enter deeper? (yes/no)")
                choice = input("> ").lower()
                if choice == 'yes':
                    current_room = 'deep_cave'
                elif choice == 'no':
                    print("Go back to entrance? (yes/no)")
                    choice = input("> ").lower()
                    if choice == 'yes':
                        current_room = 'entrance'
            else:
                print("It's too dark to enter. You need a light source.")
                print("Go back to entrance? (yes/no)")
                choice = input("> ").lower()
                if choice == 'yes':
                    current_room = 'entrance'

        elif current_room == 'deep_cave':
            print("\nYou are deep in the cave. You see a locked chest.")
            if 'key' in inventory:
                print("Do you want to open the chest? (yes/no)")
                choice = input("> ").lower()
                if choice == 'yes':
                    print(
                        "Congratulations! You found the treasure and won the game!"
                    )
                    break
            else:
                print("You need a key to open this chest.")
            print("Go back to cave entrance? (yes/no)")
            choice = input("> ").lower()
            if choice == 'yes':
                current_room = 'cave'

        elif current_room == 'meadow':
            print("\nYou are in a beautiful meadow with colorful flowers.")
            if 'key' not in inventory:
                print("You spot a golden key hidden among the flowers.")
                print("Do you want to take it? (yes/no)")
                choice = input("> ").lower()
                if choice == 'yes':
                    inventory.append('key')
                    print("You picked up the key.")
            print("Go back to entrance? (yes/no)")
            choice = input("> ").lower()
            if choice == 'yes':
                current_room = 'entrance'


start_game()
