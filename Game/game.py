import pygame


def main():

    pygame.init
    window = pygame.display.set_mode((500, 500))
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
if __name__ == "__main__":
    main()