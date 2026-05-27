import re
from nltk.chat.util import Chat, reflections

pairs = [
    [r"(hi|hello|hey)", ["Hello! How can I help you today?", "Hi there! How may I assist you?"]],
    [r"my name is (.*)", ["Hello %1! How can I assist you today?"]],
    [r"(.*) your name\?", ["I am your friendly chatbot!"]],
    [r"how are you\?", ["I'm just a bot, but I'm doing well. How about you?"]],
    [r"tell me a joke", ["Why don't skeletons fight each other? They don't have the guts!"]],
    [r"(.*) (help|assist) (.*)", ["Sure! How can I assist you with %3?"]],
    [r"(bye|exit)", ["Goodbye! Have a great day!", "See you later!"]],
    [r"(.*)", ["I'm sorry, I didn't understand that. Could you rephrase?"]],
]


class Chatbot:
    def __init__(self, pairs):
        self.chat = Chat(pairs, reflections)

    def respond(self, user_input: str) -> str:
        """Return a chatbot response for the given user input."""
        return self.chat.respond(user_input)


def chat_with_bot():
    print("Hello, I am your Chatbot! Type 'exit' to end the conversation.")
    chatbot = Chatbot(pairs)
    while True:
        try:
            user_input = input("You: ")
        except (KeyboardInterrupt, EOFError):
            print("\nChatbot: Goodbye! Have a nice day!")
            break

        if user_input.strip().lower() in {"exit", "bye"}:
            print("Chatbot: Goodbye! Have a nice day!")
            break

        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")


if __name__ == "__main__":
    chat_with_bot()
import re
from nltk.chat.util import Chat, reflections

pairs = [
    [r"(hi|hello|hey)", ["Hello! How can I help you today?", "Hi there! How may I assist you?"]],
    [r"my name is (.*)", ["Hello %1! How can I assist you today?"]],
    [r"(.*) your name\?", ["I am your friendly chatbot!"]],
    [r"how are you\?", ["I'm just a bot, but I'm doing well. How about you?"]],
    [r"tell me a joke", ["Why don't skeletons fight each other? They don't have the guts!"]],
    [r"(.*) (help|assist) (.*)", ["Sure! How can I assist you with %3?"]],
    [r"(bye|exit)", ["Goodbye! Have a great day!", "See you later!"]],
    [r"(.*)", ["I'm sorry, I didn't understand that. Could you rephrase?"]],
]


class Chatbot:
    def __init__(self, pairs):
        self.chat = Chat(pairs, reflections)

    def respond(self, user_input: str) -> str:
        """Return a chatbot response for the given user input."""
        return self.chat.respond(user_input)


def chat_with_bot():
    print("Hello, I am your Chatbot! Type 'exit' to end the conversation.")
    chatbot = Chatbot(pairs)
    while True:
        try:
            user_input = input("You: ")
        except (KeyboardInterrupt, EOFError):
            print("\nChatbot: Goodbye! Have a nice day!")
            break

        if user_input.strip().lower() in {"exit", "bye"}:
            print("Chatbot: Goodbye! Have a nice day!")
            break

        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")


if __name__ == "__main__":
    chat_with_bot() 
    #file to run
    #cmd /c "cd /d "C:\Users\Aleena c b\OneDrive\Desktop\AI Projects" && .venv\Scripts\python .venv\Proj1\Chatbot.py"
