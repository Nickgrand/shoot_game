class Settings:
    """保存所有设置"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        # self.bg_color = (105, 7, 90)

        # 飞船设置
        self.ship_speed_factor = 0.5
        self.ship_limit = 3

        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_speed_factor = 0.1
        self.bullets_allowed = 10

        # 外星人设置
        self.alien_speed_factor = 0.3
        # 下移量
        self.fleet_drop_speed = 10
        # 1右移，-1左移
        self.fleet_direction = 1
