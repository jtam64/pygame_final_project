import pygame

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sprites/flap1.png")
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 400

    def check_window(self):
        pass

    def move(self, direction):
        if direction == "up":
            print(direction)
            self.rect.y -= 50

    def gravity(self):
        self.rect.y += 8