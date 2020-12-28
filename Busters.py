import pygame
from config import HEIGHT, WIDTH


class Buster(pygame.sprite.Sprite):
    def __init__(self, radius, x, y, all_sprites, player):
        super().__init__(all_sprites)
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("blue"),
                           (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vy = 2
        self.player = player

    def update(self):
        if pygame.sprite.collide_rect(self, self.player) or self.rect.y > HEIGHT:
            for group in self.groups():
                group.remove(self)
        self.rect = self.rect.move(0, self.vy)
