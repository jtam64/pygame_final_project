import pygame

class Kite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sprites/kite.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1500
