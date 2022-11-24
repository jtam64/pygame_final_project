import pygame
from screens.Base import Base_screen

class Gameover_screen(Base_screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.x = 0
        self.end_text = self.arialB.render("Game Over", True, (255, 255, 255))
        self.player_score = self.arialS.render(f"Your score was: {str(self.keeper.newest)}", True, (255, 255, 255))

    def manage_event(self, event):
        '''Replay with spacebar

        Args:
            event: replay game with spacebar
        '''
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.next_screen = "welcome"
            self.running = False

    def update(self):
        pass

    def draw(self):
        '''Draw text on screen
        '''
        self.window.blit(self.end_text, (250, 200))
        self.window.blit(self.high_score_huge, (250, 400))
        self.window.blit(self.player_score, (250, 600))