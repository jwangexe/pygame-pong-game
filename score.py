import pygame, pygame.freetype

pygame.freetype.init()

class Score(pygame.sprite.Sprite):
    FONTSIZE = 18

    def __init__(self, color, x, y):
        super().__init__()
        self.color = color
        # get font object
        self.font = pygame.freetype.Font("./ARCADE_N.TTF")
        # init score
        self.score = 0
        # get image and set coords
        self.image, self.rect = self.font.render(str(self.score), fgcolor=color, size=self.FONTSIZE)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
    
    def increment(self):
        self.score += 1
    
    def update(self):
        self.image, self.rect = self.font.render(str(self.score), fgcolor=self.color, size=self.FONTSIZE)
        self.rect.x = self.x
        self.rect.y = self.y
    
    def reset(self):
        self.score = 0