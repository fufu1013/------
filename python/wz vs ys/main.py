import pygame,sys,random
from pygame.locals import *
from wz import *
from ys import *
from bullet import *

pygame.init()

size = (1200, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("王者大战原神")
backgroundImg = pygame.image.load('material/images/background1.jpg').convert_alpha()
sunbackImg = pygame.image.load('material/images/money22.png').convert_alpha()
bankimg=pygame.image.load('material/images/bank.png').convert_alpha()
ssxseed=pygame.image.load('material/images/ssxseed.png').convert_alpha()
yseed=pygame.image.load('material/images/yseed.png').convert_alpha()
scseed=pygame.image.load('material/images/scseed.png').convert_alpha()
yaoimg=pygame.image.load('material\images\wz_y.png').convert_alpha()
ssximg=pygame.image.load('material\images\wz_ssx.png').convert_alpha()
scimg=pygame.image.load('material\images\wz_sc.png').convert_alpha()
winimg=pygame.image.load('material\images\win.png').convert_alpha()
loseimg=pygame.image.load('material\images\lose.png').convert_alpha()

score='500'
myfont = pygame.font.SysFont('arial', 20)
txtImg = myfont.render("500", True, (0, 0, 0))

nxdlist = pygame.sprite.Group()
fufulist = pygame.sprite.Group()
moneylist = pygame.sprite.Group()
yaolist = pygame.sprite.Group()
sclist = pygame.sprite.Group()
ssxlist = pygame.sprite.Group()
wzlist = pygame.sprite.Group()
zdlist = pygame.sprite.Group()

index = 1
clock = pygame.time.Clock()
choose = 0
fufucount=0
nxdcount=0
fufudie=[0]
nxddie=[0]

GENERATOR_SUN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(GENERATOR_SUN_EVENT, 5000)

GENERATOR_ZOMBIE_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(GENERATOR_ZOMBIE_EVENT, 5000)

GENERATOR_PEASHOOTER_EVENT = pygame.USEREVENT + 3
pygame.time.set_timer(GENERATOR_PEASHOOTER_EVENT, 2000)

GENERATOR_FLAGZOMBIE_EVENT = pygame.USEREVENT + 4
pygame.time.set_timer(GENERATOR_FLAGZOMBIE_EVENT, 20000)

while True:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type == GENERATOR_SUN_EVENT:
            if len(yaolist) > 0:
                for yao in yaolist:
                    money = Money(yao.rect)
                    moneylist.add(money)
        if event.type == GENERATOR_PEASHOOTER_EVENT:
            if len(ssxlist) > 0:
                for ssx in ssxlist:
                    zd = ssxzd(ssx.rect,size)
                    zdlist.add(zd)
        if event.type == GENERATOR_ZOMBIE_EVENT and fufucount<10:
            fufu=FUFU()
            fufucount+=1
            fufulist.add(fufu)
        if event.type == GENERATOR_FLAGZOMBIE_EVENT and 3:
            nxd=Naxd()
            nxdcount+=1
            nxdlist.add(nxd)
        if event.type == MOUSEBUTTONDOWN:
            mouse_pressed = pygame.mouse.get_pressed()
            if mouse_pressed[2] and choose != 0:
                if choose == 1:
                    choose = 0
                if choose == 2:
                    choose = 0
                if choose == 3:
                    choose = 0
            if mouse_pressed[0]:
                (x,y) = pygame.mouse.get_pos()
                if 330 <= x <= 380 and 10 <= y <= 80:
                    choose = 1
                elif 380 < x <= 430 and 10 <= y <= 80:
                    choose = 2
                elif 430 < x <= 480 and 10 <= y <= 80:
                    choose = 3
                elif 250 < x < 1200 and 70 < y < 600:
                    if choose == 1:
                        yao=Yao()
                        yao.rect.top = y
                        yao.rect.left = x
                        yaolist.add(yao)
                        choose = 0
                        score = int(score)
                        score -= 50
                        myfont = pygame.font.SysFont('arial', 20)
                        txtImg = myfont.render(str(score), True, (0, 0, 0))
                    if choose == 2:
                        ssx = Sunsx()
                        ssx.rect.top = y
                        ssx.rect.left = x
                        ssxlist.add(ssx)
                        choose = 0
                        score = int(score)
                        score -= 100
                        myfont = pygame.font.SysFont('arial', 20)
                        txtImg = myfont.render(str(score), True, (0, 0, 0))
                    if choose == 3:
                        sc=Sunc()
                        sc.rect.top = y
                        sc.rect.left = x
                        sclist.add(sc)
                        choose = 0
                        score = int(score)
                        score -= 50
                        myfont = pygame.font.SysFont('arial', 20)
                        txtImg = myfont.render(str(score), True, (0, 0, 0))

                for money in moneylist:
                    if money.rect.collidepoint((x,y)):
                        money.is_click = True
                        score = int(score) + 50
                        myfont = pygame.font.SysFont('arial', 20)
                        txtImg = myfont.render(str(score), True, (0, 0, 0))
    for fufu in fufulist:
        for sc in sclist:
            if pygame.sprite.collide_mask(fufu, sc):
                fufu.ismeetwz = True
                sc.ys.add(fufu)
    for nxd in nxdlist:
        for sc in sclist:
            if pygame.sprite.collide_mask(nxd, sc):
                nxd.ismeetwz = True
                sc.ys.add(nxd)
    for fufu in fufulist:
        for ssx in ssxlist:
            if pygame.sprite.collide_mask(fufu, ssx):
                fufu.ismeetwz = True
                ssx.ys.add(fufu)
    for nxd in nxdlist:
        for ssx in ssxlist:
            if pygame.sprite.collide_mask(nxd, ssx):
                nxd.ismeetwz = True
                ssx.ys.add(nxd)
    for fufu in fufulist:
        for yao in yaolist:
            if pygame.sprite.collide_mask(fufu, yao):
                fufu.ismeetwz = True
                yao.ys.add(fufu)
    for nxd in nxdlist:
        for yao in ssxlist:
            if pygame.sprite.collide_mask(nxd, yao):
                nxd.ismeetwz = True
                yao.ys.add(nxd)
    for zd in zdlist:
        for fufu in fufulist:
            if pygame.sprite.collide_mask(zd, fufu):
                fufu.energy -= 1
                zdlist.remove(zd)
    for zd in zdlist:
        for nxd in nxdlist:
            if pygame.sprite.collide_mask(zd, nxd):
                nxd.energy -= 1
                zdlist.remove(zd)


    screen.blit(backgroundImg, (0, 0))
    screen.blit(bankimg, (250, 0))
    screen.blit(sunbackImg, (258, 2))
    screen.blit(txtImg, (270, 60))
    screen.blit(yseed, (330, 10))
    screen.blit(ssxseed, (380, 10))
    screen.blit(scseed, (430, 10))

    (x, y) = pygame.mouse.get_pos()
    if choose == 1:
        screen.blit(yaoimg, (x, y))
    if choose == 2:
        screen.blit(ssximg, (x, y))
    if choose == 3:
        screen.blit(scimg, (x, y))

    zdlist.update(index)
    zdlist.draw(screen)
    fufulist.update(index,fufudie)
    fufulist.draw(screen)
    nxdlist.update(index,nxddie)
    nxdlist.draw(screen)
    moneylist.update()
    moneylist.draw(screen)
    yaolist.update()
    yaolist.draw(screen)
    sclist.update()
    sclist.draw(screen)
    ssxlist.update()
    ssxlist.draw(screen)

    if fufudie[0]==10 and nxddie[0]==3:
        screen.blit(winimg, (400, 200))

    for fufu in fufulist:
        if fufu.rect.left==150:
            screen.blit(loseimg, (400, 200))
    for nxd in nxdlist:
        if nxd.rect.left==150:
            screen.blit(loseimg, (400, 200))

    index += 1
    pygame.display.update()
