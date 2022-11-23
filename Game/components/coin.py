import pygame
import random

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sprites/coin.png")
        self.rect = self.image.get_rect()

    def random_pos(self):
        x_cord = random.randint(0, 550)
        y_cord = random.randint(800, 2000)
        return [x_cord, y_cord]