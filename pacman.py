import pygame


class Pacman(object):
    def __init__(self, dim, pos):
        self.dim = dim
        self.pos = pos
        self.height = 24
        self.width = 24
        img = pygame.image.load('images/pacman_right1.png')
        img = pygame.transform.scale(img, (self.height, self.width))
        self.img = img

    def draw(self, screen):
        values = list(self.pos)+list(self.dim)
        # pygame.draw.rect(screen, self.img, values)
        screen.blit(self.img, values)

    # def move(self):
    #     key_pressed = pygame.key.get_pressed()
        # if key_pressed[pygame.K_UP]:
        #     self.position.y -= 3
        # if key_pressed[pygame.K_DOWN]:
        #     self.position.y += 3
        # if key_pressed[pygame.K_LEFT]:
        #     self.position.x -= 3
        # if key_pressed[pygame.K_RIGHT]:
        #     self.position.x += 3

    # def render(self, screen):
    #     pygame.draw.circle(screen, self.img, self.pos)
