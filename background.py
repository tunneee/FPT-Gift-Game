import pygame
import image
from settings import *

class Background:
    def __init__(self):
        self.image = image.load("Assets/background.png", size=(SCREEN_WIDTH, SCREEN_HEIGHT),
                                )


    def draw(self, surface):
        image.draw(surface, self.image, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2), pos_mode="center")

class Background_game:
    def __init__(self):
        self.image = image.load("Assets/background_game.png", size=(SCREEN_WIDTH, SCREEN_HEIGHT),
                                convert="default")


    def draw(self, surface):
        image.draw(surface, self.image, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2), pos_mode="center")

class Background_endgame:
    def __init__(self):
        self.image = image.load("Assets/background_endgame.png", size=(SCREEN_WIDTH, SCREEN_HEIGHT),
                                convert="default")


    def draw(self, surface):
        image.draw(surface, self.image, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2), pos_mode="center")

