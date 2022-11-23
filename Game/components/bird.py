import pygame

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sprites/flap1.png")
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 400

    def check_window(self):
        if self.rect.y <= -50:
            self.rect.y = -50

    def move(self, direction):
        if direction == "up":
            self.rect.y -= 150
        self.check_window()

    def flap(self):
        self.image = pygame.image.load("sprites/flap4.png")
    
    def default(self):
        self.image = pygame.image.load("sprites/flap1.png")


    def gravity(self):
        self.rect.y += 10
