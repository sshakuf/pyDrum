import pygame
from pygame import mixer
pygame.init()

WIDTH  = 1400
HEIGHT = 800

black = (0,0,0)
white = (255,255,255)
gray = (128,128,128)
dark_gray = (50,50,50)
green = (0,255,0)
gold = (212, 175, 55)
blue = (0,255,255)



screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Beat Maker")
pygame.font.init()
label_font = pygame.font.Font("Roboto-Bold.ttf",32)
medium_font = pygame.font.Font("Roboto-Bold.ttf",24)

fps = 60
timer = pygame.time.Clock()
beats = 16
instruments = [
    ['hi_hat', 'Hi Hat', 'sounds/hi hat.WAV'],
    ['snare', 'Snare', 'sounds/snare.WAV'],
    ['bass','Bass Drum', 'sounds/kick.WAV'],
    ['crash','Crash', 'sounds/crash.WAV'],
    ['clap','Clap', 'sounds/clap.WAV'],
    ['tom','Floor Tom', 'sounds/tom.WAV'],
]
boxes = []
sounds = []
num_instruments = len(instruments)
clicks = [[-1 for _ in range(beats)] for _ in range(num_instruments)]
bpm = 240

playing = True
active_length = 0
active_beat = 0
beat_changed = True

def draw_grid(clicked, beat): #beat-the beat no that is now played
    left_box = pygame.draw.rect(screen, gray, [0,0,200,HEIGHT-200],5)
    bottom_box = pygame.draw.rect(screen, gray, [0, HEIGHT-200, WIDTH, 200], 5)
    boxes = []
    colors = [gray, white, gray]
    y = 30
    instrument_hieght = (HEIGHT-200) // num_instruments
    for ins in instruments:
        lbl_txt = label_font.render(ins[1], True, white)    
        screen.blit(lbl_txt,(30,y))
        y = y+instrument_hieght


    for i in range(num_instruments):
        pygame.draw.line(screen, gray, [0, (i*instrument_hieght)+instrument_hieght], [200, (i*instrument_hieght)+instrument_hieght], 3)
    for i in range(beats):
        for j in range(num_instruments):
            color = gray
            if clicks[j][i] != -1:
                color = green
            pygame.draw.rect(screen, color, 
                [i*((WIDTH-200) // beats) + 200, (j*instrument_hieght), ((WIDTH-200) // beats), (HEIGHT-200) // num_instruments],0,3)
            pygame.draw.rect(screen, gold, 
                [i*((WIDTH-200) // beats) + 200, (j*instrument_hieght), ((WIDTH-200) // beats), (HEIGHT-200) // num_instruments],5,5)
            rect = pygame.draw.rect(screen, black, 
                [i*((WIDTH-200) // beats) + 200, (j*instrument_hieght), ((WIDTH-200) // beats), (HEIGHT-200) // num_instruments],2,5)
            boxes.append((rect, (i,j)))

            active = pygame.draw.rect(screen, blue, 
            [beat * ((WIDTH-200) // beats ) + 200 ,
             0,
            ((WIDTH-200) // beats),
             num_instruments * instrument_hieght],5,3)

    return boxes


def play_notes():
    for i in range(len(clicks)):
        if clicks[i][active_beat] != -1:
           sounds[i].play() 


def loadSounds():
    sounds = []
    for ins in instruments:
        sounds.append(mixer.Sound(ins[2]))
    return sounds

sounds = loadSounds()
pygame.mixer.set_num_channels(num_instruments * 3)

def drumRun():
    global active_beat
    global playing
    global beat_changed
    global active_length


    run=True
    while run:
        timer.tick(fps)
        screen.fill(black)
        boxes =  draw_grid(clicks, active_beat)

        #lower menu buttons
        play_pause = pygame.draw.rect(screen, gray, [50,HEIGHT - 150, 200, 100] ,0 ,5)
        if playing:
            play_text = label_font.render('Playing', True, green)
        else:
            play_text = label_font.render('Paused', True, dark_gray)
        screen.blit(play_text, (80,HEIGHT - 120))




        if beat_changed:
            play_notes()
            beat_changed = False


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(boxes)):
                    if boxes[i][0].collidepoint(event.pos):
                        coords = boxes[i][1]
                        clicks[coords[1]][coords[0]] *= -1
            if event.type == pygame.MOUSEBUTTONUP:
                if play_pause.collidepoint(event.pos):
                    if playing:
                        playing = False
                    elif not playing:
                        playing = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playing = not playing

        # beat_length = (fps * 60) // bpm
        beat_length = 3600 // bpm

        if playing:
            if active_length < beat_length:
                active_length += 1
            else:
                active_length = 0
                if active_beat < beats -1 :
                    active_beat += 1
                    beat_changed = True
                else:
                    active_beat = 0
                    beat_changed = True
                #go over all the sounds in the clicks and play it




        pygame.display.flip()

    pygame.quit()


def Play(is_playing):
    global playing
    if is_playing:
        playing = True
    else:
        playing = False

        