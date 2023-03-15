import pygame, pygame.freetype

pygame.freetype.init()

class GameOver():
    FONTSIZE = 27

    def __init__(self, text, textcolor, x, y):

        # init text
        self.color = textcolor
        self.font = pygame.freetype.Font("./ARCADE_N.TTF")
        self.text = text

        # get text and rect
        self.image, self.rect = self.font.render(self.text, fgcolor=self.color, size=self.FONTSIZE)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y