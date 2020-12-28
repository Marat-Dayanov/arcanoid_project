from random import randrange

import pygame
from config import *
from Utiles import *
from Busters import *


class Block(pygame.sprite.Sprite):
    image1 = load_image("block.png")
    image2 = load_image("block2.png")
    image3 = load_image("block3.png")

    def __init__(self, x, y, health, all_sprites, blocks, player):
        super().__init__(all_sprites, blocks)
        self.all_sprites = all_sprites
        self.player = player
        self.health = health
        if self.health >= 3:
            self.image = Block.image1
        elif self.health == 2:
            self.image = Block.image2
        else:
            self.image = Block.image3
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5

    def check_collide_with_ball(self, ball):
        if pygame.sprite.collide_circle(self, ball):
            self.health -= 1
            if self.health <= 0:
                for group in self.groups():
                    group.remove(self)
                if randrange(0, 2):
                    Buster(20, self.rect.x, self.rect.y, self.all_sprites, self.player)
            if self.health >= 3:
                self.image = Block.image1
            elif self.health == 2:
                self.image = Block.image2
            else:
                self.image = Block.image3
