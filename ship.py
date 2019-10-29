import pygame
class Ship():
    def __init__(self,screen):
        self.screen = screen

        """get_rect()方法可以获取屏幕和元素的矩阵信息"""
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()


        """将屏幕的中心点坐标赋值给元素的中心点"""
        """再将屏幕的底部坐标赋值给元素底部"""
        """这样ship元素就在屏幕底部中心了"""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image,self.rect)