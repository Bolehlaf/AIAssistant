import speech_recognition as sr
import openai

# Set up your OpenAI API credentials
openai.api_key = 'YOUR_API_KEY'

# Function to recognize speech from audio
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand."
    except sr.RequestError:
        return "Sorry, I couldn't access the speech recognition service."

# Function to interact with OpenAI API
def ask_openai(question):
    response = openai.Completion.create(
        engine='davinci',
        prompt=question,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
        timeout=10
    )
    return response.choices[0].text.strip()

# Main loop for the personal assistant
def main():
    print("Personal Assistant is ready.")
    while True:
        user_input = recognize_speech()
        print("You: ", user_input)
        if user_input.lower() == 'exit':
            break
        response = ask_openai(user_input)
        print("Assistant: ", response)

# Run the personal assistant
if __name__ == '__main__':
    main()
