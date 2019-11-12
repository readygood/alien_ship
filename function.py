import pygame
import sys
from bullet import Bullet

def check_event_down(event,ui_setting,screend,ship_main,bullets):

    if event.key == pygame.K_RIGHT:
        # ship_main.rect.centerx += 1
        ship_main.keepmoving_right = True
    # elif event.key == pygame.K_LEFT:
    #     ship_main.rect.centerx -= 1
    elif event.key == pygame.K_LEFT:

        ship_main.keepmoving_left = True

    elif event.key == pygame.K_UP:

        ship_main.keepmoving_up = True

    elif event.key == pygame.K_DOWN:

        ship_main.keepmoving_down = True

    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(ui_setting,screend,ship_main)
        bullets.add(new_bullet)

def check_event_up(event,ship_main):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:

        ship_main.keepmoving_right = False
        ship_main.keepmoving_left = False
        ship_main.keepmoving_up = False
        ship_main.keepmoving_down = False

def check_event(ui_setting,screend,ship_main,bullets):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_event_down(event,ui_setting,screend,ship_main,bullets)
        #     if event.key == pygame.K_RIGHT:
        #         #ship_main.rect.centerx += 1
        #         ship_main.keepmoving_right = True
        #     # elif event.key == pygame.K_LEFT:
        #     #     ship_main.rect.centerx -= 1
        #     elif event.key == pygame.K_LEFT:
        #         ship_main.keepmoving_left = True
        #
        #     elif event.key == pygame.K_UP:
        #         ship_main.keepmoving_up = True
        #
        #     elif event.key == pygame.K_DOWN:
        #         ship_main.keepmoving_down = True

        elif event.type == pygame.KEYUP:
            check_event_up(event,ship_main)
            # if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            #     ship_main.keepmoving_right = False
            #     ship_main.keepmoving_left = False
            #     ship_main.keepmoving_up = False
            #     ship_main.keepmoving_down = False


def update_screen(setting,screen_display,ship_main,bullets):

    """更新屏幕上的图像，并且换到新屏幕"""
    screen_display.fill(setting.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    """使用ship的blitme方法获取image(这里是飞船)的位置信息"""
    ship_main.blitme()

    """最近绘制的屏幕可见"""
    pygame.display.flip()