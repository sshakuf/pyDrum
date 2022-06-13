import pygame



WIDTH  = 1400
HEIGHT = 800

black = (0,0,0)
white = (255,255,255)
gray = (128,128,128)
dark_gray = (50,50,50)
green = (0,255,0)
dark_green = (0,155,0)
gold = (212, 175, 55)
blue = (0,255,255)

pygame.font.init()
label_font = pygame.font.Font("Roboto-Bold.ttf",32)
medium_font = pygame.font.Font("Roboto-Bold.ttf",24)

fps = 60
timer = pygame.time.Clock()
beats = 8
instruments = [
    ['hi_hat', 'Hi Hat', 'sounds/hi hat.WAV'],
    ['snare', 'Snare', 'sounds/snare.WAV'],
    ['bass','Bass Drum', 'sounds/kick.WAV'],
    ['crash','Crash', 'sounds/crash.WAV'],
    ['clap','Clap', 'sounds/clap.WAV'],
    ['tom','Floor Tom', 'sounds/tom.WAV'],
]
boxes = []
boxesEffects = []
sounds = []
num_instruments = len(instruments)
clicks = [[0 for _ in range(beats)] for _ in range(num_instruments)]
clicksEffects = [[0 for _ in range(beats)] for _ in range(num_instruments)]
bpm = 240

playing = True
active_length = 0
active_beat = 0
beat_changed = True
