import pygame

class Base_screen:
    def __init__(self, window):
        self.window = window

        # import background image
        self.bg = pygame.image.load("sprites/bg.png")
        self.bg = pygame.transform.scale(self.bg, (3000, 800))
        self.i = 0

    def run(self):
        self.running = True
        while self.running:
            clock = pygame.time.Clock()
            clock.tick(30)
            pygame.display.update()

            # scrolling background
            self.window.fill((0, 0, 0))
            self.window.blit(self.bg, (self.i, 0))
            self.window.blit(self.bg, (3000+self.i, 0))
            # when background reaches the end, reset background
            if self.i == -3000:
                self.window.blit(self.bg, (3000+self.i, 0))
                self.i = 0
            # scroll background by number
            self.i -= 3

            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    quit()
