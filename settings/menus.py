import pygame


class Menu():

    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.front = pygame.font.Font(None, 36)
        self.color = (250, 250, 250)

        self.start_button_text = 'START'
        self.start_button_rect = pygame.Rect(screen_width // 2 - 100, 300, 200, 50)

    def draw_button(self):
        """Функция для отображения текста на экране"""
        pygame.draw.rect(self.screen, self.color, self.start_button_rect)

        text_obj = self.front.render(self.start_button_text, True, self.color)
        text_rect = text_obj.get_rect()
        text_rect.center = self.start_button_rect.center

        self.screen.blit(text_obj, text_rect)
