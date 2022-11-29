import pygame
from screens.Base import Base_screen

'''Render the gameover screen
'''
class Gameover_screen(Base_screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Render enc text, player score, and highscore
        self.end_text = self.arialB.render("Game Over", True, (255, 255, 255))
        self.player_score = self.arialS.render(f"Your score was: {str(self.keeper.get_newest())}", True, (255, 255, 255))
        # get user text input box
        self.user_text = ""
        self.input_rect = pygame.Rect(400, 500, 140, 50)
        # get color values for box
        self.color_inactive = pygame.Color('lightblue3')
        self.color_active = pygame.Color('darkblue')
        self.color = self.color_inactive

        # text box is off by default
        self.active = False

    def manage_event(self, event):
        '''Event handler for end screen

        Args:
            event: Event to handle
        '''
        # check for mouse click event within the input box
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.input_rect.collidepoint(event.pos):
                self.active = True

        if self.active:
            # change the colour of the box
            self.color = self.color_active

            # check for backspace and remove last character
            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                self.user_text = self.user_text[:-1]

            if event.type == pygame.KEYDOWN and not event.key == pygame.K_BACKSPACE and not event.key == pygame.K_RETURN:
                # check for keypress and add to user text
                if len(self.user_text) < 4:
                    self.user_text += event.unicode.upper()
            
            # check for enter key and save score
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.keeper.add_score_to_scores(self.user_text, self.keeper.get_newest())
                self.running = False

    def draw(self):
        '''Draw text on screen
        '''
        self.window.blit(self.end_text, (250, 200))
        self.window.blit(self.high_score_huge, (250, 400))
        self.window.blit(self.player_score, (250, 600))

        pygame.draw.rect(self.window, self.color, self.input_rect)
        text_surface = self.arialS.render(self.user_text, True, (255, 255, 255))
        self.window.blit(text_surface, (self.input_rect.x + 5, self.input_rect.y + 5))
        self.input_rect.w = max(100, text_surface.get_width()+10)
