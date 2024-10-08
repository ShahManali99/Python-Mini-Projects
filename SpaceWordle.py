import random
from collections import Counter

space_words = ["comet", "earth", "venus", "pluto", "stars", "lunar", "orbit", "space", "quark", "nebula", "galaxy"]

def space_wordle():
    secret_word = random.choice(space_words)
    attempts = 6

    print("Welcome to Space Wordle!")
    print(f"Guess the {len(secret_word)}-letter space-related word. You have {attempts} attempts.")

    while True:
        guess = input("Enter your guess: ").lower()

        if len(guess) != len(secret_word):
            print(f"Please enter a {len(secret_word)}-letter word.")
            continue

        if guess == secret_word:
            print(f"Congratulations! You guessed the word: {secret_word}")
            break

        # Count occurrences of each letter in the secret word
        secret_letter_counts = Counter(secret_word)
        result = ['⬛'] * len(secret_word)

        # First pass: Mark correct letters in correct positions
        for i in range(len(secret_word)):
            if guess[i] == secret_word[i]:
                result[i] = '🟩'
                secret_letter_counts[guess[i]] -= 1

        # Second pass: Mark correct letters in wrong positions
        for i in range(len(secret_word)):
            if result[i] == '⬛' and guess[i] in secret_word and secret_letter_counts[guess[i]] > 0:
                result[i] = '🟨'
                secret_letter_counts[guess[i]] -= 1

        print(''.join(result))
        attempts -= 1

        if attempts==0:
            print(f"Sorry, you've run out of attempts. The word was: {secret_word}")
            break

space_wordle()