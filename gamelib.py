import pygame
from pygame.locals import *

background = pygame.image.load("BackGround2.png")

class SimpleGame(object):
    
    BLACK = pygame.Color('black')
    BROWN = pygame.Color('brown')
    GREY = pygame.Color('grey')

    def __init__(self, title, background_image = background, window_size = (640, 480), fps = 60):
        self.title = title
        self.window_size = window_size
        self.fps = fps
        self.is_over = False
        self.background_image = background_image
        
    def __game_init(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption(self.title)
        self.font = pygame.font.SysFont("monospace",18)
        pygame.display.flip()

    def on_key_left(self, key):
        if(event.type == K_LEFT):
            pass

    def on_key_right(self, key):
        if(event.type == K_RIGHT):
            pass
    
    def on_key_space(self, key):
        if(event.type == K_SPACE):
            pass

    def over(self):
        self.is_over = True

    def __handle_events(self):
        pass
        for event in pygame.event.get():
            if event.type == QUIT:
                self.over()
        #     elif event.type == KEYLEFT:
        #         self.on_key_left(event.key)
        #     elif event.type == KEYRIGHT:
        #         self.on_key_right(event.key)

    def run(self):
        self.init()
#        global game_time
#        self.__game_init()
#        
        while not self.is_over:
#            while game_time <= 0:
#                self.__handle_events()
#            game_time -= 1
#            print game_time
            
#            self.surface.blit(background, self.window_size)
            self.surface.fill(self.BLACK)
            self.__handle_events()
            self.render(self.surface)
            self.update()
            pygame.display.update()
            self.clock.tick(self.fps)

    def is_key_pressed(self, key):
        keys_pressed = pygame.key.get_pressed()
        if key < 0 or key >= len(keys_pressed):
            return False
        return (keys_pressed[key])
        
    def update(self):
        pass

    def render(self, surface):
        pass

    def init(self):
        self.__game_init()