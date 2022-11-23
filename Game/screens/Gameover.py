import pygame
from screens.Base import Base_screen

class Gameover_screen(Base_screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.x = 0

        pygame.font.init()
        self.arialB = pygame.font.SysFont("arial", 200)


    def manage_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.next_screen = "welcome"
            self.running = False

    def update(self):
        end_text = self.arialB.render("Game Over", True, (255, 255, 255))
        self.window.blit(end_text, (250, 200))

    def draw(self):
        pass