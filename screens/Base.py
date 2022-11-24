import pygame
from helper.score import Score
class Base_screen:
    def __init__(self, window):
        # initialize font
        pygame.font.init()

        # set window
        self.window = window
        self.next_screen = False

        # import background image
        self.bg = pygame.image.load("sprites/bg.png")
        self.bg = pygame.transform.scale(self.bg, (3000, 800))
        # variables for scrolling background
        self.i = 0
        self.x = 10

        # Initiate helper file
        self.keeper = Score()

        # add fonts
        self.arialT = pygame.font.SysFont("arial", 20)
        self.arialS = pygame.font.SysFont("arial", 50)
        self.arialB = pygame.font.SysFont("arial", 200)
        self.arial = pygame.font.SysFont("arial", 25)

        # add highscore variable available to all screens
        self.high_score = self.arialT.render(f"Highscore {str(self.keeper.highest)}", True, (255, 255, 255))
        self.high_score_huge = self.arialS.render(f"Highscore {str(self.keeper.highest)}", True, (255, 255, 255))

    def run(self):
        '''How the game runs
        '''
        self.running = True
        while self.running:
            clock = pygame.time.Clock()

            clock.tick(30)

            self.update()

            self.draw()

            pygame.display.update()

            # scrolling background
            self.window.fill((0, 0, 0))
            self.window.blit(self.bg, (self.i, 0))
            # add another background at the end of the first one
            self.window.blit(self.bg, (3000+self.i, 0))
            # when background reaches the end, reset background and add a new one
            if self.i <= -3000:
                self.window.blit(self.bg, (3000+self.i, 0))
                self.i = 0

            # scroll background by variable
            self.i -= self.x

            # Event loop
            for event in pygame.event.get():
                # 2 quit options, escape key or clicking the x
                if event.type == pygame.QUIT:
                    self.running = False
                    self.next_screen =  False

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False
                    self.next_screen = False

                # Child class event handler
                self.manage_event(event)