import pygame
from pygame.locals import *
from math import *

rockImage = pygame.image.load("FlintStone.png")

class ObjectRock(object):

    def __init__(self, player, speed = 3):
        # (self.x, self.y) = pos
        self.speed = speed
        self.space = False
        self.checkDistance = 0
        self.player = player
        self.force = 0

    def render(self, surface):
        self.image = pygame.transform.scale(rockImage, (int(30), int(30)))
        pos = (self.x, self.y)
        surface.blit(self.image, pos)

    def update(self):
        self.force += 5

    def reset(self):
        self.force = 0
        self.checkDistance = 0

    def setPos(self, posX):
        if self.player == "CAT":
            (self.x, self.y) = (posX + 50, 290)
        if self.player == "MAN":
            (self.x, self.y) = (posX - 1, 290)

    def move(self):
        if self.checkDistance < self.force:
            self.moveY()
            if self.player == "CAT":
                self.moveX_cat()
            if self.player == "MAN":
                self.moveX_man()
            self.checkDistance += speed
        else:
            self.reset()

    def moveX_man(self):
        self.x -= self.speed

    def moveX_cat(self):
        self.x += self.speed

    def moveY(self, theta = pi/4):
        speedY = math.tan(theta) * self.speed
        if self.x < force/2:
            self.y += speedY
        else:
            self.y -= speedY

        
######## Players ########

manImage = pygame.image.load("playerMan.png")
meowImage = pygame.image.load("playerCat.png")


class PlayerMan(object):

    def __init__(self, pos, size = 100, hp = 3):
        (self.posX, self.posY) = pos
        self.size = size
        self.hp = 3
        self.image = pygame.transform.scale(manImage, (int(self.size), int(self.size)))
        self.round = False
   
    def is_round_false(self):
        self.round = False

    def is_round_true(self):
        self.round = True

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
        self.round = False

    def is_round_false(self):
        self.round = False

    def is_round_true(self):
        self.round = True

    def move_left(self):
        self.posX -= 5

    def move_right(self):
        self.posX += 5

    def render(self, surface):
        pos = (self.posX, self.posY)
        surface.blit(self.image, pos)
