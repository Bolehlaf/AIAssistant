import os
import openai
from dotenv import load_dotenv

# Load the variables from .env file
load_dotenv()

# Set up your API key
openai.api_key = os.getenv("OPENAI_API_KEY")


def ask_chat_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",  # GPT-3.5 engine
        prompt=prompt,
        temperature=0.7,
        max_tokens=150,
        n=1,
        stop=None,
        echo=True
    )
    return response.choices[0].text.strip()


def main():
    print("Hello! I'm your personal assistant. How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Goodbye!")
            break
        response = ask_chat_gpt(user_input)
        print("Assistant:", response)


if __name__ == "__main__":
    main()

