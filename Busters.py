import pygame
from config import HEIGHT, WIDTH
from Utiles import *


class Buster(pygame.sprite.Sprite):
    game = None
    image = load_image('buster.png')

    def __init__(self, x, y, all_sprites):
        super().__init__(all_sprites)
        self.radius = 20
        self.image = Buster.image
        self.rect = pygame.Rect(x, y, 2 * self.radius, 2 * self.radius)
        self.vy = 1

    def update(self):
        if pygame.sprite.collide_rect(self, Buster.game.player) or self.rect.y > HEIGHT:
            self.bonus()
            for group in self.groups():
                group.remove(self)
        self.rect = self.rect.move(0, self.vy)

    def bonus(self):
        pass

    @classmethod
    def destroy(cls):
        pass


class GreatPlayerBuster(Buster):
    def bonus(self):
        self.game.player.set_width(Buster.game.player.rect.w * 1.5)
        pygame.time.set_timer(BUSTERENDEVENT, 10000)

    @classmethod
    def destroy(cls):
        Buster.game.player.set_width(Buster.game.player.rect.w * 0.66)


busters = [
    GreatPlayerBuster,
]
