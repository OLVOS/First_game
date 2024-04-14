import pygame, sys
import CONSTS as con
from enemys import Enemy
from bullet import Bullet
from stats import Stats
from scores import Score
from menus import Menu
import time


def events(screen, player, bullets):
    """обработка событий"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            sys.exit()
            # running = False

        elif event.type == pygame.KEYDOWN:
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

            elif event.type == pygame.MOUSEBUTTONDOWN:
                menu = Menu(screen)
                if menu.text_rect.collidepoint(event.pos):

                    print("Нажата кнопка 'Играть'")

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d: #право
                player.mright = False
            elif event.key == pygame.K_a: #лево
                player.mleft = False
            elif event.key == pygame.K_w: #верх
                player.mtop = False
            elif event.key == pygame.K_s: #низ
                player.mdown = False


# def damage(player, enemy, bullet):
#     player = player.get_rect()
#     enemy = enemy.get_rect()
#     bullet = bullet.get_rect()
#
#     if bullet.colliderect(enemy):
#         print('YOU LOSE')
# def damage2():


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
        time.sleep(0.5)
        player.respawn()
        create_enemy(screen, enemies)


def player_kill(screen, stats, player, enemies, bullets):
    stats.health -= 1
    enemies.empty()
    bullets.empty()
    player.respawn()
    create_enemy(screen, enemies)
    time.sleep(1)


def update_bullets(screen, stats, sc, bullets, enemies):
    bullets.update()
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


def update_enemy(screen, stats, player, enemies, bullets):
    enemies.update()
    if stats.health == 0:
        sys.exit()

    if pygame.sprite.spritecollideany(player, enemies):
        player_kill(screen, stats, player, enemies, bullets)
        print('oops!', f'Твои жизни:{stats.health}')
    enemies_check(screen, stats, player, enemies, bullets)


def enemies_check(screen, stats, player, enemies, bullets):
    screen_rect = screen.get_rect()

    for enemy in enemies.sprites():
        if enemy.rect.bottom == screen_rect.bottom:
            player_kill(screen, stats, player, enemies, bullets)
            break


def record_check(stats, sc):
    if stats.score > stats.record:
        stats.record = stats.score
        sc.image_record()
        with open('record.txt', 'w') as r:
            r.write(str(stats.record))


def update_screen(screen, menu, bg, hearts, score, player, enemies, bullets):
    screen.fill(bg)
    menu.output_menu()
    # hearts.draw()
    score.output_score()

    for bullet in bullets.sprites():
        bullet.output_bullet()
    player.draw()
    enemies.draw(screen)
    pygame.display.flip()
