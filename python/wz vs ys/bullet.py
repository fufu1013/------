import pygame
import random

class ssxzd(pygame.sprite.Sprite):
    def __init__(self,rect,bg_size):
        super(ssxzd, self).__init__()
        self.image = pygame.image.load("material/images/zd.png")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = rect[0] + 45, rect[1]
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 5

    def update(self, *args):
        if self.rect.right < self.width:
            self.rect.left += self.speed
        else:
            self.kill()

class Money(pygame.sprite.Sprite):
    def __init__(self, rect):
        super(Money, self).__init__()
        self.image = pygame.image.load('material/images/money.png').convert_alpha()
        self.rect = self.image.get_rect()
        offsetTop = random.randint(-50, 50)
        offsetLeft = random.randint(-50, 50)

        self.rect.top = rect.top + offsetTop
        self.rect.left = rect.left + offsetLeft
        self.is_click = False
        self.times = 5
        self.scale = 10

    def update(self):
        if self.is_click:
            self.kill()