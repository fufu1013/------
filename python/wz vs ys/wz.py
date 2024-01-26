import pygame
import random

class Sunsx(pygame.sprite.Sprite):
    def __init__(self):
        super(Sunsx,self).__init__()
        self.image = pygame.image.load('material\images\wz_ssx.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.top = 80
        self.rect.left = 250

class Yao(pygame.sprite.Sprite):
    def __init__(self):
        super(Yao,self).__init__()
        self.image = pygame.image.load('material\images\wz_y.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.top = 80
        self.rect.left = 250

class Zhugl(pygame.sprite.Sprite):
    def __init__(self):
        super(Zhugl,self).__init__()
        self.image = pygame.image.load('material\images\wz_zgl.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.top = 80
        self.rect.left = 250

class Sunc(pygame.sprite.Sprite):
    def __init__(self):
        super(Sunc,self).__init__()
        self.image = pygame.image.load('material\images\wz_sc.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.top = 80
        self.rect.left = 250

class Money(pygame.sprite.Sprite):
    def __init__(self):
        super(Money,self).__init__()
        self.image=pygame.image.load('material\images\money.png').convert_alpha()
        self.rect=self.image.get_rect()


