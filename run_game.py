import time
from game import *

pygame.init()

display_width = 600
display_height = 800

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('PACMAN')
clock = pygame.time.Clock()

title = pygame.image.load('images/title.png')
title_rect = title.get_rect()
title_rect = ((display_width / 2) - title_rect.centerx, (display_height / 10))
font = pygame.font.Font(None, 32)
text1 = font.render("PLAY GAME", 2, white)
textpos1 = text1.get_rect()
textpos1 = ((display_width / 2) - textpos1.centerx, (display_height / 2) + (display_height / 4))

text2 = font.render("HIGH SCORES", 2, white)
textpos2 = text2.get_rect()
textpos2 = ((display_width / 2) - textpos2.centerx, (display_height / 2) + (display_height / 3))

text3 = font.render("Blinky", 16, white)
textpos3 = text3.get_rect()
textpos3 = ((display_width / 2) - textpos3.centerx, (display_height / 2) - (display_height / 15))

text4 = font.render("Pinky", 2, white)
text5 = font.render("Inky", 2, white)
text6 = font.render("Clyde", 2, white)

pacmanRight = [pygame.image.load('images/pacman_right1.png'), pygame.image.load('images/pacman_right2.png'),
               pygame.image.load('images/pacman_right3.png'), pygame.image.load('images/pacman_right4.png')]
pacmanLeft = [pygame.image.load('images/pacman_left1.png'), pygame.image.load('images/pacman_left2.png'),
              pygame.image.load('images/pacman_left3.png'), pygame.image.load('images/pacman_left4.png')]

redRight = [pygame.image.load('images/red_right1.png'), pygame.image.load('images/red_right2.png')]
pinkRight = [pygame.image.load('images/pink_right1.png'), pygame.image.load('images/pink_right2.png')]
blueRight = [pygame.image.load('images/blue_right1.png'), pygame.image.load('images/blue_right2.png')]
orangeRight = [pygame.image.load('images/orange_right1.png'), pygame.image.load('images/orange_right2.png')]
deadGhost = [pygame.image.load('images/dead1.png'), pygame.image.load('images/dead2.png')]
powerPill = pygame.image.load('images/powerpill.png')
transparent = (0, 0, 0)
x_pos = -32
y_pos = display_height/2
x_pos2 = -32
x_vel = 5
x_vel2 = 5
x_pos3 = -32
x_pos4 = -32
x_pos5 = -32

hover_text1 = font.render("PLAY GAME", 2, red)
walk_count = 0
ghost_count = 0


def game_intro(x_pos, x_pos2, x_pos3, x_pos4, x_pos5, y_pos, x_vel, x_vel2, walk_count, ghost_count):
    intro = True
    hit_right = False
    hit_left = False
    red_intro = False
    pink_intro = False
    blue_intro = False
    orange_intro = False
    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if (x in range(170, 540)) and (y in range(605, 640)):
                    print("Hallelujah")
                    return

        gameDisplay.fill(black)
        gameDisplay.blit(title, title_rect)
        gameDisplay.blit(text1, textpos1)
        gameDisplay.blit(text2, textpos2)
        x_pos += x_vel

        # if x_pos > display_width:
        #     x_vel *=-1
        if walk_count + 1 >= 4:
                walk_count = 0
        if ghost_count + 1 >= 3:
            ghost_count = 0

        if hit_right and hit_left is False:
            gameDisplay.blit(pacmanLeft[walk_count], (x_pos, y_pos))
            gameDisplay.blit(deadGhost[ghost_count], (x_pos - 64, y_pos))
            gameDisplay.blit(deadGhost[ghost_count], (x_pos - 96, y_pos))
            gameDisplay.blit(deadGhost[ghost_count], (x_pos - 128, y_pos))
            gameDisplay.blit(deadGhost[ghost_count], (x_pos - 160, y_pos))
            if x_pos < -64:
                hit_left = True
        elif hit_right and hit_left and x_pos2 < 600:
            x_pos2 += x_vel2
            gameDisplay.blit(redRight[ghost_count], (x_pos2, y_pos))
            gameDisplay.blit(text3, textpos3)
            # if x_pos2 > (display_width/2 + display_width/5):
            if x_pos2 > (display_width / 2) - 16:
                gameDisplay.blit(text3, textpos3)
                if red_intro is False:
                    time.sleep(1)
                red_intro = True
        elif x_pos2 > 600 and x_pos3 < 600:
            x_pos3 += x_vel2
            gameDisplay.blit(pinkRight[ghost_count], (x_pos3, y_pos))
            gameDisplay.blit(text4, textpos3)
            # if x_pos2 > (display_width/2 + display_width/5):
            if x_pos3 > (display_width / 2) - 16:
                gameDisplay.blit(text4, textpos3)
                if pink_intro is False:
                    time.sleep(1)
                pink_intro = True
        elif x_pos3 > 600 and x_pos4 < 600:
            x_pos4 += x_vel2
            gameDisplay.blit(blueRight[ghost_count], (x_pos4, y_pos))
            gameDisplay.blit(text5, textpos3)
            # if x_pos2 > (display_width/2 + display_width/5):
            if x_pos4 > (display_width / 2) - 16:
                if blue_intro is False:
                    time.sleep(1)
                blue_intro = True
        elif x_pos4 > 600 and x_pos5 <600:
            x_pos5 += x_vel2
            gameDisplay.blit(orangeRight[ghost_count], (x_pos5, y_pos))
            gameDisplay.blit(text6, textpos3)
            # if x_pos2 > (display_width/2 + display_width/5):
            if x_pos5 > (display_width / 2) - 16:
                if orange_intro is False:
                    time.sleep(1)
                orange_intro = True
        elif x_pos5 > 600:
            gameDisplay.blit(title, title_rect)
            gameDisplay.blit(text1, textpos1)
            gameDisplay.blit(text2, textpos2)
        else:
                gameDisplay.blit(pacmanRight[walk_count], (x_pos, y_pos))
                gameDisplay.blit(redRight[ghost_count], (x_pos - 64, y_pos))
                gameDisplay.blit(pinkRight[ghost_count], (x_pos - 96, y_pos))
                gameDisplay.blit(blueRight[ghost_count], (x_pos - 128, y_pos))
                gameDisplay.blit(orangeRight[ghost_count], (x_pos - 160, y_pos))
                gameDisplay.blit(powerPill, (display_width - 32, y_pos))
        if x_pos > 550:
            gameDisplay.fill(black)
            # pygame.draw.rect(gameDisplay, black, (display_width - 32, y_pos))
            hit_right = True
            x_vel *= -1
        walk_count += 1
        ghost_count += 1

        pygame.display.update()
        clock.tick(15)


game_intro(x_pos, x_pos2, x_pos3, x_pos4, x_pos5, y_pos, x_vel, x_vel2, walk_count, ghost_count)

print("HI")
game()
pygame.quit()
quit()
