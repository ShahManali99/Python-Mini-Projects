# Disney Princess Personality Quiz

princess_traits = {
    "Snow White": 0,
    "Cinderella": 0,
    "Aurora": 0,
    "Ariel": 0,
    "Belle": 0,
    "Jasmine": 0,
    "Mulan": 0,
    "Tiana": 0,
    "Rapunzel": 0,
    "Merida": 0
}

questions = [
    {
        "question": "What's your favorite hobby?",
        "options": {
            "A": ("Singing", ["Snow White", "Ariel", "Rapunzel"]),
            "B": ("Reading", ["Belle"]),
            "C": ("Exploring", ["Jasmine", "Mulan", "Merida"]),
            "D": ("Cooking", ["Tiana"]),
        }
    },
    {
        "question": "What's your ideal adventure?",
        "options": {
            "A": ("Exploring a new kingdom", ["Jasmine", "Rapunzel"]),
            "B": ("Saving your family or people", ["Mulan", "Merida"]),
            "C": ("Finding true love", ["Snow White", "Cinderella", "Aurora", "Ariel"]),
            "D": ("Pursuing your dreams", ["Belle", "Tiana"]),
        }
    },
    {
        "question": "What's your best quality?",
        "options": {
            "A": ("Kindness", ["Snow White", "Cinderella"]),
            "B": ("Intelligence", ["Belle", "Tiana"]),
            "C": ("Bravery", ["Mulan", "Merida"]),
            "D": ("Determination", ["Ariel", "Jasmine", "Rapunzel"]),
        }
    },
    {
        "question": "What's your preferred outfit?",
        "options": {
            "A": ("Elegant gown", ["Cinderella", "Aurora", "Belle"]),
            "B": ("Practical and comfortable", ["Mulan", "Tiana"]),
            "C": ("Exotic and colorful", ["Jasmine", "Rapunzel"]),
            "D": ("Simple and natural", ["Snow White", "Ariel", "Merida"]),
        }
    },
    {
        "question": "What's your ideal pet?",
        "options": {
            "A": ("Bird", ["Snow White", "Cinderella"]),
            "B": ("Horse", ["Mulan", "Merida"]),
            "C": ("Cat", ["Jasmine"]),
            "D": ("Dog", ["Belle", "Rapunzel"]),
        }
    }
]

def ask_question(question):
    print(question["question"])
    for option, (answer, _) in question["options"].items():
        print(f"{option}. {answer}")

    while True:
        choice = input("Enter your choice (A/B/C/D): ").upper()
        if choice in question["options"]:
            return choice
        else:
            print("Invalid choice. Please try again.")

def calculate_result(answers):
    for answer in answers:
        for princess in questions[answers.index(answer)]["options"][answer][1]:
            princess_traits[princess] += 1

    return max(princess_traits, key=princess_traits.get)

def main():
    print("Welcome to the Disney Princess Personality Quiz!")
    print("Answer the following questions to find out which Disney Princess you are most like.")
    print()

    answers = []
    for question in questions:
        answers.append(ask_question(question))
        print()

    result = calculate_result(answers)
    print(f"You are most like {result}!")

if __name__ == "__main__":
    main()