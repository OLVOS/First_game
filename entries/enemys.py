import pygame


class Enemy(pygame.sprite.Sprite):

    def __init__(self, screen):
        """инит игрока"""
        super(Enemy, self).__init__()

        self.screen = screen
        self.image = pygame.image.load('/code/pymain/exp/pygame/game_1/main/images/enemy3.png')
        self.rect = self.image.get_rect()
        self.speed = 0.6

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height-300
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """рисовка"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """обновление позиции игрока"""
        # self.rect.clamp_ip(self.screen)
        self.y += self.speed
        self.rect.y = self.y

    def get_rect(self):
        return self.rect
