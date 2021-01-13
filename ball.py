from random import randrange

import pygame
from config import HEIGHT, WIDTH
from Utiles import *


class Ball(pygame.sprite.Sprite):
    image = load_image('ball.png')

    def __init__(self, all_sprites, balls, player, blocks, game):
        super().__init__(all_sprites, balls)
        self.balls = balls
        self.radius = 10
        self.image = Ball.image
        self.rect = pygame.Rect(player.rect.x + player.rect.w // 2, player.rect.y - player.rect.h, 2 * self.radius, 2 * self.radius)
        self.vx = randrange(1, 4)
        self.vy = randrange(2, 4)
        self.player = player
        self.blocks = blocks
        self.power = 1
        self.game = game

    def update(self):
        if self.rect.y + self.radius * 2 >= HEIGHT:
            for group in self.groups():
                group.remove(self)
            if len(self.balls) == 0:
                menu.menu()
        if not 0 < self.rect.x < WIDTH or not 0 < self.rect.x + self.radius * 2 < WIDTH:
            self.vx = -self.vx
        if self.rect.y <= 0:
            self.vy = -self.vy
        self.rect = self.rect.move(self.vx, 0)

        if pygame.sprite.collide_rect(self, self.player):
            self.vy = -self.vy
            self.vx = -self.vx
            self.rect = self.rect.move(self.vx, 0)
        elif pygame.sprite.spritecollideany(self, self.blocks):
            for block in self.blocks:
                block.check_collide_with_ball(self)
            self.vx = -self.vx
            self.rect = self.rect.move(self.vx, 0)
            if len(self.blocks) == self.game.iron_count:
                menu.complete_level()
                menu.menu()
        else:
            self.rect = self.rect.move(0, self.vy)

            if pygame.sprite.collide_rect(self, self.player):
                self.vy = -self.vy
                self.rect = self.rect.move(0, self.vy)

            elif pygame.sprite.spritecollideany(self, self.blocks):
                for block in self.blocks:
                    block.check_collide_with_ball(self)
                self.vy = -self.vy
                self.rect = self.rect.move(0, self.vy)
                if len(self.blocks) == self.game.iron_count:
                    menu.complete_level()
                    menu.menu()
