class StationeryStore:

    def __init__(self):
        self.inventory = {}
        self.cart = {}

    def add_item(self, item, quantity, price):
        if item in self.inventory:
            self.inventory[item]['quantity'] += quantity
        else:
            self.inventory[item] = {'quantity': quantity, 'price': price}
        print(f"Added {quantity} {item}(s) to inventory.")

    def display_inventory(self):
        print("\nCurrent Inventory:")
        for item, details in self.inventory.items():
            print(
                f"{item}: Quantity - {details['quantity']}, Price - ${details['price']:.2f}"
            )

    def add_to_cart(self, item, quantity):
        if item in self.inventory:
            if self.inventory[item]['quantity'] >= quantity:
                if item in self.cart:
                    self.cart[item] += quantity
                else:
                    self.cart[item] = quantity
                self.inventory[item]['quantity'] -= quantity
                print(f"Added {quantity} {item}(s) to your cart.")
            else:
                print(f"Error: Not enough {item} in stock.")
        else:
            print(f"Error: {item} not found in inventory.")

    def calculate_total(self):
        total = 0
        for item, quantity in self.cart.items():
            total += self.inventory[item]['price'] * quantity
        return total

    def checkout(self):
        total_cost = self.calculate_total()
        print("\nYour Cart:")
        for item, quantity in self.cart.items():
            print(
                f"{item}: Quantity - {quantity}, Price - ${self.inventory[item]['price']:.2f} each"
            )

        print(f"\nTotal Cost: ${total_cost:.2f}")
        confirm = input(
            "Do you want to proceed to checkout? (yes/no): ").lower()

        if confirm == 'yes':
            print("Thank you for your purchase!")
            self.cart.clear()  # Clear the cart after checkout
        else:
            print("Checkout canceled.")


def main():
    store = StationeryStore()

    # Adding some initial items to the inventory
    store.add_item("Notebook", 10, 2.50)
    store.add_item("Pen", 20, 1.20)
    store.add_item("Pencil", 15, 0.80)
    store.add_item("Eraser", 25, 0.50)

    while True:
        print("\nStationery Store Management System")
        store.display_inventory()

        action = input(
            "What would you like to do? (add to cart/checkout/exit): ").lower(
            )

        if action == 'add to cart':
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            store.add_to_cart(item.lower(), quantity)

        elif action == 'checkout':
            store.checkout()

        elif action == 'exit':
            print("Thank you for visiting the Stationery Store. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
