import pygame
from config import HEIGHT, WIDTH
from Utiles import BUSTERENDEVENT


class Buster(pygame.sprite.Sprite):
    def __init__(self, radius, x, y, all_sprites, game):
        super().__init__(all_sprites)
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("blue"),
                           (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vy = 1
        self.game = game

    def update(self):
        if pygame.sprite.collide_rect(self, self.game.player) or self.rect.y > HEIGHT:
            self.bonus()
            for group in self.groups():
                group.remove(self)
        self.rect = self.rect.move(0, self.vy)

    def bonus(self):
        pass


class GreatPlayerBuster(Buster):
    def bonus(self):
        self.game.player.set_width(self.game.player.rect.w * 1.5)
        pygame.time.set_timer(BUSTERENDEVENT, 10000)


busters = [
    GreatPlayerBuster
]
