import pygame
from config import HEIGHT, WIDTH
from Utiles import *
from ball import Ball


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
        if pygame.sprite.collide_rect(self, Buster.game.player):
            self.bonus()
            for group in self.groups():
                group.remove(self)
        if self.rect.y > HEIGHT:
            Buster.game.buster = None
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
        self.game.player.set_width(Buster.game.player.rect.w * 2)
        pygame.time.set_timer(BUSTERENDEVENT, 10000)

    @classmethod
    def destroy(cls):
        Buster.game.player.set_width(Buster.game.player.rect.w * 0.5)


class SpeedBuster(Buster):
    def bonus(self):
        self.game.player.set_speed(Buster.game.player.speed * 2)
        pygame.time.set_timer(BUSTERENDEVENT, 10000)

    @classmethod
    def destroy(cls):
        Buster.game.player.set_speed(Buster.game.player.speed * 0.5)


class PowerBuster(Buster):
    def bonus(self):
        for ball in Buster.game.balls:
            ball.power = 3
        pygame.time.set_timer(BUSTERENDEVENT, 20000)

    @classmethod
    def destroy(cls):
        for ball in Buster.game.balls:
            ball.power = 1


class ManyBuster(Buster):
    def bonus(self):
        Buster.game.buster = None
        Ball(Buster.game.all_sprites, Buster.game.balls, Buster.game.player, Buster.game.blocks, Buster.game)
        Ball(Buster.game.all_sprites, Buster.game.balls, Buster.game.player, Buster.game.blocks, Buster.game)


busters = [
    GreatPlayerBuster,
    SpeedBuster,
    PowerBuster,
    ManyBuster
]
