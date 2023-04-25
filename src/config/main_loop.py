import pygame
from config.gui import EventHandler
from repositories.constants import TIMER, FPS


class MainLoop:
    def __init__(self, dices, players):
        self.event_handler = EventHandler(dices, players)

    def handle_events(self):
        # Check all occurred events
        # Main gameloop

        while self.event_handler.running:
            for event in pygame.event.get():
                TIMER.tick(FPS)
                self.event_handler.dice_drawer.draw_all()
                self.event_handler.hold_dice(event)
                self.event_handler.undo_hold_dice(event)
                self.event_handler.roll_dice(event)
                self.event_handler.quit(event)
                self.event_handler.set_upper_part(event)
                self.event_handler.set_lower_part(event)
                self.event_handler.set_total()
                pygame.display.flip()
