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

        # make kite not spawn at first
        self.kite = 0

        # get ticks for flap cooldown
        self.last = pygame.time.get_ticks()

        # cooldown for flapping
        self.cooldown = 100

        # get random location for coins
        self.coin.rect.y = self.coin.random_pos()

        # add bird and coin sprites to group
        self.sprites.add(self.bird, self.coin)

        # set score to start at 1
        self.score = 1

    def draw(self):
        # draw sprites on window
        self.sprites.draw(self.window)

        # display highscore
        self.window.blit(self.high_score, (1375, 0))


    def manage_event(self, event):
        # check keypress for bird
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
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

        # check if coin leaves screen if it does, reset it
        if self.coin.rect.x <= 0:
            self.coin.default()

        # score based on distance
        self.score += (pygame.time.get_ticks() / 10000000) * math.sqrt(pygame.time.get_ticks())
        # render the score on screen
        score_card = self.arial.render("SCORE", True, (255, 255, 255))
        score_surface = self.arial.render(str(math.ceil(self.score)), True, (255, 255, 255))
        self.window.blit(score_card, (0, 0))
        self.window.blit(score_surface, (0, 20))

        # add gravity for bird
        self.bird.gravity()

        # after slight delay, reset flapping bird image to default
        now = pygame.time.get_ticks()
        if now >= self.last + self.cooldown:
            self.bird.default()

        # variable coin value modifier
        modifier = self.score / 100
        self.coin.alter_value(modifier)

        # check coin collection event
        if self.bird.rect.colliderect(self.coin.rect):
            # add coin value to score
            score_add = self.arial.render(str(f"+{self.coin.value}"), True, (255, 255, 255))
            self.window.blit(score_add, (self.coin.rect.x, self.coin.rect.y))
            self.score += self.coin.value
            self.coin.default()

        # every 100 points increase speed
        if int(self.score) % 100 == 0:
            self.x += 1

        # every 1000 points spawn a kite, check if kite exists first
        if int(self.score) % 100 == 0 and self.kite == 0:
            self.kite = Kite()
            self.sprites.add(self.kite)
        # if kite is already spawned, reset kite to default
        if int(self.score) % 100 == 0 and self.kite !=0 and self.kite.rect.x < 0:
            self.kite.default()


        # FAIL CONDITIONS
        # if bird hits kite
        if self.kite != 0:
            self.kite.scrolling(self.x)
            # check collision event
            if self.bird.rect.colliderect(self.kite.rect):
                self.keeper + int(self.score)
                self.next_screen = "gameover"
                self.running = False
        # if bird hits ground
        if self.bird.crash():
            self.keeper + int(self.score)
            self.next_screen = "gameover"
            self.running = False

        # WIN CONDITION at 1,000,000 points
        if self.score >= 1_000_000:
            self.keeper + int(self.score)
            self.next_screen = "win"
            self.running = False