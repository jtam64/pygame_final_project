import pygame
import random
from components.sprite import Sprite

class Coin(Sprite):
    '''Coin sprite for collection

    Args:
        Sprite (object): Set the image and rect for the coin
    '''
    def __init__(self):
        '''Permanent x value for the coin
        '''
        super().__init__("sprites/coin.png")
        self.rect.x = 1500
        self.value = 5

    def random_pos(self) -> int:
        '''Spawn coin at random y position

        Returns:
            int: random integer between 0 and 600
        '''
        return random.randint(0, 600)

    def default(self):
        '''Resets the position for the coin
        '''
        self.rect.y = self.random_pos()
        self.rect.x = 1500

    def scrolling(self, x:int):
        '''Makes coin move with the background

        Args:
            x (int): A value to move the coin 
        '''
        self.rect.x -= x

    def alter_value(self, modifier:int):
        '''Modifies the value of the coin depending on modifier

        Args:
            modifier (int): A value passed in to modify the coin value
        '''
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
