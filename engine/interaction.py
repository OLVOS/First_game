import pygame, sys
from exp.pygame.game_1.main.settings import CONSTS as con
from exp.pygame.game_1.main.entries.enemys import Enemy
from exp.pygame.game_1.main.entries.bullet import Bullet
from exp.pygame.game_1.main.settings.stats import Stats
from game_state import Game
import time


def events(screen, menu, stats, sc, game, player, bullets):
    """обработка событий"""

    for event in pygame.event.get():

        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if game.state == 'menu' and menu.start_button_rect.collidepoint(mouse_pos):
                stats.score = 0
                sc.image_score()
                game.state = 'gameplay'

        elif event.type == pygame.KEYDOWN:
            game = Game(screen)
            if event.key == pygame.K_d: #право
                player.mright = True
            elif event.key == pygame.K_a: #лево
                player.mleft = True
            elif event.key == pygame.K_w: #верх
                player.mtop = True
            elif event.key == pygame.K_s: #низ
                player.mdown = True
            elif event.key == pygame.K_SPACE: #пробел
                new_bullet = Bullet(screen, player)
                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d: #право
                player.mright = False
            elif event.key == pygame.K_a: #лево
                player.mleft = False
            elif event.key == pygame.K_w: #верх
                player.mtop = False
            elif event.key == pygame.K_s: #низ
                player.mdown = False


def create_enemy(screen, enemies):
    enemy = Enemy(screen)
    enemy_width = enemy.rect.width+10
    enemy_height = enemy.rect.height+30
    count_enemy_x = int((con.SC_WIDTH - 2 * enemy_width) / enemy_width)
    count_enemy_y = int((con.SC_HEIGHT - 200 - 2 * enemy_height) / enemy_height)

    for enemy_heig in range(count_enemy_y):
        for enemy_wid in range(count_enemy_x):
            enemy = Enemy(screen)

            enemy.x = enemy_width + (enemy_width * enemy_wid)
            enemy.y = enemy_height + (enemy_height * enemy_heig)
            enemy.rect.x = enemy.x
            enemy.rect.y = enemy.rect.height + (enemy.rect.height * enemy_heig)

            enemies.add(enemy)


def update_stats(screen, hearts):
    stats = Stats(screen)
    stats_width = stats.rect.width

    for heart in range(4):
        stats = Stats(screen)
        stats.x = stats_width + (stats_width * heart)
        stats.rect.x = stats.x

        hearts.add(hearts)
    print(len(hearts))


def restart_enemies(screen, player, enemies):
    if len(enemies) == 0:
        # time.sleep(0.5)
        player.respawn()
        create_enemy(screen, enemies)


def player_kill(screen, stats, player, enemies, bullets):
    stats.health -= 1
    enemies.empty()
    bullets.empty()
    player.respawn()
    # create_enemy(screen, enemies)
    time.sleep(1)


def update_bullets(screen, stats, sc, bullets, player, enemies):
    bullets.update()
    if len(enemies) == 0:
        bullets.empty()
        print('enemies = 0 and bullet.empty')
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    collisions = pygame.sprite.groupcollide(bullets, enemies, True, True)

    for enemy in collisions.values():
        stats.score += 1 * len(enemy)

    if collisions:
        stats.score += 1
        sc.image_score()
        record_check(stats, sc)
        enemies_check(screen, stats, player, enemies, bullets)


def update_enemy(screen, menu, game, stats, player, enemies, bullets):
    enemies.update()

    enemies_check(screen, stats, player, enemies, bullets)
    if pygame.sprite.spritecollideany(player, enemies):
        player_kill(screen, stats, player, enemies, bullets)
        print('oops!', f'Твои жизни:{stats.health}')

    elif stats.health == 0:

        enemies.empty()
        bullets.empty()

        game.state = 'menu'
        stats.health = 2
        return


def enemies_check(screen, stats, player, enemies, bullets):
    screen_rect = screen.get_rect()

    for enemy in enemies.sprites():
        if enemy.rect.bottom == screen_rect.bottom:
            player_kill(screen, stats, player, enemies, bullets)
            break
    if len(enemies) == 0:
        bullets.empty()
        restart_enemies(screen, player, enemies)


def record_check(stats, sc):
    if stats.score > stats.record:
        stats.record = stats.score
        sc.image_record()
        with open('../record.txt', 'w') as r:
            r.write(str(stats.record))


def update_screen(screen, menu, color, bg, hearts, score, player, enemies, bullets):
    # screen.fill(color)
    screen.blit(bg, (0, 0))

    for bullet in bullets.sprites():
        bullet.output_bullet()

    score.output_score()
    player.draw()
    enemies.draw(screen)
    pygame.display.flip()
