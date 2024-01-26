#导入所需的模块
import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((400,400))
screen.fill((156,156,156))

pygame.display.set_caption('hello world')

surface_image =pygame.image.load("图片路径")
f = pygame.font.Font('C:/Windows/Fonts/simhei.ttf',50)
text = f.render("C语言中文网",True,(255,0,0),(0,0,0))
textRect =text.get_rect()
textRect.center = (200,200)
screen.blit(text,textRect)

# 固定代码段，实现点击"X"号退出界面的功能，几乎所有的pygame都会使用该段代码
while True:
    # 循环获取事件，监听事件状态
    for event in pygame.event.get():
        # 判断用户是否点了"X"关闭按钮,并执行if代码段
        if event.type == pygame.QUIT:
            #卸载所有模块
            pygame.quit()
            #终止程序，确保退出程序
            sys.exit()
    pygame.display.flip() #更新屏幕内容


#刷新界面显示
pygame.display.flip()

pygame.display.update()