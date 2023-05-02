import pygame
from repositories.constants import WHITE, RED, START_FONT, START_TEXT, SCREEN


class Setup:
    def __init__(self):
        self.running = True
        self.name = ''
        SCREEN.blit(START_TEXT, pygame.Rect(40, 300, 20, 30))

    def game_setup_loop(self, player):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE and 0 < len(self.name):
                    self.name = self.name[:-1]
                elif event.key == pygame.K_RETURN:
                    player.minutes['Name'] = self.name
                    self.running = False
                elif 0 <= len(self.name) < 8:
                    self.name += event.unicode.upper()
            elif event.type == pygame.QUIT:
                pygame.quit()
        name = START_FONT.render(self.name, True, RED, WHITE)
        self.draw_game_setup(name)

    def game_setup(self, player):
        while self.running:
            self.game_setup_loop(player)
        SCREEN.fill(WHITE)

    def draw_game_setup(self, name):
        SCREEN.fill(WHITE)
        SCREEN.blit(name, pygame.Rect(500, 200, 20, 30))
        SCREEN.blit(START_TEXT, pygame.Rect(40, 200, 20, 30))
        pygame.display.flip()
