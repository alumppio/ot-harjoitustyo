import pygame
from repositories.constants import TIMER, FPS


class Delay:
    def __init__(self, time):
        self.running = True
        self.delay_time(time)

    def delay_time(self, time):
        while self.running:
            TIMER.tick(FPS)
            pygame.event.get()
            current_time = pygame.time.get_ticks()
            pygame.display.flip()
            if current_time >= time:
                self.running = False
