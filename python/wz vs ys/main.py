import pygame,sys,random
from pygame.locals import *
from wz import *
from ys import *

pygame.init()

size = (1200, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("王者大战原神")
backgroundImg = pygame.image.load('material/images/background1.jpg').convert_alpha()

ssx=Sunsx()

clock = pygame.time.Clock()
while True:
    clock.tick(15)

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(backgroundImg, (0, 0))
    screen.blit(ssx.image, ssx.rect)

    pygame.display.update()

