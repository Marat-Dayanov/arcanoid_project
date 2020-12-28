import pygame

from config import HEIGHT, WIDTH
from ball import Ball
from Player import *
from block import *
from levels import *
from Busters import *


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        self.all_sprites = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()

        self.level = level1

        for i, row in enumerate(level1):
            for j, el in enumerate(row):
                if el != 0:
                    Block(j * 60, i * 50, el, self.all_sprites, self.blocks)

        self.clock = pygame.time.Clock()

        self.player = Player(self.all_sprites)
        self.balls = Ball(10, 20, 100, self.all_sprites, self.player, self.blocks)
        self.buster = Buster(10, 10, 100, self.all_sprites, self.player)


if __name__ == '__main__':
    pygame.init()

    game = Game()
    running = True
    while running:
        game.screen.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            game.player.move_left()
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            game.player.move_right()
        game.all_sprites.update()
        game.all_sprites.draw(game.screen)
        pygame.display.flip()
        game.clock.tick(60)
    pygame.quit()
