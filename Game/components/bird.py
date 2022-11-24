import pygame
from components.sprite import Sprite

class Bird(Sprite):
    '''Bird sprite for the main character of the game.

    Args:
        Sprite (object): Sprite is the parent class the will setup the image and rect for the bird
    '''
    def __init__(self):
        super().__init__("sprites/flap1.png")
        self.rect.x = 400
        self.rect.y = 400

    def check_window(self):
        '''Checks if bird leaves the top of the window and if so, it will keep it within the window.
        '''
        if self.rect.y <= -50:
            self.rect.y = -50

    def move(self, direction:str):
        '''Flap method for the bird

        Args:
            direction (str): If direction is up, move the bird 150 pixels up
        '''
        if direction == "up":
            self.rect.y -= 150
        self.check_window()

    def flap(self):
        '''Flap animation for the bird
        '''
        self.image = pygame.image.load("sprites/flap4.png")
    
    def default(self):
        '''Reset the bird to the default image
        '''
        self.image = pygame.image.load("sprites/flap1.png")

    def gravity(self):
        '''Gravity for the bird
        '''
        self.rect.y += 15

    def crash(self):
        '''Checks if the bird crashed into the bottom of the screen

        Returns:
            bool: returns true or false if bird is above 650 y pixels
        '''
        return self.rect.y >= 650