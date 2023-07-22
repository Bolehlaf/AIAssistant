from elevenlabs import clone, generate, play, set_api_key, voices
from elevenlabs.api import History
import os
from dotenv import load_dotenv

# Load the variables from .env file
load_dotenv()

set_api_key(os.getenv("ELEVEN_LABS_API_KEY"))
voices = voices()

audio = generate(text="Hello there!", voice=voices[0])

#tts_url = f"https://api.elevenlabs.io/v1/text-to-speech/5rNo0ltEOddbCvMlxHIj/stream"

play(audio)

history = History.from_api()
print(history)