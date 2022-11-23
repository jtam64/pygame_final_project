import pygame
from components.sprite import Sprite
import random

class Kite(Sprite):
    def __init__(self):
        super().__init__( "sprites/kite.png")
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.default()

    def scrolling(self, x):
        self.rect.x -= x

    def default(self):
        self.rect.x = 1500
        self.rect.y = random.randint(0, 600)