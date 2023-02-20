import pygame
from color import COLOR

class Paddle(pygame.sprite.Sprite):
    
    def __init__(self, color, x, y, width, height):
        # init paddle
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(COLOR.BLACK_ALT)
        self.image.set_colorkey(COLOR.BLACK_ALT)

        # draw paddle
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # get collision object
        self.rect = self.image.get_rect()

        # set paddle location
        self.rect.x = x
        self.rect.y = y