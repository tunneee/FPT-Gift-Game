import pygame
import time
import random
from settings import *
from background import Background_game,Background_endgame
from hand import Hand
from hand_tracking import HandTracking
from present import Present
from tnt import Tnt
import cv2
import ui

class Game:
    def __init__(self, surface):
        self.surface = surface
        self.background = Background_game()
        self.background_endgame = Background_endgame()
        # Load camera
        self.cap = cv2.VideoCapture(1)

        self.high_score = 0

        self.sounds = {}
        self.sounds["slap"] = pygame.mixer.Sound(f"Assets/Sounds/slap.mp3")
        self.sounds["slap"].set_volume(SOUNDS_VOLUME)
        self.sounds["screaming"] = pygame.mixer.Sound(f"Assets/Sounds/screaming.wav")
        self.sounds["screaming"].set_volume(SOUNDS_VOLUME)
        self.sounds["tnt"] = pygame.mixer.Sound(f"Assets/Sounds/tnt.mp3")
        self.sounds["tnt"].set_volume(SOUNDS_VOLUME)


    def reset(self): # reset all the needed variables
        self.hand_tracking = HandTracking()
        self.hand = Hand()
        self.insects = []
        self.insects_spawn_timer = 0
        self.score = 0
        self.game_start_time = time.time()


    def spawn_insects(self):
        
        t = time.time()
        if t > self.insects_spawn_timer:
            self.insects_spawn_timer = t + PRESENTS_SPAWN_TIME

            # increase the probability that the insect will be a tnt over time
            nb = (GAME_DURATION-self.time_left)/GAME_DURATION * 150 / 2   # increase from 0 to 50 during all  the game (linear)
            if random.randint(-5, 60) < nb:
                self.insects.append(Tnt())
            else:
                self.insects.append(Present())
            
            if self.time_left < (GAME_DURATION/3)*2:
                self.insects.append(Present())

    def load_camera(self):
        _, self.frame = self.cap.read()

        height, width, _ = self.frame.shape

        # Define the zoom factor (e.g., 2x)
        zoom_factor = 1

        # Calculate the new dimensions for the zoomed frame
        new_height = int(height / zoom_factor)
        new_width = int(width / zoom_factor)

        # Calculate the top-left corner coordinates for the ROI
        start_row = int((height - new_height) / zoom_factor)
        start_col = int((width - new_width) / zoom_factor)

        # Crop the frame to create the zoom effect
        zoomed_frame = self.frame[start_row:start_row + new_height, start_col:start_col + new_width]

        self.frame = zoomed_frame
 

    def set_hand_position(self):
        self.frame = self.hand_tracking.scan_hands(self.frame)
        (x, y) = self.hand_tracking.get_hand_center()
        self.hand.rect.center = (x, y)
    
    def draw_endgame(self):
        self.background_endgame.draw(self.surface)

    def draw(self):
        # draw the background
        self.background.draw(self.surface)
        # draw the insects
        for insect in self.insects:
            insect.draw(self.surface)
        # draw the hand
        self.hand.draw(self.surface)
        # draw the score
        ui.draw_text(self.surface, f"Score : {self.score}", (5, 0.9*SCREEN_HEIGHT), COLORS["score"], font=FONTS["medium"],
                    shadow=True, shadow_color=(255,255,255))
        
        # draw the high score
        ui.draw_text(self.surface, f"High score : {self.high_score}", (5, 0.95*SCREEN_HEIGHT), COLORS["score"], font=FONTS["medium"],
                    shadow=True, shadow_color=(255,255,255))

        # draw the time left
        timer_text_color = (160, 40, 0) if self.time_left < 5 else COLORS["timer"] # change the text color if less than 5 s left
        ui.draw_text(self.surface, f"Time left : {self.time_left}", (0.81*SCREEN_WIDTH, SCREEN_HEIGHT*0.95),  timer_text_color, font=FONTS["medium"],
                    shadow=True, shadow_color=(255,255,255))


    def game_time_update(self):
        self.time_left = max(round(GAME_DURATION - (time.time() - self.game_start_time), 1), 0)



    def update(self):

        self.load_camera()
        self.set_hand_position()
        self.game_time_update()

        self.draw()

        if self.time_left > 0:
            self.spawn_insects()
            (x, y) = self.hand_tracking.get_hand_center()
            self.hand.rect.center = (x, y)
            self.hand.left_click = self.hand_tracking.hand_closed
            print("Hand closed", self.hand.left_click)
            if self.hand.left_click:
                self.hand.image = self.hand.image_smaller.copy()
            else:
                self.hand.image = self.hand.orig_image.copy()
            self.score = self.hand.kill_insects(self.insects, self.score, self.sounds)

            if self.score > self.high_score:
                self.high_score = self.score

            for insect in self.insects:
                insect.move()

        else: # when the game is over
            self.draw_endgame()
            
            if self.score >= 10:
                # ui.present(self.surface, 1)
                ui.draw_text(self.surface, f"Score : {self.score}", (SCREEN_WIDTH*0.5, SCREEN_HEIGHT*0.5), COLORS["score"], font=FONTS["medium"],
                        shadow=True, shadow_color=(255,255,255), pos_mode="center")
                ui.draw_text(self.surface, "Congratulations! You have received gift", (SCREEN_WIDTH*0.5, SCREEN_HEIGHT*0.75), COLORS["title"], font=FONTS["medium"],
                    shadow=True, shadow_color=(0,0,0), pos_mode="center")
            # elif self.score >= 7:
            #     ui.present(self.surface, 2)
            #     ui.draw_text(self.surface, "Congratulations! You have received FPT Notebook", (SCREEN_WIDTH*0.5, SCREEN_HEIGHT*0.75), COLORS["title"], font=FONTS["medium"],
            #         shadow=True, shadow_color=(0,0,0), pos_mode="center")
            # elif self.score >= 5:
            #     ui.present(self.surface, 3)
            #     ui.draw_text(self.surface, "Congratulations! You have received FPT Card Strap", (SCREEN_WIDTH*0.5, SCREEN_HEIGHT*0.75), COLORS["title"], font=FONTS["medium"],
            #         shadow=True, shadow_color=(0,0,0), pos_mode="center")
            else:
                ui.draw_text(self.surface, f"Score : {self.score}", (SCREEN_WIDTH*0.5, SCREEN_HEIGHT*0.5), COLORS["score"], font=FONTS["medium"],
                        shadow=True, shadow_color=(255,255,255), pos_mode="center")
                ui.draw_text(self.surface, "Have a nice day!", (SCREEN_WIDTH*0.5, SCREEN_HEIGHT*0.75), COLORS["title"], font=FONTS["medium"],
                    shadow=True, shadow_color=(0,0,0), pos_mode="center")
                
            if ui.button(self.surface, SCREEN_HEIGHT - BUTTONS_SIZES[1]*2.2, "Continue", click_sound=self.sounds["slap"]):
                return "menu"

        cv2.resize(self.frame, (960, 540))
        cv2.imshow("Frame", self.frame)
        cv2.waitKey(1)
