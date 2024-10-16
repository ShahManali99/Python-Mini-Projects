import time

menu_prices = {
    "apple pie": 15,
    "mac and cheese": 20,
    "cookies": 23,
    "cake": 30,
    "muffins": 12,
    "super secret recipe": 101,
    "naan and paneer": 10,
    "pasta": 27,
    "boom! (magic world adventure)": 50
}


def display_menu():
  print("\n===== MENU =====")
  for item, price in menu_prices.items():
    print(f"{item.title():<30} ${price:>5}")
  print("=================\n")


def bake(food):
  print(f"\nPreparing {food}...")
  time.sleep(2)  # Simulate cooking time
  print("Cooking in progress...")
  time.sleep(2)
  print("Adding final touches...")
  time.sleep(1)
  print(f"Your {food} is ready!")
  return f"Enjoy your delicious {food}!"


def magic_world_adventure():
  print("\nWelcome to the Magic World!")
  while True:
    print("\nWhat would you like to do in the Magic World?")
    print("1. Ride a dragon")
    print("2. Cast a spell")
    print("3. Meet magical creatures")
    print("4. Drink mermaid water (to exit)")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
      print("You're soaring through the skies on a majestic dragon!")
    elif choice == '2':
      spell = input("What spell would you like to cast? ")
      print(f"You cast {spell}. Magical sparks fly everywhere!")
    elif choice == '3':
      print("You encounter unicorns, phoenixes, and talking trees!")
    elif choice == '4':
      print("You drink the mermaid water and return to the restaurant.")
      break
    else:
      print("Invalid choice. Please try again.")


def main():
  total_bill = 0
  order = []

  while True:
    display_menu()
    food = input(
        "What would you like to order? (or 'done' to finish): ").lower()

    if food.lower() == 'done':
      break

    if food not in menu_prices:
      print("Sorry, that item is not on the menu. Please try again.")
      continue

    if food == "boom! (magic world adventure)":
      magic_world_adventure()
    else:
      print(bake(food))

    order.append(food)
    total_bill += menu_prices[food]

  if order:
    print("\n===== Your Order =====")
    for item in order:
      print(f"{item:<30} ${menu_prices[item]:>5}")
    print(f"\nTotal Bill: ${total_bill}")
    print("Thank you for visiting us!")
  else:
    print("No items ordered. Have a great day!")


if __name__ == "__main__":
  main()
