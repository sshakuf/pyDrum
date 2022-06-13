import pygame

import pygame_widgets
from pygame_widgets.button import Button

from common import *
from enum import Enum

class SoundRect:

    def __init__(self, screen, index, rect, state = False, onClickedCallback = None, **kwargs):
        # index - (index, instrument) , rect -bounds for the button rect,  state - true/false
        self.index = index
        self.rect = rect
        self.state = False
        self.screen = screen
        self.onClickedCallback = onClickedCallback

        self.x, self.y, self.width, self.height = rect

        color = gray
        hovercolor = dark_gray
        if self.state:
            color = green
            hovercolor = dark_green

        # Creates the button with optional parameters
        self.button = Button(
            # Mandatory Parameters
            self.screen,  # Surface to place button on
            self.x,  # X-coordinate of top left corner
            self.y,  # Y-coordinate of top left corner
            self.width,  # Width
            self.height,  # Height

            # Optional Parameters
            # text='Hello',  # Text to display
            # fontSize=50,  # Size of font
            # margin=20,  # Minimum distance between text/image and edge of button
            # inactiveColour=color,  # Colour of button when not being interacted with
            # hoverColour=hovercolor,  # Colour of button when being hovered over
            # pressedColour=(0, 200, 20),  # Colour of button when being clicked
            # radius=5,  # Radius of border corners (leave empty for not curved)
            onClick=lambda: self.clickedSound(),  # Function to call when clicked on
            # onClick=lambda: print('Click')  # Function to call when clicked on
            **kwargs
        )

    def update(self):
        color = gray
        hovercolor = dark_gray
        if self.state:
            color = green
            hovercolor = dark_green

        self.button.setInactiveColour (color)
        self.button.setHoverColour (hovercolor)

        

    def clickedSound(self):
        self.state = not self.state
        self.update()
        # self.button.setInactiveColour ((255,255,100))
        # self.button.setPressedColour((0,0,0))
        print('clicked')
        if self.onClickedCallback != None:
            self.onClickedCallback(self)


    

