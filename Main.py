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

all_sprites_list = pygame.sprite.Group()

# initialize paddles
paddle1 = Paddle(COLOR.BLACK, 20, 200, 10, 100)
all_sprites_list.add(paddle1)

paddle2 = Paddle(COLOR.BLACK, 670, 200, 10, 100)
all_sprites_list.add(paddle2)

# initialize ball
ball = Ball(COLOR.BLACK, 345, 195, 10, 10)
all_sprites_list.add(ball)

# initialize game over text
end_p1 = GameOver("P1 WINS", COLOR.RED, 325, 225)
end_p2 = GameOver("P2 WINS", COLOR.BLUE, 325, 225)

# initialize scores
scores = []
score1 = Score(COLOR.RED, 100, 50)
all_sprites_list.add(score1)
scores.append(score1)

score2 = Score(COLOR.BLUE, 600, 50)
all_sprites_list.add(score2)
scores.append(score2)

def get_keypress():
    # keypress detection
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        paddle1.move_up(5)
    if keys[pygame.K_s]:
        paddle1.move_down(5)
    if keys[pygame.K_UP]:
        paddle2.move_up(5)
    if keys[pygame.K_DOWN]:
        paddle2.move_down(5)

def check_ball_bounds():
    # check ball bounce
    if ball.rect.x >= 690:
        # p1 scores
        ball.reset()
        ball.velocity[0] = -ball.velocity[0]
        score1.increment()
    if ball.rect.x <= 0:
        # p2 scores
        ball.reset()
        ball.velocity[0] = -ball.velocity[0]
        score2.increment()
    if ball.rect.y > 490 and ball.velocity[1] > 0:      
        ball.velocity[1] = -ball.velocity[1]
        ball.increment += 0.25
    if ball.rect.y < 0 and ball.velocity[1] < 0:
        ball.velocity[1] = -ball.velocity[1]
        ball.increment += 0.25

def detect_collisions():
    # detect collisions
    if pygame.sprite.collide_mask(ball, paddle1) \
        or pygame.sprite.collide_mask(ball, paddle2):
        ball.bounce()

def win_detection(p1, p2):
    """
    p1: the GameOver class for player 1
    p2: the GameOver class for player 2
    """
    # win detection
    if score1.score >= WIN:
        # p1 wins
        screen.blit(p1.image, (p1.x, p1.y))
    elif score2.score >= WIN:
        # p2 wins
        screen.blit(p2.image, (p2.x, p2.y))

def game_tick():
    # get keypresses
    get_keypress()
    # update sprites
    all_sprites_list.update()
    # check ball boundaries
    check_ball_bounds()
    # detects collisions
    detect_collisions()
    # set background color
    screen.fill(COLOR.WHITE)
    # detect win
    win_detection(end_p1, end_p2)
    # draw sprites
    all_sprites_list.draw(screen)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    game_tick()

    pygame.display.flip()
    clock.tick(TICK)