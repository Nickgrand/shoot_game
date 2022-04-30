class Settings:
    """保存所有设置"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        # self.bg_color = (105, 7, 90)
        self.ship_speed_factor = 1.5
