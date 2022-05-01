import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from score_board import ScoreBoard


def run_game():
    # 初始化游戏，创建屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("外星人入侵")

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建用于存储统计信息的实例
    stats = GameStats(ai_settings)
    board = ScoreBoard(ai_settings, screen, stats)

    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏主循环
    while True:
        gf.check_events(ai_settings, screen, stats, board, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, board, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, board, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, board, ship, aliens, bullets, play_button)


run_game()
