import pygame
from screens.Base import Base_screen
from components.bird import Bird
from components.coin import Coin


class Game_screen(Base_screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # get sprites
        self.sprites = pygame.sprite.Group()
        self.bird = Bird()
        self.coin = Coin()

        self.sprites.add(self.bird)

        # get ticks for flap cooldown
        self.last = pygame.time.get_ticks()
        self.cooldown = 100

        #fonts 
        self.arial = pygame.font.SysFont("arial", 25)

    def draw(self):
        # draw sprites on window
        self.sprites.draw(self.window)

    def manage_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # check keypress for bird
            now = pygame.time.get_ticks()
            
            # check if last flap was within cooldown
            if now - self.last >= self.cooldown:
                self.last = now
                self.bird.move("up")

                # add flapping animation
                self.bird.flap()


    def update(self):
        # scorecard based on distance
        score = str(pygame.time.get_ticks() / 100)
        score_card = self.arial.render("SCORE", True, (255, 255, 255))
        score_surface = self.arial.render(score, True, (255, 255, 255))
        self.window.blit(score_card, (0, 0))
        self.window.blit(score_surface, (0, 20))

        # implement gravity for bird
        self.bird.gravity()


        # after slight delay, reset image to default
        now = pygame.time.get_ticks()
        if now >= self.last + self.cooldown:
            self.bird.default()

        # check crash event
        if self.bird.rect.y == 650:
            self.next_screen = "gameover"
            self.running = False