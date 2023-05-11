import sys
import pygame
from repositories.constants import WHITE, RED, START_FONT, START_TEXT_NAME, SCREEN,\
    START_TEXT_PLAYERS, BLACK, START_TIP_AMOUNT, START_TIP_NAMES
from config.dice import Dices
from config.player import Player
from config.gui import EventHandler


class Setup:
    '''Class to handle the game setup as in choosing how many players will play
    and naming the players'''

    def __init__(self):
        self.running = True
        self.name = ''
        self.players_amount = ''
        self.players = []
        self.event_handlers = []
        SCREEN.fill(WHITE)

    def name_setup_loop(self, player, player_number):
        '''A method that is used to set a certain players name in the Player-class

        
        Args:
            player (Player) : yatzy sheet Player-class object 
            player_number (int) : player number in the Setup-class self.players list
        '''
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
                sys.exit()
        name = START_FONT.render(self.name, True, RED, WHITE)
        self.draw_name_setup(name, player_number)

    def amount_of_players_loop(self):
        '''
        A method to choose how many players will play in the game.
        '''
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE and 0 < len(self.players_amount):
                    self.players_amount = self.players_amount[:-1]
                elif event.key == pygame.K_RETURN and 0 < len(self.players_amount) \
                    and 0<int(self.players_amount)<7:
                    self.players_amount = self.players_amount
                    self.running = False
                elif 0 <= len(self.players_amount) < 1:
                    self.players_amount += event.unicode
            elif event.type == pygame.QUIT:
                sys.exit()
        number = START_FONT.render(self.players_amount, True, RED, WHITE)
        self.draw_amount_setup(number)

    def amount_setup(self):
        '''
        Method that uses Setup-class self.amount_of_players_loop method to set the 
        amount of players playing in the game using the method in a while loop
        '''

        while self.running:
            self.amount_of_players_loop()
        self.running = True
        SCREEN.fill(WHITE)

    def name_setup(self, player_amount):
        '''
        Method that uses Setup-class self.name_setup_loop method to set the 
        names of the players that are playing the game using a the method in a
        while loop

        Args:
            player_amount (int) : amount of players playing from 1-6
        '''

        for i in range(player_amount):
            self.running = True
            player = Player()
            while self.running:
                self.name_setup_loop(player, i)
            self.players.append(player)
            self.name = ''

        SCREEN.fill(WHITE)

    def game_setup(self):
        '''
        Main setup method in the Setup-class. Uses name_setup and amount_setup
        methods.
        '''
        self.amount_setup()
        self.name_setup(int(self.players_amount))
        self.convert_to_event_handlers()

    def convert_to_event_handlers(self):
        '''
        Method that converts the Player-class objects whose names are changed to 
        EventHandler-class objects, prepping them for the main game loop.
        '''

        for player in self.players:
            self.event_handlers.append(EventHandler(
                Dices(), player, self.players.index(player)))

    def draw_amount_setup(self, number):
        '''
        Draws everything related to choosing the amount of players in the game

        Args:
            number (int) : number typed with the keyboard
        '''

        SCREEN.fill(WHITE)
        SCREEN.blit(number, pygame.Rect(430, 200, 20, 30))
        SCREEN.blit(START_TEXT_PLAYERS, pygame.Rect(40, 200, 20, 30))
        SCREEN.blit(START_TIP_AMOUNT, pygame.Rect(50, 300, 100, 30))
        pygame.display.flip()

    def draw_name_setup(self, name, player_number):
        '''
        Method that draws everything related to typing your name
        
        Args:
            name (string) : typed name
            player_number (int) : player number in the yatzy sheet    
        '''

        SCREEN.fill(WHITE)
        SCREEN.blit(name, pygame.Rect(500, 200, 20, 30))
        SCREEN.blit(START_TEXT_NAME, pygame.Rect(40, 200, 20, 30))
        player = START_FONT.render(
            f'Player{player_number+1}', True, BLACK, WHITE)
        SCREEN.blit(player, pygame.Rect(40, 150, 20, 30))
        SCREEN.blit(START_TIP_NAMES, pygame.Rect(50, 300, 100, 30))
        pygame.display.flip()
