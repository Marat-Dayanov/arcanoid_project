import pygame
from config import *
from Utiles import *


class Block(pygame.sprite.Sprite):
    image = load_image("block.png")

    def __init__(self, x, y, health, *groups):
        super().__init__(*groups)
        self.image = Block.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        self.health = health

    def check_collide_with_ball(self, ball):
        if pygame.sprite.collide_circle(self, ball):
            self.health -= 1
            if self.health <= 0:
                for group in self.groups():
                    group.remove(self)
