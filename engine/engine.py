import time
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
    clock = pygame.time.Clock()
    # mouse = pygame.mouse.get_pos()

    """ ЦВЕТА """
    bg_color = (0, 40, 100)
    bg_img = pygame.image.load('/code/pymain/exp/pygame/game_1/main/images/bg_3.png')
    bg_menu = pygame.image.load('/code/pymain/exp/pygame/game_1/main/images/bgmenu.jpg')
    # bt_color_1 = (200, 200, 200)

    """ ШРИФТЫ """
    # front_1 = pygame.font.Font(None, 36)

    """ КЛАССЫ """
    menu = Menu(screen, con.SC_WIDTH, con.SC_HEIGHT)
    game = Game(screen)
    player = Player(screen)
    stats = Stats(screen)
    scores = Score(screen, stats, bg_color)

    """ ГРУППЫ """
    enemies = Group()
    bullets = Group()
    # hearts = Group()

    """ ЦИКЛ """
    while True:
        """ ИГРОВОЙ ПРОЦЕСС """
        clock.tick(100)
        interaction.events(screen, menu, stats, scores, game, player, bullets)
        player.update_player()

        if game.state == 'menu':

            screen.blit(bg_menu, (0, 0))
            enemies.empty()
            bullets.empty()

            menu.draw_button()
            scores.output_record()
            player = Player(screen)
            interaction.create_enemy(screen, enemies)
            pygame.display.flip()

        elif game.state == 'gameplay':

            interaction.update_screen(screen, menu, bg_color, bg_img, stats, scores, player, enemies, bullets)
            interaction.update_bullets(screen, stats, scores, bullets, player, enemies)
            interaction.update_enemy(screen, menu, game, stats, player, enemies, bullets)


run()
