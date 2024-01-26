import pygame

pygame.init()
screen = pygame.display.set_mode((500,300))
pygame.display.set_caption('c语言中文网')
# 获取以毫秒为单位的时间
t = pygame.time.get_ticks() #该时间指的从pygame初始化后开始计算，到调用该函数为止
t1 =pygame.time.delay(3000) #暂停游戏3000毫秒
print(t1)
#暂停t1时间后，加载图片
image_surface = pygame.image.load("C:/Users/Administrator/Desktop/c-net.png")
#创建时钟对象（控制游戏的FPS）
clock = pygame.time.Clock()
while True:

    #通过时钟对象，指定循环频率，每秒循环60次
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.blit(image_surface,(0,0))
    pygame.display.update()