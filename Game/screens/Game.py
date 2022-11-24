import pygame
from screens.Base import Base_screen
from components.bird import Bird
from components.coin import Coin
from components.kite import Kite
import math

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

        # set score to start at 1
        self.score = 999990

    def draw(self):
        # draw sprites on window
        self.sprites.draw(self.window)
        # display highscore
        self.window.blit(self.high_score, (1375, 0))


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

        # add gravity for bird
        self.bird.gravity()

        # after slight delay, reset flapping bird to default
        now = pygame.time.get_ticks()
        if now >= self.last + self.cooldown:
            self.bird.default()

        # variable coin value modifier
        modifier = self.score / 100
        self.coin.alter_value(modifier)

        # check coin collection event
        if self.bird.rect.colliderect(self.coin.rect):
            score_add = self.arial.render(str(f"+{self.coin.value}"), True, (255, 255, 255))
            self.window.blit(score_add, (self.coin.rect.x, self.coin.rect.y))
            self.score += self.coin.value
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
                self.keeper + int(self.score)
                self.next_screen = "gameover"
                self.running = False
        
        # check crash event
        if self.bird.crash():
            self.keeper + int(self.score)
            self.next_screen = "gameover"
            self.running = False

        # WIN CONDITION at 1,000,000 points
        if self.score >= 1_000_000:
            self.keeper + int(self.score)
            self.next_screen = "win"
            self.running = False