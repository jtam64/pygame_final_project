from screens.Base import Base_screen
import pygame

class Win_screen(Base_screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # win text
        self.win_text = self.arialB.render("You Win!", True, (255, 255, 255))
        self.win_score = self.arialS.render("Score reached 1,000,000", True, (255, 255, 255))
    
    def draw(self):
        # display win text
        self.window.blit(self.win_text, (250, 200))
        self.window.blit(self.win_score, (250, 400))
    
    def update(self):
        pass

    def manage_event(self, event):
        # if spacebar is pressed play again
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.next_screen = "welcome"
            self.running = False