import pygame
from pygame.locals import *
from blocks import Brick
from pill import Pill
from powerpill import Powerpill
from shield import Shield
from numpy import loadtxt
from pacman import Pacman
from blinky import Blinky
from pinky import Pinky
from inky import Inky
from clyde import Clyde


pacman = Pacman((24, 24), (160, 160))


def play_intro():
    intro_sound = pygame.mixer.Sound("sounds/pacman_beginning.wav")
    pygame.mixer.Sound.play(intro_sound)


def game():
    pygame.init()
    play_intro()
    grid = loadtxt('maze.txt', dtype=str)
    rows, cols = grid.shape
    width, height = (24, 24)
    screen_size = (width*cols, height*rows)
    screen = pygame.display.set_mode(screen_size, 0, 32)
    block_list = []
    for col in range(cols):
        for row in range(rows):
            value = grid[row][col]
            if value == 'X':
                pos = (col*width, row*height)
                block_list.append(Brick((width, height), pos))
            elif value == 'S':
                pos = (col*width, row*height)
                block_list.append(Shield((width, height), pos))
            elif value == '-' or value == '|' or value == 'N':
                pos = (col * width, row * height)
                block_list.append(Pill((width, height), pos))
            elif value == 'P':
                pos = (col * width, row * height)
                block_list.append(Powerpill((width, height), pos))
            elif value == 'Y':
                pos = (col * width, row * height)
                block_list.append(Pacman((width, height), pos))
            elif value == 'b':
                pos = (col * width, row * height)
                block_list.append(Blinky((width, height), pos))
            elif value == 'i':
                pos = (col * width, row * height)
                block_list.append(Inky((width, height), pos))
            elif value == 'p':
                pos = (col * width, row * height)
                block_list.append(Pinky((width, height), pos))
            elif value == 'c':
                pos = (col * width, row * height)
                block_list.append(Clyde((width, height), pos))
    background = pygame.Surface(screen_size).convert()
    background.fill((0, 0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        # pacman.move()
        # for tile in tiles:
        #     pacman.collide(tile)
        screen.blit(background, (0, 0))
        for blocks in block_list:
            blocks.draw(screen)
        # pacman.draw(screen)
        pygame.display.update()
