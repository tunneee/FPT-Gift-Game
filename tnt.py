import pygame
import random
import image
from settings import *
from present import Present

class Tnt(Present):
    def __init__(self):
        #size
        random_size_value = random.uniform(TNT_SIZE_RANDOMIZE[0], TNT_SIZE_RANDOMIZE[1])
        size = (int(TNT_SIZES[0] * random_size_value), int(TNT_SIZES[1] * random_size_value))
        # moving
        moving_direction, start_pos = self.define_spawn_pos(size)
        # sprite
        self.rect = pygame.Rect(start_pos[0], start_pos[1], size[0]//1.4, size[1]//1.4)
        self.images = [image.load(f"Assets/tnt/1.png", size=size, flip=moving_direction=="right")] # load the images
        self.current_frame = 0
        self.animation_timer = 0
        

    def kill(self, presents): # remove the presents from the list
        presents.remove(self)
        return -TNT_PENALITY
