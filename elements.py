import pygame
from pygame.locals import *

rockImage = pygame.image.load("FlintStone.png")

class ObjectRock(object):
    
    def __init__(self, radius, color, pos, speed = 3):
        (self.x, self.y) = pos
        self.radius = radius
        self.color = color
        self.speed = speed

    def render(self, surface):
        self.image = pygame.transform.scale(rockImage, (int(30), int(30)))
        pos = (self.x, self.y)
        surface.blit(self.image, pos)

    def setPos(self, player):
        if player == "CAT":
            (self.x, self.y) = (100, 290)
        elif player == "MAN":
            (self.x, self.y) = (499, 290)

    def move(self, player):
        
        if player == "CAT":
            pass
        elif player == "MAN":
            pass


        
######## Players ########

manImage = pygame.image.load("playerMan.png")
meowImage = pygame.image.load("playerCat.png")

class PlayerMan(object):

    def __init__(self, pos, size = 100, hp = 3):
        (self.posX, self.posY) = pos
        self.size = size
        self.hp = 3
        self.image = pygame.transform.scale(manImage, (int(self.size), int(self.size)))

    def move_left(self):
        self.posX -= 5

    def move_right(self):
        self.posX += 5

    def render(self, surface):
        pos = (self.posX, self.posY)
        surface.blit(self.image, pos)

class PlayerMeow(object):

    def __init__(self, pos, size = 100, hp = 3):
        (self.posX, self.posY) = pos
        self.size = size
        self.hp = 3
        self.image = pygame.transform.scale(meowImage, (int(self.size), int(self.size)))

    def move_left(self):

        self.posX -= 5

    def move_right(self):
        self.posX += 5

    def render(self, surface):
        pos = (self.posX, self.posY)
        surface.blit(self.image, pos)
