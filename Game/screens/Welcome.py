import pygame
from screens.Base import Base_screen

class Welcome_screen(Base_screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set background scroll level to 0
        self.x = 0

        # Display welcome text
        pygame.font.init()
        arial = pygame.font.SysFont("arial", 100)
        arialS = pygame.font.SysFont("arial", 50)
        self.welcome_surface = arial.render("Crappy Bird", True, (255, 255, 255))
        self.space_surface = arialS.render("Press space to play", True, (255, 255, 255))

    def draw(self):
        self.window.blit(self.welcome_surface, (520, 150))
        self.window.blit(self.space_surface, (550, 400))

    def manage_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.next_screen = "game"
            self.running = False
    
    def update(self):
        pass