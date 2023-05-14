import sys
from sqlite3 import OperationalError
import pygame
from services.connection import CONNECTION
from config.visual.draw_end_game import DrawEndGame
from repositories.delay_time import Delay


class EndGame:
    def __init__(self, players):
        '''
        Class to handle the ending of the game. 

        Args:
            players (list) : list of Player-class objects
        '''
        self.players = players

    def set_high_scores(self):
        '''
        Method to set the high scores of the players in the database
        '''

        for player in self.players:
            try:
                CONNECTION.execute(
                    """insert into High_Scores (name, score) values (?, ?)""",
                    (player.player.minutes['Name'],
                     player.player.total_points())
                )
                CONNECTION.commit()
            except OperationalError:
                print('DATABASE NOT BUILT!!! THE GAME CLOSED.')
                sys.exit()

    def show_high_scores(self):
        '''
        Method to draw the high scores on to the screen
        '''

        drawer = DrawEndGame()
        drawer.draw_high_scores()

    def end_game(self):
        '''
        Main method to handle the ending of the game. Uses the classes other methods.
        '''

        self.set_high_scores()
        self.show_high_scores()
        Delay(30000)
        pygame.quit()
