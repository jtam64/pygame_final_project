import pygame
from screens.Base import Base_screen

class Welcome_screen(Base_screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set background scroll level to 0
        self.x = 0

        # Title images
        self.title = pygame.image.load("sprites/title.png")


        self.space_surface = self.arialS.render("Press space to play", True, (255, 255, 255))

    def draw(self):
        # Draw welcome text and title
        self.window.blit(self.title, (520, 150))
        self.window.blit(self.space_surface, (550, 400))
        self.window.blit(self.high_score, (1375, 0))

    def manage_event(self, event):
        # check for game start event
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.next_screen = "game"
            self.running = False
    
    def update(self):
        pass