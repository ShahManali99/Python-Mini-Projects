# used to generate permutations of the input letters.
import itertools

# Sample list of valid words (you can expand this)
valid_words = {"cat", "bat", "rat", "tab", "cab", "act", "tac", "arc", "car", "bar", "art"}

# This function generates all possible permutations of the given letters.
# It uses itertools.permutations to create combinations of different lengths (from 1 to the length of the input).
def get_combinations(letters):
    combinations = set()
    for i in range(1, len(letters) + 1):
        for combo in itertools.permutations(letters, i):
            word = ''.join(combo)
            combinations.add(word)
    return combinations

def find_valid_words(combinations):
    return {word for word in combinations if word in valid_words}

def main():
    print("Welcome to the Word Combination Game!")
    letters = input("Enter a combination of letters: ").lower()

    # Get all possible combinations
    combinations = get_combinations(letters)

    # Find valid words
    found_words = find_valid_words(combinations)

    if found_words:
        print("You formed the following valid words:")
        for word in found_words:
            print(f"- {word}")
    else:
        print("No valid words could be formed from those letters.")

if __name__ == "__main__":
    main()