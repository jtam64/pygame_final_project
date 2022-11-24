import pygame
from screens.Game import Game_screen
from screens.Welcome import Welcome_screen
from screens.Gameover import Gameover_screen
from screens.Win import Win_screen

class Game:
    '''The game runs off of this file. Screens is a dictionary of all the screens that can be displayed.
    '''
    def __init__(self):
        self.window = pygame.display.set_mode((1500, 800))

    def run(self):
        screens = {
            "welcome": Welcome_screen,
            "game": Game_screen,
            "gameover": Gameover_screen,
            "win": Win_screen
        }

        running = True
        current_screen = "welcome"

        while running:
            # Get the current screen
            screen_class = screens.get(current_screen)
            # Create an instance of the screen
            screen = screen_class(self.window)
            # Run the screen
            screen.run()
            # If next screen is false, game ends
            if screen.next_screen is False:
                running = False
            # Set the current screen to the next screen
            current_screen = screen.next_screen

if __name__ == "__main__":
    runbird = Game()
    runbird.run()