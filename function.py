import pygame
import sys

def check_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(setting,screen_display,ship_main):

    """更新屏幕上的图像，并且换到新屏幕"""
    screen_display.fill(setting.bg_color)

    """使用ship的blitme方法获取image(这里是飞船)的位置信息"""
    ship_main.blitme()


    """最近绘制的屏幕可见"""
    pygame.display.flip()