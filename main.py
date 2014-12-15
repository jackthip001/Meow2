import pygame
from pygame.locals import *
import pygame.mixer

from gamelib import SimpleGame
from elements import ObjectRock, PlayerMan, PlayerMeow

class MeowGame(SimpleGame):
    
    # hited = pygame.mixer.Sound()

    WHITE = pygame.Color('white')
    
    def __init__(self):
        super(MeowGame, self).__init__('Meow')
        self.man = PlayerMan(pos = (500, 320))
        self.cat = PlayerMeow(pos = (50, 320))
        self.rock_man = ObjectRock(player = "MAN")
        self.rock_cat = ObjectRock(player = "CAT")
        self.gamerun = True
        pygame.mixer.init()
        self.soundMan = pygame.mixer.Sound("LeeSinUlti.ogg.opus")
        self.soundCat = pygame.mixer.Sound("GnarA.ogg.opus")

    def init(self):
        super(MeowGame, self).init()
        self.render_hp()

    def update(self):
        # if self.gamerun:
        self.render_hp()

        if self.is_key_pressed(K_LEFT):
            self.man.move_left()
        elif self.is_key_pressed(K_RIGHT):
            self.man.move_right()

        if self.is_key_pressed(K_SPACE):
            self.rock_man.setPos(self.man.posX)
            self.rock_man.update()
            self.man.is_round_true()

        if self.is_key_pressed(K_a):
            self.cat.move_left()
        elif self.is_key_pressed(K_d):
            self.cat.move_right()

        if self.is_key_pressed(K_LSHIFT):
            self.rock_cat.setPos(self.cat.posX)
            self.rock_cat.update()
            self.cat.is_round_true()

        if not self.rock_man.pressed:
            self.rock_man.move()
            if self.rock_man.pressed:
                self.rock_man.reset()

        if not self.rock_cat.pressed:
            self.rock_cat.move()
            if self.rock_cat.pressed:
                self.rock_cat.reset()

        self.catHited()
        self.manHited()

        if self.cat.hp == 0 or self.man.hp == 0:
            self.gamerun = False

        # elif self.is_key_pressed(K_r):
            # self.__init__()

    def manHited(self):
        if self.man.posX + self.man.size >= self.rock_cat.x > self.man.posX:
            if self.rock_cat.y >= self.man.posY:
                self.soundMan.play()
                self.rock_cat.setPos(self.cat.posX)
                self.rock_cat.reset()
                self.rock_cat.pressed = True
                self.man.hp -= 1
                print "man hp : " + str(self.man.hp)

    def catHited(self):
        if self.cat.posX < self.rock_man.x <= self.cat.posX + self.cat.size:
            if self.rock_man.y >= self.cat.posY:
                self.soundCat.play()
                self.rock_man.setPos(self.man.posX)
                self.rock_man.reset()
                self.rock_man.pressed = True
                self.cat.hp -= 1
                print "cat hp : " + str(self.cat.hp)

    def on_key_up(self, key):
        if key == K_SPACE:
            self.rock_man.pressed = False
        if key == K_LSHIFT:
            self.rock_cat.pressed = False

    def render(self, surface):
        if not self.rock_cat.pressed:
            self.rock_cat.render(surface)
        if not self.rock_man.pressed:
            self.rock_man.render(surface)
        self.man.render(surface)
        self.cat.render(surface)
        surface.blit(self.hpCat, (10, 10))
        surface.blit(self.hpMan, (550, 10))

    def render_hp(self):
        self.hpCat = self.font.render("HP : %d" % self.cat.hp, 0, MeowGame.WHITE)
        self.hpMan = self.font.render("HP : %d" % self.man.hp, 0, MeowGame.WHITE)
    
def main():
    game = MeowGame()
    game.run()

if __name__ == '__main__':
    main()