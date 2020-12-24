import pygame

from config import HEIGHT, WIDTH
from ball import Ball


class EndGameException(Exception):
    pass


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        self.all_sprites = pygame.sprite.Group()

        self.clock = pygame.time.Clock()

        self.player = None
        self.balls = Ball(10, 20, 100, self.all_sprites)
        self.blocks = []

    def update(self):
        self.screen.fill('white')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise EndGameException
        self.all_sprites.update()
        self.all_sprites.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(60)


if __name__ == '__main__':
    pygame.init()

    game = Game()
    try:
        while True:
            game.update()
    except EndGameException:
        pygame.quit()
