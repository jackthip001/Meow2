import pygame
from pygame.locals import *

from gamelib import SimpleGame
from elements import ObjectRock, PlayerMan, PlayerMeow

class MeowGame(SimpleGame):
    
    WHITE = pygame.Color('white')
    
    def __init__(self):
        super(MeowGame, self).__init__('Meow')
        self.man = PlayerMan(pos = (500, 320))
        self.cat = PlayerMeow(pos = (50, 320))
        self.rock_man = ObjectRock(player = "MAN")
        self.rock_cat = ObjectRock(player = "CAT")

    def init(self):
        super(MeowGame, self).init()

    def update(self):
        if self.is_key_pressed(K_LEFT):
            self.man.move_left()
        elif self.is_key_pressed(K_RIGHT):
            self.man.move_right()

        if self.is_key_pressed(K_SPACE):
            self.rock_man.update()
            self.man.is_round_true()

        if self.is_key_pressed(K_a):
            self.cat.move_left()
        elif self.is_key_pressed(K_d):
            self.cat.move_right()
        
        if self.is_key_pressed(K_LSHIFT):
            self.rock_cat.update()
            self.cat.is_round_true()


    def render(self, surface):
        if self.cat.round == True:
            self.rock_cat.setPos(self.cat.posX)
            self.rock_cat.render(surface)
        if self.man.round == True:
            self.rock_man.setPos(self.man.posX)
            self.rock_man.render(surface)
        self.man.render(surface)
        self.cat.render(surface)

def main():
    game = MeowGame()
    game.run()

if __name__ == '__main__':
    main()