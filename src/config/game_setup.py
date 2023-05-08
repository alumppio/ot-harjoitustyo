import pygame
from repositories.constants import WHITE, RED, START_FONT, START_TEXT_NAME \
    , SCREEN, START_TEXT_PLAYERS, BLACK
from config.dice import Dices
from config.player import Player
from config.gui import EventHandler



class Setup:
    '''Class to handle the game setup as in naming urself etc.'''
    def __init__(self):
        self.running = True
        self.name = ''
        self.players_amount = ''
        self.players = []
        self.event_handlers = []
        SCREEN.fill(WHITE)

    def name_setup_loop(self, player, player_number):
        '''A method that can be used to check occured events and sets the
        players name that was written'''
        SCREEN.blit(START_TEXT_NAME, pygame.Rect(40, 300, 20, 30))
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
                exit()
        name = START_FONT.render(self.name, True, RED, WHITE)
        self.draw_name_setup(name, player_number)

    def amount_of_players_loop(self):
        SCREEN.blit(START_TEXT_PLAYERS, pygame.Rect(40, 300, 20, 30))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE and 0 < len(self.players_amount):
                    self.players_amount = self.players_amount[:-1]
                elif event.key == pygame.K_RETURN and 0 < len(self.players_amount):
                    self.players_amount = self.players_amount
                    self.running = False
                elif 0 <= len(self.players_amount) < 1:
                    self.players_amount += event.unicode
            elif event.type == pygame.QUIT:
                exit()
        number = START_FONT.render(self.players_amount, True, RED, WHITE)
        self.draw_amount_setup(number)

    def amount_setup(self):
        while self.running:
            self.amount_of_players_loop()
        self.running = True
        SCREEN.fill(WHITE)

    def name_setup(self, player_amount):
        if player_amount > 6 or player_amount < 0:
            raise ValueError("Incorrect player amount!")
        
        for i in range(player_amount):
            self.running = True
            player = Player()
            while self.running:
                self.name_setup_loop(player, i)
            self.players.append(player)
            self.name = ''

        SCREEN.fill(WHITE)

    def game_setup(self):
        self.amount_setup()
        try:
            self.name_setup(int(self.players_amount))
        except:
            raise ValueError("Incorrect player amount!")
        self.convert_to_event_handlers()

    def convert_to_event_handlers(self):
        for player in self.players:
            self.event_handlers.append(EventHandler(Dices(), player, self.players.index(player)))
        

    def draw_amount_setup(self, number):
        SCREEN.fill(WHITE)
        SCREEN.blit(number, pygame.Rect(500, 200, 20, 30))
        SCREEN.blit(START_TEXT_PLAYERS, pygame.Rect(40, 200, 20, 30))
        pygame.display.flip()

    def draw_name_setup(self, name, player_number):
        '''Method that draws everything related to typing your name'''
        SCREEN.fill(WHITE)
        SCREEN.blit(name, pygame.Rect(500, 200, 20, 30))
        SCREEN.blit(START_TEXT_NAME, pygame.Rect(40, 200, 20, 30))
        player = START_FONT.render(f'Player{player_number+1}', True, BLACK, WHITE)
        SCREEN.blit(player, pygame.Rect(40, 150, 20, 30))
        pygame.display.flip()
