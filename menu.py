import sys
import pygame
from Utiles import *


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


class Menu:
    img = None

    def __init__(self, punkts):
        self.punkts = punkts
        self.game = None
        self.font = pygame.font.Font(None, 50)

    def set_game(self, game):
        self.game = game

    def render(self):
        self.game.screen.blit(self.img, (0, 0))
        with open('completed_levels.txt', 'r') as file:
            COMPLETED_LEVELS = file.readlines()
            COMPLETED_LEVELS = [int(i) for i in COMPLETED_LEVELS]
            for i, item in enumerate(self.punkts):
                x = 180
                y = i * 40 + 100
                if COMPLETED_LEVELS[i]:
                    self.game.screen.blit(MenuItem.star_image, (x, y))
                if item.is_active:
                    text = self.font.render(item.name, True, item.active_color)
                else:
                    text = self.font.render(item.name, True, item.base_color)
                self.game.screen.blit(text, (x, y))

    def menu(self):
        done = True
        while done:
            self.game.screen.fill((0, 0, 0))

            self.render()

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    x, y = pygame.mouse.get_pos()
                    num = (y - 100) // 40
                    if num < 0:
                        num = 0
                    if num >= len(self.punkts):
                        num = len(self.punkts) - 1
                    self.punkts[num].on_click()
                    done = False

                if e.type == pygame.MOUSEMOTION:
                    x, y = pygame.mouse.get_pos()
                    num = (y - 100) // 40
                    if num < 0:
                        num = 0
                    if num >= len(self.punkts):
                        num = len(self.punkts) - 1
                    for i, item in enumerate(self.punkts):
                        item.is_active = False
                    self.punkts[num].is_active = True
            self.game.screen.blit(self.game.screen, (0, 0))
            pygame.display.flip()

    def complete_level(self):
        with open('completed_levels.txt', 'r') as file:
            COMPLETED_LEVELS = file.readlines()
            COMPLETED_LEVELS = [int(i) for i in COMPLETED_LEVELS]
            for i, punkt in enumerate(self.punkts):
                if punkt.is_active:
                    COMPLETED_LEVELS[i] = 1

        with open('completed_levels.txt', 'w') as file:
            COMPLETED_LEVELS = [str(i) for i in COMPLETED_LEVELS]
            file.write('\n'.join(COMPLETED_LEVELS))


class MenuItem:
    game = None
    star_image = load_image('star.jpg')
    star_image_complete = load_image('star.jpg')

    def __init__(self, name, base_color, active_color, level):
        self.name = name
        self.base_color = base_color
        self.active_color = active_color
        self.level = level
        self.is_active = False

    def on_click(self):
        MenuItem.game.clear()
        MenuItem.game.set_level(self.level)
