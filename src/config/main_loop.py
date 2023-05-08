import pygame
from repositories.constants import TIMER, FPS


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

        pygame.time.delay(300)
            
    def draw_names(self):
        for PLAYER in self.players:
            PLAYER.yatzy_sheet.draw_name(PLAYER.player, self.players.index(PLAYER))
    
    def check_if_done(self):
        for PLAYER in self.players:
            if not PLAYER.player.check_total():
                return False
            self.running = False
            

    def event_handle_loop(self, player):
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