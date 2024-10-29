import random
import time

# Create the deck
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
values = [
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King',
    'Ace'
]
deck = [f"{value} of {suit}" for suit in suits for value in values]
print(deck)


def deal_cards(num_cards):
    return [
        deck.pop(random.randint(0,
                                len(deck) - 1)) for _ in range(num_cards)
    ]


def calculate_hand_value(hand):
    total = 0
    for card in hand:
        value = card.split()[0]
        if value in ['Jack', 'Queen', 'King']:
            total += 10
        elif value == 'Ace':
            total += 11 if total + 11 <= 21 else 1
        else:
            total += int(value)
    return total


def play_game():
    print("Welcome to Manali's Card Game!")
    time.sleep(1)

    player_hand = deal_cards(2)
    computer_hand = deal_cards(2)

    print("\nYour hand:", ', '.join(player_hand))
    time.sleep(1)

    # Allow player to exchange cards
    exchange = input("Do you want to exchange any cards? (yes/no): ").lower()
    if exchange == 'yes':
        num_exchange = int(
            input("How many cards do you want to exchange? (1 or 2): "))
        for _ in range(num_exchange):
            player_hand.pop()
            player_hand.append(deck.pop(random.randint(0, len(deck) - 1)))
        print("Your new hand:", ', '.join(player_hand))
        time.sleep(1)

    # Betting
    bet = int(input("\nHow much do you want to bet? $"))
    time.sleep(1)

    print("\nDealer's hand:", computer_hand[0], "and a hidden card")
    time.sleep(1)

    player_total = calculate_hand_value(player_hand)
    computer_total = calculate_hand_value(computer_hand)

    print(f"\nYour hand value: {player_total}")
    time.sleep(1)
    print(f"Dealer's hand value: {computer_total}")
    time.sleep(1)

    if player_total > computer_total:
        print(f"\nCongratulations! You win ${bet}!")
    elif player_total < computer_total:
        print(f"\nSorry, you lose ${bet}.")
    else:
        print("\nIt's a tie!")

    time.sleep(1)
    print("\nThanks for playing!")


play_game()
