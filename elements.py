import pygame
from pygame.locals import *
from math import *

rockImage = pygame.image.load("FlintStone.png")

class ObjectRock(object):

    def __init__(self, player, speed = 3):
        (self.x, self.y) = (-200, -200)
        self.speed = speed
        self.pressed = False
        self.checkDistance = 0
        self.player = player
        self.force = 0

    def render(self, surface):
        self.image = pygame.transform.scale(rockImage, (int(30), int(30)))
        pos = (self.x, self.y)
        surface.blit(self.image, pos)

    def update(self):
        print "rock update"
        self.force += 5

    def reset(self):
        self.force = 0
        self.checkDistance = 0

    def setPos(self, posX):
        if self.player == "CAT":
            (self.x, self.y) = (posX + 50, 290)
        if self.player == "MAN":
            (self.x, self.y) = (posX, 290)

    def move(self):
        print "rock move"
        if self.checkDistance < self.force * 4:
            self.moveY()
            if self.player == "CAT":
                self.moveX_cat()
            if self.player == "MAN":
                self.moveX_man()
        self.checkDistance += self.speed
        if self.y >= 420:
            self.reset()
            self.pressed = True

    def moveX_man(self):
        self.x -= self.speed

    def moveX_cat(self):
        self.x += self.speed

    def moveY(self, theta = pi/3):
        speedY = tan(theta) * self.speed
        if self.checkDistance < self.force/2:
            self.y -= speedY
        elif self.y <= 420:
            self.y += speedY

        
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
        self.canMove = True
   
    def is_round_false(self):
        self.round = False

    def is_round_true(self):
        self.round = True

    def move_left(self):
        self.chPosition()
        if self.canMove:
            self.posX -= 5

    def move_right(self):
        self.posX += 5

    def chPosition(self):
        if self.posX <= 340:
            self.canMove = False
        else:
            self.canMove = True
  
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
        self.canMove = True

    def is_round_false(self):
        self.round = False

    def is_round_true(self):
        self.round = True

    def move_left(self):
        self.posX -= 5

    def move_right(self):
        self.chPosition()
        if self.canMove:
            self.posX += 5

    def chPosition(self):
        if self.posX >= 210:
            self.canMove = False
        else:
            self.canMove = True

    def render(self, surface):
        pos = (self.posX, self.posY)
        surface.blit(self.image, pos)
