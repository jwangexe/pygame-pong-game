import pygame, sys
from pygame.locals import QUIT
from color import COLOR
from paddle import Paddle
from ball import Ball

SIZE = (700, 500)

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

#initialize ball
ball = Ball(COLOR.BLACK, 345, 195, 10, 10)
all_sprites_list.add(ball)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

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

    # update sprites
    all_sprites_list.update()

    # set background color
    screen.fill(COLOR.WHITE)

    # draw sprites
    all_sprites_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)