'''main.py - запуск приложения'''

import pygame
from game import Game
from constans import *

if __name__ == '__main__':
    pygame.init()
    # установка размеров экрана
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # заголовок окна
    pygame.display.set_caption("PACMAN")
    # делаем пока пользователь не закроет приложение
    done = False
    # переменная для частоты обновления экрана
    clock = pygame.time.Clock()
    # создание экземпляра класса игра Game
    game = Game()
    while not done:
        # обработка событий
        done = game.process_events()
        # логика игры
        game.run_logic()
        # отрисовка экрана
        game.display_frame(screen)
        # fps 30
        clock.tick(30)
    # выход из приложения
    pygame.quit()
