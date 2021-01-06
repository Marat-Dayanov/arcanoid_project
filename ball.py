from random import randrange

import pygame
from config import HEIGHT, WIDTH
from Utiles import *


class Ball(pygame.sprite.Sprite):
    image = load_image('ball.png')

    def __init__(self, x, y, all_sprites, balls, player, blocks):
        super().__init__(all_sprites, balls)
        self.balls = balls
        self.radius = 10
        self.image = Ball.image
        self.rect = pygame.Rect(x, y, 2 * self.radius, 2 * self.radius)
        self.vx = 2
        self.vy = 2
        self.player = player
        self.blocks = blocks
        self.power = 1

    def update(self):
        if self.rect.y + self.radius * 2 >= HEIGHT:
            for group in self.groups():
                group.remove(self)

            if len(self.balls) == 0:
                print('You lose')
                exit()
        if not 0 < self.rect.x < WIDTH or not 0 < self.rect.x + self.radius * 2 < WIDTH:
            self.vx = -self.vx
        if self.rect.y <= 0:
            self.vy = -self.vy
        if pygame.sprite.collide_rect(self, self.player):
            self.vy = -self.vy
            self.vx = self.vx // abs(self.vx) * randrange(1, 4)
        self.rect = self.rect.move(self.vx, 0)
        if pygame.sprite.spritecollideany(self, self.blocks):
            for block in self.blocks:
                block.check_collide_with_ball(self)
            self.vx = -self.vx
            self.rect = self.rect.move(self.vx, 0)
            if len(self.blocks) == 0:
                print('You win')
                exit()
        else:
            self.rect = self.rect.move(0, self.vy)
            if pygame.sprite.spritecollideany(self, self.blocks):
                for block in self.blocks:
                    block.check_collide_with_ball(self)
                self.vy = -self.vy
                self.rect = self.rect.move(0, self.vy)
                if len(self.blocks) == 0:
                    print('You win')
                    exit()
