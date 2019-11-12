import pygame
from ship import Ship
from setting import Settings
import function as gf

def run_game():

    """初始化"""
    pygame.init()

    """根据Setting类创建一个实例"""
    ui_setting = Settings(bg_color=(225,225,225))

    """定义屏幕"""
    screend = pygame.display.set_mode((ui_setting.screen_width,ui_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    """通过Ship类创建一个ship实例"""
    """以初始化的屏幕作为参数"""
    """让ship元素根据屏幕进行对齐"""

    ship = Ship(ui_setting,screend)

    """开始主循环"""
    while True:

        """监控事件和键盘"""
        gf.check_event(ship)

        """使用ship中的update方法"""
        ship.update()

        """更新屏幕上的图像"""
        gf.update_screen(ui_setting,screend,ship)

run_game()