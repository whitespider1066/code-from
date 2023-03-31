# resources.py
# Author: Darren Christie
# Last updated: 20/3/2023
# Description: This is a demo program to demonstate the use of sprites in
import pygame
import sys
import os
from pygame.locals import *

def loadimage(name,colourkey=None):
    fullname = os.path.join('images',name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert()
    if colourkey is not None:
        if colourkey is -1:
            colourkey = image.get_at((0,0))
        image.set_colorkey(colourkey, RLEACCEL)
    return image, image.get_rect()
