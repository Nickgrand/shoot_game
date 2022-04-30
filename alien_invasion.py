import pygame

import game_functions as gf
from settings import Settings
from pygame.sprite import Group
from ship import Ship
from alien import Alien


def run_game():
    # 初始化游戏，创建屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("外星人入侵")

    ship = Ship(ai_settings, screen)
    alien = Alien(ai_settings, screen)
    bullets = Group()

    # 开始游戏主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, alien, bullets)


run_game()
