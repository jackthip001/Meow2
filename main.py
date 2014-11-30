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
        self.rock = ObjectRock(radius = 5, pos = (100, 290),color = MeowGame.WHITE)

    def init(self):
        super(MeowGame, self).init()

    def update(self):
        if self.is_key_pressed(K_LEFT):
            self.cat.move_left()
        elif self.is_key_pressed(K_RIGHT):
            self.cat.move_right()

    def render(self, surface):
        self.rock.render(surface)
        self.man.render(surface)
        self.cat.render(surface)

def main():
    game = MeowGame()
    game.run()

if __name__ == '__main__':
    main()