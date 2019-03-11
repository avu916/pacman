import pygame


class Shield(object):
    def __init__(self, dim, pos):
        self.dim = dim
        self.pos = pos
        self.height = 24
        self.width = 24
        img = pygame.image.load('images/shield.png')
        img = pygame.transform.scale(img, (self.height, self.width))
        self.img = img

    def draw(self, screen):
        values = list(self.pos)+list(self.dim)
        # pygame.draw.rect(screen, self.img, values)
        screen.blit(self.img, values)
