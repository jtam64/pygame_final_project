import pygame
from screens.Game import Game_screen
from screens.Welcome import Welcome_screen
from screens.Gameover import Gameover_screen

class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((1500, 800))

    def run(self):
        screens = {
            "welcome": Welcome_screen,
            "game": Game_screen,
            "gameover": Gameover_screen
        }

        running = True
        current_screen = "welcome"

        while running:
            screen_class = screens.get(current_screen)

            screen = screen_class(self.window)

            screen.run()

if __name__ == "__main__":
    runbird = Game()
    runbird.run()