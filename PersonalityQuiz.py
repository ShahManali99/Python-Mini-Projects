# Simple Personality Quiz

print("Welcome to personality quiz!")
ans = []
option = "Choose an option (1,2,3,4?)"
questions = [
    "How do you prefer to spend your free time?",
    "How do you feel about social gatherings?",
    "Do you prefer to be alone or be in groups?",
    " How do you recharge after a busy day?"
]
options = [
    "1. Reading a Book \n 2. Hanging out with friends \n 3. Going to a party \n 4. Engaging in a hobby\n",
    "1. I prefer to stay home \n 2. I enjoy small gatherings \n 3. I like big parties \n 4. I love meeting new people! \n",
    "1. I prefer working alone \n 2. I like working in small teams \n 3. I enjoy collaborating with large teams \n 4. I like leading group projects \n",
    "1. Spending time alone \n 2. Talking with friends \n 3. Participating in activites \n 4. Going outside for a walk \n"
]

for i in range(len(questions)):
    while True:
        try:
            choice = int(
                input(
                    f"Question {i+1}: {questions[i]}\n {options[i]} {option}"))
            if 1 <= choice <= 4:
                ans.append(choice)
                break
            else:
                print("Invalid choice. Please select a number between 1 and 4")
        except ValueError:
            print("Invalid input. Please enter a number.")

final = sum(ans)

if final <= 5:
    print(
        "You are an introvert! You are more comfortable in focusing on your own inner thoughts and ideas, rather than what's happening around you. You are also especially good at noticing other peoples introverted qualities as well!"
    )

elif final <= 10:
    print(
        "You are an ambivert! You are a person who has features of both an introvert and an extrovert in their personality. Ambiverts are sometimes also called outgoing or social introverts and typically enjoy other people, but also need time alone."
    )

else:
    print(
        "You are an extrovert! You tend to be very talkative, sociable, active, and warm. You thrive in social settings and are energized by the external world and social interactions."
    )
