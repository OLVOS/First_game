import pygame
import CONSTS as con
import interaction
from pygame.sprite import Group
from players import Player
from stats import Stats
from scores import Score
from menus import Menu


def run():
    """ ЗАПУСК """
    pygame.init()
    pygame.display.set_caption("Vosgard")

    """ ПЕРЕМЕННЫЕ """
    screen = pygame.display.set_mode((con.SC_WIDTH, con.SC_HEIGHT))
    bg_color = (0, 40, 100)
    menu = Menu(screen)

    player = Player(screen)
    enemies = Group()
    bullets = Group()
    hearts = Group()
    stats = Stats(screen)
    scores = Score(screen, stats, bg_color)

    # print(len(hearts))

    """ ЦИКЛ """
    while True:

        """ БАЗОВЫЕ ФУНКЦИИ """
        interaction.events(screen, player, bullets)
        player.update_player()
        # interaction.update_stats(screen, hearts)

        """ ИГРОВОЙ ПРОЦЕСС """
        interaction.update_screen(screen, menu, bg_color, stats, scores, player, enemies, bullets)
        interaction.update_bullets(screen, stats, scores, bullets, enemies)
        interaction.update_enemy(screen, stats, player, enemies, bullets)

        interaction.restart_enemies(screen, player, enemies)


run()
