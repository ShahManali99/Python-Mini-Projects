import random
import json


def load_questions(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)


def play_trivia(questions):
    score = 0
    total_questions = 0

    for category, q_list in questions.items():
        print(f"\n--- {category.upper()} ---")
        print(q_list)
        random.shuffle(q_list)
        for question in q_list[:3]:  # Ask 3 questions per category
            total_questions += 1
            print(question["question"])
            player_answer = input("Your answer: ")
            if player_answer.lower() == question["answer"].lower():
                print("Correct!")
                score += 1
            else:
                print(f"Sorry, the correct answer is {question['answer']}")

    print(f"\nYour final score is {score} out of {total_questions}")
    return score, total_questions


def main():
    questions = load_questions("trivia_questions.json")

    while True:
        score, total = play_trivia(questions)
        play_again = input("\nDo you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
