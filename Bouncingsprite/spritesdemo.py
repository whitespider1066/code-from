# spritesdemo.py
# Author: Darren Christie
# Last updated: 20/3/2023
# Description: This is a demo program to demonstate the use of sprites in
# pygame.
import pygame
from pygame.locals import *

import player

# initialise pygame
pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)

# initialise our screen
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 600
#SCREEN_FLAGS = FULLSCREEN
#screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),SCREEN_FLAGS)
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Sprite Demo')

# other game initialisation here
# such as loading graphics, sfx, music, etc
FPS = 60 # sets our frame rate for the game

# start our real time clock
clock = pygame.time.Clock()

# create our player object
player = player.Player(40,10,(SCREEN_WIDTH,SCREEN_HEIGHT))

# create our sprite group
allsprites = pygame.sprite.RenderPlain((player))

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

    # call all the sprite updates
    allsprites.update()

    # update display
    screen.fill(WHITE)
    allsprites.draw(screen)
    pygame.display.flip()

# leave our game
pygame.quit()
exit()
