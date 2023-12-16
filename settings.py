import pygame

WINDOW_NAME = "Săn quà cùng FPT UNIVERSITY DA NANG"
# GAME_TITLE = "Present"

SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080


FPS = 30
DRAW_FPS = True

# sizes
BUTTONS_SIZES = (250, 80)
HAND_SIZE = 200
HAND_HITBOX_SIZE = (60, 80)
PRESENTS_SIZES = (50, 38)
# for each new mosquito, it will multiply the size with an random value beteewn X and Y

PRESENT_SIZE_RANDOMIZE = (1, 2)
TNT_SIZES = (50, 50)
TNT_SIZE_RANDOMIZE = (1, 2)

# drawing
DRAW_HITBOX = False  # will draw all the hitbox

# animation
ANIMATION_SPEED = 0.05  # the frame of the insects will change every X sec

# difficulty
GAME_DURATION = 40  # the game will last X sec
PRESENTS_SPAWN_TIME = 1
PRESENTS_MOVE_SPEED = {"min": 7, "max": 10}
# will remove X of the score of the player (if he kills a bee)
TNT_PENALITY = 2

# colors
COLORS = {"title": (199,0,0), "score": (218,165,32), "timer": (218,165,32),
          "buttons": {"default": (56, 67, 209), "second":  (87, 99, 255),
                      "text": (255, 255, 255), "shadow": (46, 54, 163)}}  # second is the color when the mouse is on the button

# sounds / music
MUSIC_VOLUME = 0.16  # value between 0 and 1
SOUNDS_VOLUME = 1

# fonts
pygame.font.init()
FONTS = {}
FONTS["small"] = pygame.font.Font(None, 40)
FONTS["medium"] = pygame.font.Font(None, 72)
FONTS["big"] = pygame.font.Font(None, 120)
