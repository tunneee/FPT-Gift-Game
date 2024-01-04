# Setup Python ----------------------------------------------- #
import pygame
import sys
import os
from settings import *
from game import Game
from menu import Menu


# Setup pygame/window --------------------------------------------- #
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100, 32)  # windows position
pygame.init()
pygame.display.set_caption(WINDOW_NAME)
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)

mainClock = pygame.time.Clock()

# Fonts ----------------------------------------------------------- #   
fps_font = pygame.font.SysFont("coopbl", 22)

# Music ----------------------------------------------------------- #
# pygame.mixer.music.load("Assets/Sounds/Komiku_-_12_-_Bicycle.mp3")
# pygame.mixer.music.set_volume(MUSIC_VOLUME)
# pygame.mixer.music.play(-1)
# Variables ------------------------------------------------------- #
state = "menu"

# Creation -------------------------------------------------------- #
game = Game(SCREEN)
menu = Menu(SCREEN)


# Functions ------------------------------------------------------ #
def user_events():
    global flag_reset
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_r:
                flag_reset=True
                 

def update():
    global state,flag_reset
    if state == "menu":
        if menu.update() == "game" or flag_reset==True:
            game.reset()  # reset the game to start a new game
            state = "game"
    elif state == "game":
        if game.update() == "menu":
            state = "menu"
        if  flag_reset==True:
            game.reset()
            state = "game"
    pygame.display.update()
    mainClock.tick(FPS)
                

# Loop ------------------------------------------------------------ #
while True:

    flag_reset=False    
    # Buttons ----------------------------------------------------- #
    user_events()

    # Update ------------------------------------------------------ #
    update()

    # FPS
    if DRAW_FPS:
        fps_label = fps_font.render(
            f"FPS: {int(mainClock.get_fps())}", 1, (255, 200, 20))
        SCREEN.blit(fps_label, (5, 5))
