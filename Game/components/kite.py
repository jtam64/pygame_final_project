import pygame
from components.sprite import Sprite
import random

class Kite(Sprite):
    '''Kite sprite for lose event

    Args:
        Sprite (object): sets the image and rect for the kite
    '''
    def __init__(self):
        super().__init__( "sprites/kite.png")
        self.default()

    def scrolling(self, x:int):
        '''Move with background

        Args:
            x (int): variable to move sprite in
        '''
        self.rect.x -= x

    def default(self):
        '''Resets kite to default position
        '''
        self.rect.x = 1500
        self.rect.y = random.randint(0, 600)