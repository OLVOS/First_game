import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, player):
        super(Bullet, self).__init__()

        self.screen = screen
        self.rect = pygame.Rect(0, 0, 50, 25)
        self.color = 20, 250, 50
        self.speed = 20

        self.rect.centery = player.rect.centery
        self.rect.centerx = player.rect.centerx
        self.rect.top = player.rect.top
        self.y = self.rect.y

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def output_bullet(self):
        """рисовка"""
        pygame.draw.rect(self.screen, self.color, self.rect)
        # self.screen.blit(self.color, self.rect)
