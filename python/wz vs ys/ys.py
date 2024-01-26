import pygame
import random

class Xiaog:
    def __init__(self):
        self.image = pygame.image.load('material\images\ys_xg.jpg').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.top = 100
        self.rect.left = 250

class FUFU:
    def __init__(self):
        self.image = pygame.image.load('material\images\ys_fufu.jpg').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.top = 100
        self.rect.left = 250

class Naxd:
    def __init__(self):
        self.image = pygame.image.load('material\images\ys_nxd.jpg').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.top = 100
        self.rect.left = 250

class Kel:
    def __init__(self):
        self.image = pygame.image.load('material\images\ys_kl.jpg').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.top = 100
        self.rect.left = 250