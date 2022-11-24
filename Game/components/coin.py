import pygame
import random
from components.sprite import Sprite

class Coin(Sprite):
    def __init__(self):
        super().__init__("sprites/coin.png")
        self.rect.x = 1500
        self.value = 5

    def random_pos(self):
        return random.randint(0, 600)

    def default(self):
        self.rect.y = self.random_pos()
        self.rect.x = 1500

    def scrolling(self, x):
        self.rect.x -= x

    def alter_value(self, modifier):
        if modifier > 1:
            if 1 <= modifier <= 10:
                self.value = 15
            elif 11 <= modifier <= 20:
                self.value = 100
            elif 21 <= modifier <= 30:
                self.value = 200
            elif 31 <= modifier <= 40:
                self.value = 500
            elif 41 <= modifier <= 50:
                self.value = 1000
