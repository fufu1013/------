import pygame
import random

fufu=0
class Sunsx(pygame.sprite.Sprite):
    def __init__(self):
        super(Sunsx,self).__init__()
        self.image = pygame.image.load('material\images\wz_ssx.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.ys = set()
        self.energy = 8 * 15

    def update(self):
        for ys in self.ys:
            if not ys.isAlive:
                continue
            self.energy -= 1
            if self.energy <= 0:
                for ys in self.ys:
                    ys.ismeetwz = False
                self.kill()

class Yao(pygame.sprite.Sprite):
    def __init__(self):
        super(Yao,self).__init__()
        self.image = pygame.image.load('material\images\wz_y.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.ys = set()
        self.energy = 8 * 15

    def update(self):
        for ys in self.ys:
            if not ys.isAlive:
                continue
            self.energy -= 1
            if self.energy <= 0:
                for ys in self.ys:
                    ys.ismeetwz = False
                self.kill()

class Sunc(pygame.sprite.Sprite):
    def __init__(self):
        super(Sunc,self).__init__()
        self.image = pygame.image.load('material\images\wz_sc.png').convert_alpha()
        self.image1 = pygame.image.load('material\images\wz_sc1.png').convert_alpha()
        self.image2 = pygame.image.load('material\images\wz_sc2.png').convert_alpha()
        self.image3 = pygame.image.load('material\images\wz_sc3.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.ys = set()
        self.energy = 32 * 15
    def update(self):
        for ys in self.ys:
            if not ys.isAlive:
                continue
            self.energy -= 1
            if self.energy <= 0:
                for ys in self.ys:
                    ys.ismeetwz = False
                self.kill()

        if self.energy == 64 * 15:
            self.image = self.image
        elif 48 * 15 <= self.energy < 64 * 15:
            self.image = self.image1
        elif 24 * 15 <= self.energy < 48 * 15:
            self.image = self.image2
        else:
            self.image = self.image3

class Money(pygame.sprite.Sprite):
    def __init__(self):
        super(Money,self).__init__()
        self.image=pygame.image.load('material\images\money.png').convert_alpha()
        self.rect=self.image.get_rect()