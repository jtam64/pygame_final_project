import pygame
import random

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sprites/coin.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1500

    def random_pos(self):
        return random.randint(0, 600)

    def static_coin(self):
        self.rect.x -= 5

    def default(self):
        self.rect.y = self.random_pos()
        self.rect.x = 1500

    def scrolling(self):
        self.rect.x -= 10