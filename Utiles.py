import os, sys, pygame
from levels import *
from menu import Menu, MenuItem

pygame.init()


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


BUSTERENDEVENT = pygame.USEREVENT + 1

Menu.img = load_image('menu_background.png')


for i, level in enumerate(levels):
    if i == 10:
        level.bg = load_image('background_for_LOL.jpg')
    else:
        level.bg = load_image('img.jpg')


menu_items = [MenuItem(f'Level {i + 1}', (250, 250, 30), (250, 30, 250), level) for i, level in enumerate(levels)]
menu = Menu(menu_items)
