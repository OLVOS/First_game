import pygame
import exp.pygame.game_1.main.settings


class Stats():

    def __init__(self, screen):
        self.stats_reset()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.icon_health = pygame.image.load('/code/pymain/exp/pygame/game_1/main/images/player2.png')
        self.rect = self.icon_health.get_rect()

        with open('../record.txt', 'r') as r:
            self.record = int(r.readline())

        # self.rect.x = self.screen_rect.x
        # self.rect.y = self.screen_rect.y

        # self.rect.top = self.screen_rect.topleft

    def stats_reset(self):
        self.health = 2
        self.score = 0

    def draw(self):
        self.screen.blit(self.icon_health, self.rect)
