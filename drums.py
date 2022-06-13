import pygame
from pygame import mixer
from common import *
from SoundRect import SoundRect
import pygame_widgets

pygame.init()

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Beat Maker")
pygame.font.init()

def build_grid(clicked, beat): #beat-the beat no that is now played

    boxes = []
    boxesEffects = []

    instrument_hieght = (HEIGHT-200) // num_instruments
    ins_width = (WIDTH-200) // beats
    effct_height = instrument_hieght/4

    padding = 2

    for i in range(beats):
        for j in range(num_instruments):
            pos = (i*(ins_width) + 200+padding, (j*instrument_hieght) + padding, (ins_width)-padding, instrument_hieght-effct_height - padding)
            rect = SoundRect(screen, (i,j), pos, clicks[j][i], ClickedSound,
            borderColour= gold,
            borderThickness=3,
            radius=5
            )

            # pygame.draw.rect(screen, color, pos, 0, 3)
            # pygame.draw.rect(screen, gold, pos, 5, 5)
            # rect = pygame.draw.rect(screen, black, pos, 2, 5)
            boxes.append((rect, (i,j)))

            color = gray
            if clicksEffects[j][i] != 0:
                color = green
            pos = [i*(ins_width) + 200 + padding, (j*instrument_hieght)+instrument_hieght - effct_height +padding, (ins_width) - padding, effct_height - padding]
            effect = SoundRect(screen, (i,j), pos, clicks[j][i], ClickedEffect,
            borderColour= gold,
            borderThickness=3,
            radius=5
            )
            # pygame.draw.rect(screen, color, pos, 0, 3)
            # pygame.draw.rect(screen, gold, pos, 5, 5)
            # effect = pygame.draw.rect(screen, black, pos, 2, 5)
            boxesEffects.append((effect, (i,j)))
    
    return (boxes, boxesEffects)


def draw_grid(clicked, beat): #beat-the beat no that is now played
    left_box = pygame.draw.rect(screen, gray, [0,0,200,HEIGHT-200],5)
    bottom_box = pygame.draw.rect(screen, gray, [0, HEIGHT-200, WIDTH, 200], 5)
    colors = [gray, white, gray]
    y = 30

    instrument_hieght = (HEIGHT-200) // num_instruments
    ins_width = (WIDTH-200) // beats
    effct_height = instrument_hieght/4

    for ins in instruments:
        lbl_txt = label_font.render(ins[1], True, white)    
        screen.blit(lbl_txt,(30,y))
        y = y+instrument_hieght

    for i in range(num_instruments):
        pygame.draw.line(screen, gray, [0, (i*instrument_hieght)+instrument_hieght], [200, (i*instrument_hieght)+instrument_hieght], 3)

    active = pygame.draw.rect(screen, blue, 
    [beat * (ins_width ) + 200 , 0, (ins_width), num_instruments * instrument_hieght],5,3)

def ClickedSound(soundRect):
    coords = soundRect.index
    if clicks[coords[1]][coords[0]] == 0:
        clicks[coords[1]][coords[0]] = 1
    else:
        clicks[coords[1]][coords[0]] = 0

def ClickedEffect(soundRect):
    coords = soundRect.index
    if clicksEffects[coords[1]][coords[0]] == 0:
        clicksEffects[coords[1]][coords[0]] = 1
    else:
        clicksEffects[coords[1]][coords[0]] = 0

def play_notes():
    for i in range(len(clicks)):
        if clicks[i][active_beat] != 0:
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
    global boxes
    global boxesEffects

    # screen.fill(black)
    # boxes, boxesEffects =  draw_grid(clicks, active_beat)
    boxes, boxesEffects = build_grid(clicks, active_beat)

    run=True
    while run:
        timer.tick(fps)
        screen.fill(black)

        # draw_grid(clicks, active_beat)

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
            # if event.type == pygame.MOUSEBUTTONDOWN:
                # for i in range(len(boxes)):
                    # if boxes[i][0].collidepoint(event.pos):
                    #     coords = boxes[i][1]
                    #     if clicks[coords[1]][coords[0]] == 0:
                    #         clicks[coords[1]][coords[0]] = 1
                    #     else:
                    #         clicks[coords[1]][coords[0]] = 0
                        
                    # if boxesEffects[i][0].collidepoint(event.pos):
                    #     coords = boxes[i][1]
                    #     if clicksEffects[coords[1]][coords[0]] == 0:
                    #         clicksEffects[coords[1]][coords[0]] = 1
                    #     else:
                    #         clicksEffects[coords[1]][coords[0]] = 0




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


        pygame_widgets.update(event)  # Call once every loop to allow widgets to render and listen

        draw_grid(clicks, active_beat)

        pygame.display.flip()
    pygame.quit()


def Play(is_playing):
    global playing
    if is_playing:
        playing = True
    else:
        playing = False

