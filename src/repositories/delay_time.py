import pygame
from repositories.constants import TIMER, FPS


class Delay:
    '''
    Class to cause the game to pause for a given amount of time
    '''
    
    def __init__(self, time):
        '''
        Args:
            time (int) : given amount of time in pygame.ticks
        '''
        
        self.running = True
        self.delay_time(time)

    def delay_time(self, time):
        '''
        Main method to delay the game
        
        Args:
            time (int) : given amount of time in pygame.ticks
        '''
        
        
        while self.running:
            TIMER.tick(FPS)
            pygame.event.get()
            current_time = pygame.time.get_ticks()
            pygame.display.flip()
            if current_time >= time:
                self.running = False
