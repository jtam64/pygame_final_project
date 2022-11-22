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
        self.text_surface = arial.render("Crappy Bird", True, (255, 255, 255))

        # Start button


    def draw(self):
        self.window.blit(self.text_surface, (550, 150))

    def manage_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.next_screen = "game"
            self.running = False