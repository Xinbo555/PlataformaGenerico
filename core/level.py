import os.path

import pygame.image

import settings
from settings import *

class World:
    def __init__(self):
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        grass_path = os.path.join('assets','images','background','grass.png')
        self.grass_image = pygame.image.load(grass_path).convert_alpha()
        self.grass_image = pygame.transform.scale(self.grass_image,(GRASS_SIZE,GRASS_SIZE))

    def draw(self,screen):

        for i in range(0,self.width,settings.GRASS_SIZE):
            for j in range(0,self.height,settings.GRASS_SIZE):
                screen.blit(self.grass_image,(i,j))


