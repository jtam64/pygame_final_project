import pygame
from screens.Base import base_screen

class game_screen(base_screen):
    def __init__(self):
        super().__init__()
        # make background scroll
        self.window.fill((0,0,0))
        self.window.blit(self.bg, (self.i, 0))
        self.window.blit(self.bg, (3000+self.i, 0))

        # when background reaches the end, reset background
        self.i = 0
        if self.i == -3000:
            self.window.blit(self.bg, (3000+self.i, 0))
            self.i = 0

        # scroll background by number
        self.i -= 3
