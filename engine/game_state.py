import pygame
from exp.pygame.game_1.main.entries.players import Player


class Game():
    def __init__(self, screen):
        self.screen = screen
        self.player = Player(screen)
        self.enemies = pygame.sprite.Group()
        # self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'menu'

    def quit_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.player.update_player()
        self.enemies.update()

    def draw(self):
        self.screen.fill((222, 22, 222))
        self.player.draw()
        self.enemies.draw(self.screen)
        self.screen.flip()

    def run_game(self):
        while self.running:
            self.quit_event()
            self.update()
            self.draw()
            # self.clock.tick(60)



