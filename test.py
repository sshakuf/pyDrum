import pygame

import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

from SoundRect import SoundRect
# Set up Pygame
pygame.init()
win = pygame.display.set_mode((600, 600))

# Creates the button with optional parameters
# button = Button(
#     # Mandatory Parameters
#     win,  # Surface to place button on
#     100,  # X-coordinate of top left corner
#     100,  # Y-coordinate of top left corner
#     300,  # Width
#     150,  # Height

#     # Optional Parameters
#     text='Hello',  # Text to display
#     fontSize=50,  # Size of font
#     margin=20,  # Minimum distance between text/image and edge of button
#     inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
#     hoverColour=(150, 0, 0),  # Colour of button when being hovered over
#     pressedColour=(0, 200, 20),  # Colour of button when being clicked
#     radius=20,  # Radius of border corners (leave empty for not curved)
#     onClick=lambda: print('Click')  # Function to call when clicked on
# )
button = SoundRect(win, (0,0), (100,100,100,100),0,0 )

slider = Slider(win, 100, 300, 400, 40, min=0, max=99, step=1)
output = TextBox(win, 275, 400, 50, 50, fontSize=30)

output.disable()  # Act as label instead of textbox

run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()

    output.setText(slider.getValue())

    win.fill((255, 255, 255))


    pygame_widgets.update(events)  # Call once every loop to allow widgets to render and listen
    pygame.display.update()