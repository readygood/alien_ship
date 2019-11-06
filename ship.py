import pygame
import setting

class Ship():
    def __init__(self,setting,screen):

        self.screen = screen
        self.setting = setting

        """get_rect()方法可以获取屏幕和元素的矩阵信息"""
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()


        """将屏幕的中心点坐标赋值给元素的中心点"""
        """再将屏幕的底部坐标赋值给元素底部"""
        """这样ship元素就在屏幕底部中心了"""
        self.rect.centerx = self.screen_rect.centerx
        #self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom

        """移动标志(flag)"""
        self.keepmoving_right = False
        self.keepmoving_left = False
        self.keepmoving_up = False
        self.keepmoving_down = False

        """定义飞船移动像素的属性"""
        self.move_px = float(self.rect.centerx)
        self.move_py = float(self.rect.centery)


    def blitme(self):
        self.screen.blit(self.image,self.rect)

    """为Ship类定义一个方法,可以使飞船上下左右移动"""
    def update(self):
        # if self.keepmoving_right:
        #     self.rect.centerx += 2
        # elif self.keepmoving_left:
        #     self.rect.centerx -= 2
        # elif self.keepmoving_up:
        #     self.rect.centery -= 2
        # elif self.keepmoving_down:
        #     self.rect.centery += 2
        #
        # if self.keepmoving_right and self.rect.right < self.screen_rect.right:
        #     self.rect.centerx += 2

        if self.keepmoving_right:
            self.move_px += self.setting.ship_speed_factor

        if self.keepmoving_left:
            self.move_px -= self.setting.ship_speed_factor

        if self.keepmoving_up:
            self.move_py -= self.setting.ship_speed_factor

        if self.keepmoving_down:
            self.move_py += self.setting.ship_speed_factor

        self.rect.centerx = self.move_px
        self.rect.centery = self.move_py