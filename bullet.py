import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    """创建一个对飞船发射的子弹进行管理的类"""

    def __init__(self,settingss,screen,ship):
        """在飞船所处的位置创建一个子弹对象"""

        """继承Sprite"""
        super(Bullet,self).__init__()

        """定义属性screen"""
        self.screen = screen

        """在(0,0)处创建一个表示子弹的矩形，再设置正确位置"""

        """定义子单属性
        通过settings中的属性bullet_width和bullet_height来创建一个子弹
        然后调整子弹位置(初始位置)"""
        self.rect = pygame.Rect(0,0,settingss.bullet_width,settingss.bullet_height)

        """飞船的x轴坐标传递给子弹"""
        self.rect.centerx = ship.rect.centerx

        """飞船的顶部坐标传递给子弹"""
        self.rect.top = ship.rect.top

        """定义子弹的初始y坐标位置"""
        self.y = float(self.rect.y)

        self.color = settingss.bullet_color
        self.speed = settingss.bullet_speed_factor

    def update(self):
        self.y -= self.speed

        self.rect.y = self.y

    def draw_bullet(self):

        pygame.draw.rect(self.screen,self.color,self.rect)