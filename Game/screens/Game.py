import pygame
from screens.Base import Base_screen
from components.bird import Bird

class Game_screen(Base_screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sprites = pygame.sprite.Group()
        self.bird = Bird()

        self.sprites.add(self.bird)

    def draw(self):
        self.sprites.draw(self.window)

    def manage_event(self, event):
        pass

    def update(self):
        self.bird.gravity()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.bird.move("up")