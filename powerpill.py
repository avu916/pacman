import pygame


class Powerpill(object):
    def __init__(self, dim, pos):
        self.dim = dim
        self.pos = pos
        self.height = 24
        self.width = 24
        img = pygame.image.load('images/powerpill.png')
        img = pygame.transform.scale(img, (self.height, self.width))
        self.img = img

    def draw(self, screen):
        values = list(self.pos)+list(self.dim)
        # pygame.draw.rect(screen, self.img, values)
        screen.blit(self.img, values)
