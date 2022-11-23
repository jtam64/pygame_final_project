import pygame
import random
from components.sprite import Sprite

class Coin(Sprite):
    def __init__(self):
        super().__init__("sprites/coin.png")
        self.rect.x = 1500

    def random_pos(self):
        return random.randint(0, 600)

    def default(self):
        self.rect.y = self.random_pos()
        self.rect.x = 1500

    def scrolling(self, x):
        self.rect.x -= x