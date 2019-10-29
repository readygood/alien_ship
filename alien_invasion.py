import pygame
from ship import Ship
from setting import Settings
import check_events

my_setting = Settings()

def run_game():

    pygame.init()
    ui_setting = my_setting
    screen = pygame.display.set_mode((ui_setting.screen_width,ui_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    """通过Ship类创建一个ship实例"""
    """以初始化的屏幕作为参数"""
    """让ship元素根据屏幕进行对齐"""
    ship = Ship(screen)
    bg_color = ui_setting.bg_color


    """开始主循环"""
    while True:
        # 监视键盘和鼠标事件
        check_events.check_event()

        screen.fill(bg_color)

        """使用ship的blitme方法获取image(这里是飞船)的位置信息"""
        ship.blitme()
        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()