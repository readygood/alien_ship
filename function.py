import pygame
import sys
import ship

def check_event(ship_main):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                #ship_main.rect.centerx += 1
                ship_main.keepmoving_right = True
            # elif event.key == pygame.K_LEFT:
            #     ship_main.rect.centerx -= 1
            elif event.key == pygame.K_LEFT:
                ship_main.keepmoving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                ship_main.keepmoving_right = False
                ship_main.keepmoving_left = False

def update_screen(setting,screen_display,ship_main):

    """更新屏幕上的图像，并且换到新屏幕"""
    screen_display.fill(setting.bg_color)

    """使用ship的blitme方法获取image(这里是飞船)的位置信息"""
    ship_main.blitme()

    """最近绘制的屏幕可见"""
    pygame.display.flip()