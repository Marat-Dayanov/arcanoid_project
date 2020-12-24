import pygame


class Player():
    def __init__(self, width, height):
        self.board_width = 100
        self.board_height = 30

        self.x, self.y = width // 2, height

    def move(self, moving):
        pygame.draw.rect(screen, 'white',  (self.x + moving, self.y,
                                            self.board_width, self.board_height))


if __name__ == '__main__':
    pygame.init()
    size = 470, 470
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True
    player = Player(470, 470)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.K_RIGHT:
                player.move(-1)
            if event.type == pygame.K_LEFT:
                player.move(1)
        pygame.display.flip()
        screen.fill('black')
    pygame.quit()
