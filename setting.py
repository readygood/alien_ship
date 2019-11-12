class Settings():
    def __init__(self,screen_width=1600,screen_height=800,bg_color=(230,230,230)):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.bg_color = bg_color

        """飞船移动速度设置"""

        self.ship_speed_factor = 1.5


        """子弹设置"""
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60