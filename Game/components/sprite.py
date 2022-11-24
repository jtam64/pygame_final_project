import pygame

class Sprite(pygame.sprite.Sprite):
    '''Sprite class for all sprites in the game

    Args:
        pygame (class from pygame): Sprite class from pygame
    '''
    def __init__(self, image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
