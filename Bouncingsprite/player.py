# player.py
# Author: Darren Christie
# Last updated: 20/3/2023
# Description: this is the class definition for a player controlled object
import pygame

import resources

class Player(pygame.sprite.Sprite):
    def __init__(self, startx,starty,screensize):
        # call the sprite initializer
        pygame.sprite.Sprite.__init__(self)
        # load our image
        self.image, self.rect = resources.loadimage('Idle.png',-1)
        # set the start position of the sprite
        self.rect.topleft = startx,starty
        # needed to detect if we have hit the edge of the screen
        self.screenwidth = screensize[0]
        self.screenheight = screensize[1]

    def update(self):
        # has the sprite hit the edge of the screen?
        if self.rect.left < (self.screenwidth - self.rect.w):
            self.rect.x += 6
            
        
