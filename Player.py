import pygame
from config import *
from Utiles import *


class Player(pygame.sprite.Sprite):
    image = load_image("platform.png")

    def __init__(self, all_sprites):
        super().__init__(all_sprites)
        self.image = Player.image
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2
        self.rect.y = HEIGHT - 50
        self.speed = 5

    def move_left(self):
        self.rect = self.rect.move(-self.speed, 0)

    def move_right(self):
        self.rect = self.rect.move(self.speed, 0)
