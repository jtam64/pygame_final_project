import pygame

class base_screen:
    def __init__(self, window):
        self.window = window

        # import background image
        self.bg = pygame.image.load("sprites/bg.png")
        self.bg = pygame.transform.scale(self.bg, (3000, 800))

    def run(self):
        self.running = True
        while self.running:
            clock = pygame.time.Clock()
            clock.tick(30)
            self.update()
            self.draw()
            pygame.display.update()

            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    quit()
