import pygame


class Menu():

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.front = pygame.font.Font(None, 36)

        self.text = self.front.render("Играть", True, (255, 255, 255))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.screen_rect.center

    def output_menu(self):
        self.screen.blit(self.text, self.text_rect)