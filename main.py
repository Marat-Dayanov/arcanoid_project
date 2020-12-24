import pygame

from config import HEIGHT, WIDTH
from ball import Ball
from Player import *


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        self.all_sprites = pygame.sprite.Group()

        self.clock = pygame.time.Clock()

        self.player = Player(self.all_sprites)
        self.balls = Ball(10, 20, 100, self.all_sprites)
        self.blocks = []


if __name__ == '__main__':
    pygame.init()

    game = Game()
    running = True
    while running:
        game.screen.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.K_RIGHT:
                game.player.move(-1)
            if event.type == pygame.K_LEFT:
                game.player.move(1)
        game.all_sprites.update()
        game.all_sprites.draw(game.screen)
        pygame.display.flip()
        game.clock.tick(60)
    pygame.quit()
