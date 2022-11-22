import pygame

class Sprites(pygame.sprite.Sprite):
    def __init__(self, limits=None):
        super().init()
        self.limits = limits