import pygame
from random import randint
from color import COLOR

class Ball(pygame.sprite.Sprite):
    
    def __init__(self, color, x, y, width, height):
        # ball init
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(COLOR.BLACK_ALT)
        self.image.set_colorkey(COLOR.BLACK_ALT)

        # draw ball (as a rectangle)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = [randint(-6, 6), randint(-6, 6)]

        # get collision rect
        self.rect = self.image.get_rect()

        # set coordinates
        self.rect.x = x
        self.rect.y = y
    
    def speed_up(self, var, a):
        """
        var: string x or y or xy
        a: acceleration (relative to velocity)

        returns new velocity
        """
        if var == "xy":
            self.speed_up("x", a)
            self.speed_up("y", a)
            return

        if var == "x":
            v = self.velocity[0]
        else:
            v = self.velocity[1]

        neg = False
        if v < 0:
            neg = True
            v = -v
        v += a

        if neg:
            v = -v
        if var == "x":
            self.velocity[0] = v
        else:
            self.velocity[1] = v
        
        return

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(6, 6)

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        if self.rect.x >= 690:
            self.reset()
            self.velocity[0] = -self.velocity[0]
        if self.rect.x <= 0:
            self.reset()
            self.velocity[0] = -self.velocity[0]
        if self.rect.y > 490:
            self.velocity[1] = -self.velocity[1]
            self.speed_up("xy", 0.25)
        if self.rect.y < 0:
            self.velocity[1] = -self.velocity[1]
            self.speed_up("xy", 0.25)

    def reset(self):
        self.rect.x = 345
        self.rect.y = 195
        self.velocity = [randint(-6, 6), randint(-6, 6)]