import pygame

from config import HEIGHT, WIDTH
from ball import Ball
from Player import *
from block import *
from levels import *
from Busters import *
from menu import *


class Game:
    """Класс игры"""
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Арканоид')

        self.background = None

        self.all_sprites = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()
        self.balls = pygame.sprite.Group()

        self.player = Player(self.all_sprites, self.balls)

        self.clock = pygame.time.Clock()

        Ball(self.all_sprites, self.balls, self.player, self.blocks, self)

        self.buster = None

    def set_level(self, level):
        """Функция прогрузки уровня"""
        self.iron_count = 0
        for i, row in enumerate(level.level_map):
            for j, el in enumerate(row):
                if el == -5:
                    self.iron_count += 1
                if el != 0:
                    Block(j * 60, i * 50, el, self.all_sprites, self.blocks, self)
        self.background = level.bg

    def buster_clear(self):
        """Завершение действия бустера"""
        if self.buster is None:
            return
        self.buster.destroy()
        self.buster = None

    def clear(self):
        """Очистка всех спрайтов, при завершении уровня"""
        self.all_sprites = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()
        self.balls = pygame.sprite.Group()

        self.player = Player(self.all_sprites, self.balls)
        Ball(self.all_sprites, self.balls, self.player, self.blocks, self)

        self.buster = None


if __name__ == '__main__':
    pygame.init()

    game = Game()
    Buster.game = game
    MenuItem.game = game
    menu.set_game(game)
    menu.menu()
    running = True
    while running:
        game.screen.blit(game.background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == BUSTERENDEVENT:
                game.buster_clear()
                pygame.time.set_timer(BUSTERENDEVENT, 0)
        if pygame.key.get_pressed()[pygame.K_a]:
            game.player.move_left()
        if pygame.key.get_pressed()[pygame.K_d]:
            game.player.move_right()
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            game.player.move_left()
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            game.player.move_right()
        game.all_sprites.update()
        game.all_sprites.draw(game.screen)
        pygame.display.flip()
        game.clock.tick(80)
    pygame.quit()
