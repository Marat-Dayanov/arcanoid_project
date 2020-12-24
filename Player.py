import pygame
from config import *


class Player(pygame.sprite.Sprite):
    def __init__(self, all_sprites):
        super().__init__(all_sprites)
        self.board_width = 100
        self.board_height = 30

        self.image = pygame.Surface((self.board_width, self.board_height),
                                    pygame.SRCALPHA, 32)
        pygame.draw.rect(self.image, 'white', (WIDTH // 2, HEIGHT - self.board_height, self.board_width, self.board_height))
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT - self.board_height, self.board_width, self.board_height)

    def move(self, moving):
        self.rect = self.rect.move(moving, 0)

    def update(self):
        self.rect = self.rect.move(1, 0)
