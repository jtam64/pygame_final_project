import pygame
from screens.Base import Base_screen

class Gameover_screen(Base_screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.x = 0

    def manage_event(self, event):
        pass

    def update(self):
        pass

    def draw(self):
        pass