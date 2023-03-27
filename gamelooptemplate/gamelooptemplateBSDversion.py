# gamelooptemplate.py
# Author: Darren Christie
# Last updated: 20/3/2023
# Description: This is a basic template for a game loop that can be used
# for the basis of writing a game in pygame.
# This code is released under the "New BSD License"
# https://opensource.org/license/bsd-3-clause/

import pygame
from pygame.locals import *

# initialise pygame
pygame.init()

# initialise our screen
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 600
#SCREEN_FLAGS = FULLSCREEN
#screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),SCREEN_FLAGS)
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Game Loop Template')

# other game initialisation here
# such as loading graphics, sfx, music, etc
FPS = 30

# start our real time clock
clock = pygame.time.Clock()

# our game loop
running = True

while running:

    # computes how many milliseconds have passed since the previous call
    clock.tick(FPS) 

    # handle all the events in our game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # exit our game
            running = False
        elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            # key pressed, let's find out which one
            if event.key == K_ESCAPE:
                running = False


    # update display
    pygame.display.update()

# leave our game
pygame.quit()
exit()
