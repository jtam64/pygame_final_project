import pygame

class Game:
    def __init__(self):
        pass
    
    def game(self):
        # Initialize game and set screen
        pygame.init
        window = pygame.display.set_mode((1500, 800))
        running = True
        clock = pygame.time.Clock()
        # import background image and begin scrolling
        bg = pygame.image.load("sprites/bg.png")
        bg = pygame.transform.scale(bg, (3000, 800))
        i = 0

        while running:
            # make background scroll
            window.fill((0,0,0))
            window.blit(bg, (i, 0))
            window.blit(bg, (3000+i, 0))
            # when background reaches the end, reset background
            if i == -3000:
                window.blit(bg, (3000+i, 0))
                i = 0
            # scroll background by number
            i -= 3

            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    quit()

            pygame.display.update()

def main():
    g = Game()
    g.game()

if __name__ == "__main__":
    main()