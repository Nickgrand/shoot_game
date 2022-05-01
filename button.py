import pygame.font


class Button:
    def __init__(self, ai_settings, screen, msg):
        """初始化按钮属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 设置按钮尺寸和其他属性
        self.width, self.height = ai_settings.screen_width / 5, ai_settings.screen_width / 5
        self.button_color = (105, 7, 90)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont("arial", 48)

        # 创建按钮的rect对象，并居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 按钮的标签只需创建一次
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """将按钮渲染为图像，并在按钮上居中"""
        self.msg_img = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center

    def draw_button(self):
        # 绘制用颜色填充的按钮，再绘制文本
        # 位于中间
        self.screen.fill(self.button_color, self.rect)
        # 位于左上
        self.screen.blit(self.msg_img, self.msg_img_rect)
