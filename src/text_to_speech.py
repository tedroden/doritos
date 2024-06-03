import os
import hashlib

from gtts import gTTS
from openai import OpenAI
from audio import play_audio_file

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def get_path(text: str):
    return "audio/" + hashlib.md5(text.encode()).hexdigest() + ".mp3"

def google_text_to_speech(text, lang='en'):
    filename = get_path(text)
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save(filename)

    return filename


def openai_text_to_speech(text):
    filename = get_path(text)
    response = client.audio.speech.create(
        model="tts-1",
        voice="shimmer",
        input=text
    )
    response.stream_to_file(filename)
    return filename


def text_to_speech_by_provider(text, provider="openai"):
    filename = None
    if provider == "google":
        filename = google_text_to_speech(text)
    elif provider == "openai":
        filename = openai_text_to_speech(text)
    else:
        raise ValueError(f"Invalid provider: {provider}")
    return filename


def text_to_speech(text, provider="openai"):
    filename = text_to_speech_by_provider(text, provider)
    play_audio_file(filename)
