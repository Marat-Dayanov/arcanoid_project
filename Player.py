from copy import deepcopy

import pygame
from config import *
from Utiles import *


class Player(pygame.sprite.Sprite):
    image = load_image("platform.png")

    def __init__(self, all_sprites, balls):
        super().__init__(all_sprites)
        self.image = Player.image
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2
        self.rect.y = HEIGHT - 50
        self.speed = 2
        self.balls = balls

    def move_left(self):
        """Движение платформы влево"""
        prev_rect = deepcopy(self.rect)
        if self.rect.x - self.speed >= 0:
            self.rect = self.rect.move(-self.speed, 0)
        else:
            self.rect.x = 0
        if pygame.sprite.spritecollideany(self, self.balls):
            self.rect = prev_rect

    def move_right(self):
        """Движение платформы вправо"""
        prev_rect = deepcopy(self.rect)
        if self.rect.x + self.speed + self.rect.w <= WIDTH:
            self.rect = self.rect.move(self.speed, 0)
        else:
            self.rect.x = WIDTH - self.rect.w
        if pygame.sprite.spritecollideany(self, self.balls):
            self.rect = prev_rect

    def set_width(self, width):
        """Установка длины платформы"""
        x, y = self.rect.x, self.rect.y
        self.image = pygame.transform.scale(self.image, (int(width), int(self.rect.h)))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def set_player_speed(self, speed):
        """Установка скорости платформы"""
        self.speed = speed
