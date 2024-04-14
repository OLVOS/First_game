import pygame
from exp.pygame.game_1.main.settings import CONSTS as con
import interaction
from pygame.sprite import Group
from exp.pygame.game_1.main.entries.players import Player
from exp.pygame.game_1.main.settings.stats import Stats
from exp.pygame.game_1.main.settings.scores import Score
from exp.pygame.game_1.main.settings.menus import Menu
from game_state import Game


def run():
    """ ЗАПУСК """
    pygame.init()
    pygame.display.set_caption("Vosgard")

    """ ПЕРЕМЕННЫЕ """
    screen = pygame.display.set_mode((con.SC_WIDTH, con.SC_HEIGHT))
    mouse = pygame.mouse.get_pos()

    """ ЦВЕТА """
    bg_color = (0, 40, 100)
    bt_color_1 = (200, 200, 200)

    """ ШРИФТЫ """
    front_1 = pygame.font.Font(None, 36)

    """ КЛАССЫ """
    menu = Menu(screen, con.SC_WIDTH, con.SC_HEIGHT)
    game = Game(screen)
    player = Player(screen)
    stats = Stats(screen)
    scores = Score(screen, stats, bg_color)

    """ ГРУППЫ """
    enemies = Group()
    bullets = Group()
    hearts = Group()

    """ ЦИКЛ """
    while True:
        """ БАЗОВЫЕ ФУНКЦИИ """
        interaction.events(screen, menu, game, player, bullets)
        player.update_player()

        if game.state == 'menu':
            print('top if')
            enemies.empty()
            bullets.empty()
            player = Player(screen)
            interaction.create_enemy(screen, enemies)

            menu.draw_button()
            pygame.display.flip()
            print(game.state)
            print('bottom if')

        elif game.state == 'gameplay':
            print('top elif')
            interaction.update_screen(screen, menu, bg_color, stats, scores, player, enemies, bullets)

            interaction.update_bullets(screen, stats, scores, bullets, enemies)
            interaction.update_enemy(screen, menu, game, stats, player, enemies, bullets)

            interaction.restart_enemies(screen, player, enemies)
            print(game.state)
            print('bottom elif')


run()
