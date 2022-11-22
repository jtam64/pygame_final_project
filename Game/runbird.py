import pygame
from screens.Game import game_screen
from screens.Welcome import welcome_screen
from screens.Gameover import gameover_screen

class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((1500, 800))

    def run(self):
        screens = {
            "welcome": welcome_screen,
            "game": game_screen,
            "gameover": gameover_screen
        }
    
        running = True
        current_screen = "game"

        while running:
            screen_class = screens.get(current_screen)

            screen = screen_class(self.window)

            screen.run()
