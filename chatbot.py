import random

class Chatbot:
    def __init__(self):
        self.user_name = ""
        self.context = {}

    def greet(self):
        print("Hello! I'm ChatBot. What's your name?")
        self.user_name = input("You: ")
        print(f"Nice to meet you, {self.user_name}! How can I assist you today?")

    def get_response(self, user_input):
        user_input = user_input.lower()

        # Greetings
        greetings = ["hello", "hi", "hey", "howdy"]
        if any(word in user_input for word in greetings):
            return random.choice([
                f"Hello {self.user_name}! How can I help you?",
                f"Hi there {self.user_name}! What's on your mind?",
                f"Hey {self.user_name}! What would you like to chat about?"
            ])

        # How are you
        if "how are you" in user_input:
            return random.choice([
                "I'm just a bunch of code, but thanks for asking! How about you?",
                "I'm doing great! How's your day going?",
                "All systems operational! How are you feeling today?"
            ])

        # What is your name
        if "what is your name" in user_input:
            return f"I'm called ChatBot. And you're {self.user_name}, right?"

        # What can you do
        if "what can you do" in user_input:
            return "I can chat with you, answer questions, and even help with some tasks. Try asking me about the weather or news!"

        # Weather (simulated API call)
        if "weather" in user_input:
            return self.get_weather()

        # News (simulated API call)
        if "news" in user_input:
            return self.get_news()

        # Remember context
        if "remember" in user_input:
            key = input("What should I remember? Enter a key: ")
            value = input("Enter the value to remember: ")
            self.context[key] = value
            return f"Okay, I'll remember that {key} is {value}."

        # Recall context
        if "recall" in user_input:
            key = input("What should I recall? Enter a key: ")
            if key in self.context:
                return f"I remember that {key} is {self.context[key]}."
            else:
                return f"I'm sorry, I don't have any information about {key}."

        # Default response
        return random.choice([
            "I'm not sure I understand. Can you rephrase that?",
            "That's an interesting question. Can you tell me more?",
            "I'm still learning about that. Can you ask me something else?"
        ])

    def get_weather(self):
        return "It's sunny and 72°F (22°C) today. Perfect weather for a chat!"

    def get_news(self):
        return "The top news today: 'Local Dog Wins Award for Being Extra Fluffy'"

def main():
    chatbot = Chatbot()
    chatbot.greet()

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'exit', 'quit']:
            print("ChatBot: Goodbye! Have a great day!")
            break
        response = chatbot.get_response(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    main()