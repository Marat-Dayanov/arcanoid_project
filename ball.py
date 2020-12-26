import pygame
from config import HEIGHT, WIDTH


class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, x, y, all_sprites, player, blocks):
        super().__init__(all_sprites)
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("red"),
                           (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vx = 2
        self.vy = 2
        self.player = player
        self.blocks = blocks

    def update(self):
        if self.rect.y + self.radius * 2 >= HEIGHT:
            print('You lose')
            exit()
        if not 0 < self.rect.x < WIDTH or not 0 < self.rect.x + self.radius * 2 < WIDTH:
            self.vx = -self.vx
        if self.rect.y <= 0:
            self.vy = -self.vy
        if pygame.sprite.collide_rect(self, self.player):
            self.vy = -self.vy
        self.rect = self.rect.move(self.vx, 0)
        if pygame.sprite.spritecollideany(self, self.blocks):
            self.vx = -self.vx
            self.rect = self.rect.move(self.vx, 0)
        else:
            self.rect = self.rect.move(0, self.vy)
            if pygame.sprite.spritecollideany(self, self.blocks):
                self.vy = -self.vy
                self.rect = self.rect.move(0, self.vy)
