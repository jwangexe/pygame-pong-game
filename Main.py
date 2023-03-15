import pygame, sys, time
from pygame.locals import QUIT
from color import COLOR
from paddle import Paddle
from ball import Ball
from score import Score
from end_text import GameOver

SIZE = (700, 500) # size of game window
TICK = 60 # number of ms per tick
WIN = 10 # number of points to win

pygame.init()

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption("Pong")

class Game():

    def __init__(self):
        self.game_sprites_list = pygame.sprite.Group()

        # initialize paddles
        self.paddle1 = Paddle(COLOR.BLACK, 20, 200, 10, 100)
        self.game_sprites_list.add(self.paddle1)

        self.paddle2 = Paddle(COLOR.BLACK, 670, 200, 10, 100)
        self.game_sprites_list.add(self.paddle2)

        # initialize ball
        self.ball = Ball(COLOR.BLACK, 345, 195, 10, 10)
        self.game_sprites_list.add(self.ball)

        # initialize game over text
        self.end_p1 = GameOver("P1 WINS", COLOR.RED, 325, 225)
        self.end_p2 = GameOver("P2 WINS", COLOR.BLUE, 325, 225)

        # initialize scores
        self.scores = []
        self.score1 = Score(COLOR.RED, 100, 50)
        self.game_sprites_list.add(self.score1)
        self.scores.append(self.score1)

        self.score2 = Score(COLOR.BLUE, 600, 50)
        self.game_sprites_list.add(self.score2)
        self.scores.append(self.score2)

    def get_keypress(self):
        # keypress detection
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.paddle1.move_up(5)
        if keys[pygame.K_s]:
            self.paddle1.move_down(5)
        if keys[pygame.K_UP]:
            self.paddle2.move_up(5)
        if keys[pygame.K_DOWN]:
            self.paddle2.move_down(5)

    def check_ball_bounds(self):
        # check ball bounce
        if self.ball.rect.x >= 690:
            # p1 scores
            self.ball.reset()
            self.ball.velocity[0] = -self.ball.velocity[0]
            self.score1.increment()
        if self.ball.rect.x <= 0:
            # p2 scores
            self.ball.reset()
            self.ball.velocity[0] = -self.ball.velocity[0]
            self.score2.increment()
        if self.ball.rect.y > 490 and self.ball.velocity[1] > 0:      
            self.ball.velocity[1] = -self.ball.velocity[1]
            self.ball.increment += 0.25
        if self.ball.rect.y < 0 and self.ball.velocity[1] < 0:
            self.ball.velocity[1] = -self.ball.velocity[1]
            self.ball.increment += 0.25

    def detect_collisions(self):
        # detect collisions
        if pygame.sprite.collide_mask(self.ball, self.paddle1) \
            or pygame.sprite.collide_mask(self.ball, self.paddle2):
            self.ball.bounce()

    def win_detection(self, p1, p2):
        """
        p1: the GameOver class for player 1
        p2: the GameOver class for player 2
        """
        # win detection
        if self.score1.score >= WIN:
            # p1 wins
            screen.blit(p1.image, (p1.x, p1.y))
        elif self.score2.score >= WIN:
            # p2 wins
            screen.blit(p2.image, (p2.x, p2.y))

    def game_tick(self):
        # get keypresses
        self.get_keypress()
        # update sprites
        self.game_sprites_list.update()
        # check ball boundaries
        self.check_ball_bounds()
        # detects collisions
        self.detect_collisions()
        # set background color
        screen.fill(COLOR.WHITE)
        # detect win
        self.win_detection(self.end_p1, self.end_p2)
        # draw sprites
        self.game_sprites_list.draw(screen)

game = Game()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    game.game_tick()

    pygame.display.flip()
    clock.tick(TICK)