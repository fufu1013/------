import pygame
import random

class FUFU(pygame.sprite.Sprite):
    def __init__(self):
        super(FUFU, self).__init__()
        self.image = pygame.image.load('material/images/ys_fufu1.png').convert_alpha()
        self.images = [pygame.image.load('material/images/ys_fufu{}.png'.format(i)).convert_alpha() for i in
                       range(1, 3)]
        self.rect = self.images[0].get_rect()
        self.rect.top = 100 + random.randrange(0, 4) * 125
        # print(self.rect.top)
        self.rect.left = 1000
        self.speed = 1
        self.energy = 6
        self.ismeetwz = False
        self.isAlive = True

    def update(self, index,die):
        if self.energy>0:
            if index % 20 >= 0 and index % 20 <= 9:
                self.image = self.images[0]
            else:
                self.image = self.images[1]
            if self.rect.left > 150 and not self.ismeetwz:
                self.rect.left -= self.speed
        else:
            self.kill()
            die[0]+=1
            self.isAlive = False

class Naxd(pygame.sprite.Sprite):
    def __init__(self):
        super(Naxd, self).__init__()
        self.image = pygame.image.load('material/images/ys_nxd1.png').convert_alpha()
        self.images = [pygame.image.load('material/images/ys_nxd{}.png'.format(i)).convert_alpha() for i in
                       range(1, 3)]
        self.rect = self.images[0].get_rect()
        self.rect.top = 100 + random.randrange(0, 4) * 125
        # print(self.rect.top)
        self.rect.left = 1000
        self.speed = 1
        self.energy=10
        self.ismeetwz = False
        self.isAlive = True

    def update(self, index,die):
        if self.energy > 0:
            if index % 20 >= 0 and index % 20 <= 9:
                self.image = self.images[0]
            else:
                self.image = self.images[1]
            if self.rect.left > 150 and not self.ismeetwz:
                self.rect.left -= self.speed
        else:
            self.kill()
            die[0]+=1
            self.isAlive = False