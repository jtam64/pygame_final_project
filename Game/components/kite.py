import pygame
from components.sprite import Sprite

class Kite(Sprite):
    def __init__(self):
        super().__init__( "sprites/kite.png")
        self.rect.x = 1500
