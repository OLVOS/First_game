import pygame
from exp.pygame.game_1.main.settings import CONSTS as con
import interaction
from pygame.sprite import Group
from exp.pygame.game_1.main.entries.players import Player
# from stats import Stats
# from scores import Score
from exp.pygame.game_1.main.settings.menus import Menu
from game_state import Game


def run():
    """ ЗАПУСК """
    pygame.init()
    pygame.display.set_caption("Vosgard")

    """ ПЕРЕМЕННЫЕ """
    screen = pygame.display.set_mode((con.SC_WIDTH, con.SC_HEIGHT))
    game = Game(screen)
    menu = Menu(screen, con.SC_WIDTH, con.SC_HEIGHT)

    """ ЦВЕТА """
    bg_color = (0, 40, 100)
    bt_color_1 = (200, 200, 200)

    """ ШРИФТЫ """
    front_1 = pygame.font.Font(None, 36)

    """ КЛАССЫ """
    player = Player(screen)

    """ ГРУППЫ """
    bullets = Group()

    """ ЦИКЛ """
    while True:
        interaction.events(screen, menu, game, player, bullets)

        """ БАЗОВЫЕ ФУНКЦИИ """
        if game.state == 'menu':
            menu.draw_button()
            print(game.state)
            pygame.display.flip()

        elif game.state == 'gameplay':
            print('gameplay')
            game.run_game()
            pygame.display.flip()

run()
