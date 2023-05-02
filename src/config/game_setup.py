import pygame
from repositories.constants import WHITE, RED, START_FONT, START_TEXT, SCREEN


class Setup:
    '''Class to handle the game setup as in naming urself etc.'''
    def __init__(self):
        self.running = True
        self.name = ''
        SCREEN.blit(START_TEXT, pygame.Rect(40, 300, 20, 30))

    def game_setup_loop(self, player):
        '''A method that can be used to check occured events and sets the
        players name that was written'''
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE and 0 < len(self.name):
                    self.name = self.name[:-1]
                elif event.key == pygame.K_RETURN and 0 < len(self.name):
                    player.minutes['Name'] = self.name
                    self.running = False
                elif 0 <= len(self.name) < 8:
                    self.name += event.unicode.upper()
            elif event.type == pygame.QUIT:
                pygame.quit()
        name = START_FONT.render(self.name, True, RED, WHITE)
        self.draw_game_setup(name)

    def game_setup(self, player):
        '''A method that is a loop which uses an another method game_setup_loop
        which check occurred events and sets the name of a player. '''
        while self.running:
            self.game_setup_loop(player)
        SCREEN.fill(WHITE)

    def draw_game_setup(self, name):
        '''Method that draws everything related to typing your name'''
        SCREEN.fill(WHITE)
        SCREEN.blit(name, pygame.Rect(500, 200, 20, 30))
        SCREEN.blit(START_TEXT, pygame.Rect(40, 200, 20, 30))
        pygame.display.flip()
