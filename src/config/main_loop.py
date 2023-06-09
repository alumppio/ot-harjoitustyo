import pygame
from repositories.constants import TIMER, FPS
from repositories.delay_time import Delay


class MainLoop:
    ''' Initializing the mainloop using the EventHandler class

    Args: 
        players = [EventHandler(), ... , EventHandler()]

        '''

    def __init__(self, players):
        self.players = players
        self.draw_names()
        self.running = True

    def handle_events(self):
        '''Check all occurred events
        Main gameloop '''

        while self.running:
            for player in self.players:
                self.event_handle_loop(player)
            self.check_if_done()
        Delay(20000)

    def draw_names(self):
        '''
        Method to draw the player names on to the screen
        '''

        for player in self.players:
            player.yatzy_sheet.draw_name(
                player.player, self.players.index(player))

    def check_if_done(self):
        '''
        Method to check if the game has been played through
        '''

        for player in self.players:
            if not player.player.check_total():
                break
            self.running = False

    def event_handle_loop(self, player):
        '''
        Loop that handles the events that have occured in the game of a given player

        Args:
            player (EventHandler) : EventHandler-class object that contains all the needed 
            information of the player
        '''

        player.dice_drawer.clean_dice()
        player.current_player()
        while player.running:
            for event in pygame.event.get():
                TIMER.tick(FPS)
                player.dice_drawer.draw_all()
                player.hold_dice(event)
                player.undo_hold_dice(event)
                player.roll_dice(event)
                player.set_upper_part(event)
                player.set_lower_part(event)
                player.set_total()
                player.quit(event)
                pygame.display.flip()

        player.running = True
