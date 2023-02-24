import pygame, sys
from pygame.locals import QUIT
from color import COLOR
from paddle import Paddle

SIZE = (700, 500)

pygame.init()

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption("Pong")

all_sprites_list = pygame.sprite.Group()

paddle1 = Paddle(COLOR.BLACK, 20, 200, 10, 100)
all_sprites_list.add(paddle1)
paddle2 = Paddle(COLOR.BLACK, 670, 200, 10, 100)
all_sprites_list.add(paddle2)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # update sprites
    all_sprites_list.update()

    # set background color
    screen.fill(COLOR.WHITE)

    # draw sprites
    all_sprites_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)