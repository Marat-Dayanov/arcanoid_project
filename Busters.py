import pygame
from config import HEIGHT, WIDTH
from Utiles import *
from ball import *
from config import *


class Buster(pygame.sprite.Sprite):
    game = None

    def __init__(self, x, y, all_sprites):
        super().__init__(all_sprites)
        self.radius = 20
        self.rect = pygame.Rect(x, y, 2 * self.radius, 2 * self.radius)
        self.vy = 1

    def update(self):
        """Падение бустера и проверка столкновения бустера с платформой"""
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
        """Изменение параметров игры"""
        pass

    @classmethod
    def destroy(cls):
        """Уничтожение действия бустера"""
        pass


class PositiveBuster(Buster):
    image = load_image('buster.png')

    def __init__(self, x, y, all_sprites):
        super(PositiveBuster, self).__init__(x, y, all_sprites)
        self.image = PositiveBuster.image


class NegativeBuster(Buster):
    image = load_image('bad_buster.png')

    def __init__(self, x, y, all_sprites):
        super(NegativeBuster, self).__init__(x, y, all_sprites)
        self.image = NegativeBuster.image


class GreatPlayerBuster(PositiveBuster):
    """Бустер, увеличавающий платформу"""
    def bonus(self):
        self.game.player.set_width(Buster.game.player.rect.w * 2)
        pygame.time.set_timer(BUSTERENDEVENT, 10000)

    @classmethod
    def destroy(cls):
        Buster.game.player.set_width(Buster.game.player.rect.w * 0.5)


class SpeedBuster(PositiveBuster):
    """Бустер, ускоряющий платформу"""
    def bonus(self):
        self.game.player.set_player_speed(Buster.game.player.speed * 2)
        pygame.time.set_timer(BUSTERENDEVENT, 10000)

    @classmethod
    def destroy(cls):
        Buster.game.player.set_player_speed(Buster.game.player.speed * 0.5)


class PowerBuster(PositiveBuster):
    """Бустер, увеличавающий силу шарика"""
    def bonus(self):
        for ball in Buster.game.balls:
            ball.power = 3
        pygame.time.set_timer(BUSTERENDEVENT, 20000)

    @classmethod
    def destroy(cls):
        for ball in Buster.game.balls:
            ball.power = 1


class ManyBuster(PositiveBuster):
    """Бустер, увеличавающий кол-во шариков"""
    def bonus(self):
        Buster.game.buster = None
        Ball(Buster.game.all_sprites, Buster.game.balls, Buster.game.player, Buster.game.blocks, Buster.game)
        Ball(Buster.game.all_sprites, Buster.game.balls, Buster.game.player, Buster.game.blocks, Buster.game)


class SmallPlayerBuster(NegativeBuster):
    """Бустер, уменьшающий платформу"""
    def bonus(self):
        self.game.player.set_width(Buster.game.player.rect.w * 0.5)
        pygame.time.set_timer(BUSTERENDEVENT, 20000)

    @classmethod
    def destroy(cls):
        Buster.game.player.set_width(Buster.game.player.rect.w * 2)


class SpeedNegativePlayerBuster(NegativeBuster):
    """Бустер, замедляющий платформу"""
    def bonus(self):
        self.game.player.set_player_speed(Buster.game.player.speed * 0.5)
        pygame.time.set_timer(BUSTERENDEVENT, 10000)

    @classmethod
    def destroy(cls):
        Buster.game.player.set_player_speed(Buster.game.player.speed * 2)


class HealthBlockBuster(NegativeBuster):
    """Бустер, восстанавливающий жизни всех шариков"""
    def bonus(self):
        for block in Buster.game.blocks:
            if block.health != -5:
                block.health = 3
                block.refresh_image()
                Buster.game.buster = None


"""Список всех бустеров"""
busters = [
    GreatPlayerBuster,
    SpeedBuster,
    PowerBuster,
    ManyBuster,
    SmallPlayerBuster,
    SpeedNegativePlayerBuster,
    HealthBlockBuster
]
