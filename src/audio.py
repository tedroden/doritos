import pygame
import random

# Initialize the mixer module
print("Initializing audio mixer...")
pygame.mixer.init()

def play_audio_file(filename):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()


def play_crunch():
    # play one of seven crunch sounds
    fn = f"crunches/crunch{random.randint(1, 7)}.mp3"
    play_audio_file(fn)
