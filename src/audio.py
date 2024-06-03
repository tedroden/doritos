import pygame
# Initialize the mixer module
print("Initializing audio mixer...")
pygame.mixer.init()

def play_audio_file(filename):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
