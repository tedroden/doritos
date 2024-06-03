import os
from datetime import datetime # for log file
import speech_recognition as sr # for speech recognition

from provider import send_to_openai
from text_to_speech import text_to_speech
# Initialize recognizer
recognizer = sr.Recognizer()

from audio import play_crunch

# Define the wake word/phrase
WAKE_WORD = os.environ.get('WAKE_WORD', "doritos")

def log_transcription(transcription: str):
    # log a file with transction-$date.txt, include the transcription
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    filename = f"transcripts/{datetime.now().strftime('%Y-%m-%d')}.txt"
    with open(filename, "a") as file:
        s = f"{timestamp}|{transcription}"
        print(f"📓 Logged: {s}")
        file.write(s + "\n")

def get_transcription(audio: sr.AudioData) -> str:
    try:
        # Recognize the audio
        transcription = recognizer.recognize_google(audio).lower()
        log_transcription(transcription)
        return transcription

    except sr.UnknownValueError:
        # Handle unrecognized speech
        print("🙉 Could not understand audio (ignoring)")
    except sr.RequestError as e:
        # Handle API request errors
        print(f"Could not request results from Google Speech Recognition; {e}")

def contains_wake_word(transcription: str) -> bool:
    return WAKE_WORD in transcription


def queue_say(text: str):
    pass
    # print("queue_say:", text)

def handle_command(transcription: str):
    # Handle the command
    parts = transcription.split(WAKE_WORD)

    # Everything after the first wake word is the command
    command = "".join(parts[1:]).strip()

    print("💬 Sending:", command)
    play_crunch()
    response = send_to_openai(command, queue_say)
    print("💭 received:", response)
    text_to_speech(response)



def listen_for_wake_word():
    with sr.Microphone() as source:

        # Do this forever!
        while True:

            # Adjust for ambient noise and record audio
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

            # Recognize the audio
            transcription = get_transcription(audio)

            # We may not have a transcription if it errors in
            #`get_transcription`, if that happens, no need to
            #worry. We'll just keep listening.
            if transcription and \
               contains_wake_word(transcription):
                handle_command(transcription)


if __name__ == "__main__":
    # Make the directories we need in order to save the audio and transcripts
    paths = ["transcripts", "audio"]
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)

    # Play a sound to let them know we're awake.
    play_crunch()
    print(f"🚀 Ready and listening for {WAKE_WORD}")

    # Start listening
    listen_for_wake_word()
