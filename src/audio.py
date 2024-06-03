import os
import random

# Hide the pygame support prompt
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame


# Initialize the mixer module
print("🔉 Initializing audio mixer...")
pygame.mixer.init()

def play_audio_file(filename):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()


def play_crunch():
    # play one of seven crunch sounds
    fn = f"crunches/crunch{random.randint(1, 7)}.mp3"
    print(f"🗣️ Crunching {fn}")
    play_audio_file(fn)
