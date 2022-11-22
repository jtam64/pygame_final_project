import pygame
from screens.Base import Base_screen

class Game_screen(Base_screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def draw(self):
        pass

    def manage_event(self, event):
        pass