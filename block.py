import pygame
from config import *
from Utiles import *


class Block(pygame.sprite.Sprite):
    image = load_image("block.png")

    def __init__(self, x, y, *groups):
        super().__init__(*groups)
        self.image = Block.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
