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
        self.rect.topleft = startx,starty
        self.screenwidth = screensize[0]
        self.screenheight = screensize[1]
        self.xspeed = 6
        self.yspeed = 6
        print(self.screenwidth)

    def update(self):
        self.rect.x += self.xspeed;
        if self.rect.left > (self.screenwidth - self.rect.w) or self.rect.left < 0:
            self.xspeed *= -1
        self.rect.y += self.yspeed;
        if self.rect.top > (self.screenheight - self.rect.h) or self.rect.top < 0:
            self.yspeed *= -1
            
        
