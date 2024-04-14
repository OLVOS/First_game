import pygame


class Score():

    def __init__(self, screen, stats, bg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.bg = bg
        self.text_color = (200, 10, 100)
        self.front = pygame.font.SysFont(None, 50)
        self.image_score()
        self.image_record()

    def image_score(self):
        self.score_img = self.front.render(str(self.stats.score), True, self.text_color, self.bg)
        self.score_rect = self.score_img.get_rect()
        self.score_rect.top = self.screen_rect.top+10
        self.score_rect.right = self.screen_rect.centery+45

    def image_record(self):
        self.record_img = self.front.render(str(self.stats.record), True, self.text_color, self.bg)
        self.record_rect = self.record_img.get_rect()
        self.record_rect.top = self.screen_rect.top + 10
        self.record_rect.right = self.screen_rect.right

    def output_score(self):
        """рисовка"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.record_img, self.record_rect)

