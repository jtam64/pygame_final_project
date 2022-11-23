import pygame
from screens.Base import Base_screen
from components.bird import Bird
from components.coin import Coin
from components.kite import Kite
import math
from helper.score import Score

class Game_screen(Base_screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # get sprites
        self.sprites = pygame.sprite.Group()
        self.bird = Bird()
        self.coin = Coin()
        self.kite = 0

        # get ticks for flap cooldown
        self.last = pygame.time.get_ticks()
        self.cooldown = 100

        #add arial font
        self.arial = pygame.font.SysFont("arial", 25)

        # get random location for coins
        self.coin.rect.y = self.coin.random_pos()

        # add all sprites to group
        self.sprites.add(self.bird, self.coin)

        # def score
        self.score = 1

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
        # make coin y position move
        self.coin.scrolling(self.x)

        # check if coin leaves screen
        if self.coin.rect.x <= 0:
            self.coin.default()

        # scorecard based on distance
        self.score += (pygame.time.get_ticks() / 10000000) * math.sqrt(pygame.time.get_ticks())
        score_card = self.arial.render("SCORE", True, (255, 255, 255))
        score_surface = self.arial.render(str(math.ceil(self.score)), True, (255, 255, 255))
        self.window.blit(score_card, (0, 0))
        self.window.blit(score_surface, (0, 20))

        # implement gravity for bird
        self.bird.gravity()

        # after slight delay, reset image to default
        now = pygame.time.get_ticks()
        if now >= self.last + self.cooldown:
            self.bird.default()

        # check coin collection event
        if self.bird.rect.colliderect(self.coin.rect):
            score_add = self.arial.render("+10", True, (255, 255, 255))
            self.window.blit(score_add, (self.coin.rect.x, self.coin.rect.y))
            self.score += 10
            self.coin.default()

        # every 100 points increase speed
        if int(self.score) % 100 == 0:
            self.x += 1

        # every 1000 points spawn a kite
        if int(self.score) % 100 == 0 and self.kite == 0:
            self.kite = Kite()
            self.sprites.add(self.kite)
        
        if int(self.score) % 100 == 0 and self.kite !=0 and self.kite.rect.x < 0:
            self.kite.default()


        # FAIL CONDITIONS
        if self.kite != 0:
            self.kite.scrolling(self.x)
            # check collision event
            if self.bird.rect.colliderect(self.kite.rect):
                self.next_screen = "gameover"
                self.running = False
        
        # check crash event
        if self.bird.crash():
            self.next_screen = "gameover"
            self.running = False