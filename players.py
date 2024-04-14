import pygame


class Player:
    def __init__(self, screen):
        """инит игрока"""

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load('/code/pymain/exp/pygame/game_1/main/images/player2.png')
        self.rect = self.image.get_rect()
        self.speed = 1

        self.center = self.screen_rect.centerx
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.top = self.screen_rect.top
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False
        self.mtop = False
        self.mdown = False

    def draw(self):
        """рисовка"""
        self.screen.blit(self.image, self.rect)

    def update_player(self):
        """обновление позиции игрока"""
        self.rect.clamp_ip(self.screen_rect)
    #
        if self.mright:
            self.rect.centerx += self.speed
        if self.mleft:
            self.rect.centerx -= self.speed
    #
        if self.mtop:
            self.rect.centery -= self.speed
        if self.mdown:
            self.rect.centery += self.speed

    def get_rect(self):
        return self.rect

    def respawn(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom
