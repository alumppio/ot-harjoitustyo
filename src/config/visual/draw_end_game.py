import sys
from sqlite3 import OperationalError
import pygame
from services.connection import CONNECTION
from repositories.constants import SCREEN, END_FONT, END_TEXT, BLACK, WHITE, END_TIP


class DrawEndGame:
    def __init__(self):
        try:
            self.scores = CONNECTION.execute("""
        SELECT name, score FROM High_Scores ORDER BY score DESC;
        """)
        except OperationalError:
            print('DATABASE NOT BUILT!!! THE GAME CLOSED.')
            sys.exit()

        self.count = 1
        SCREEN.fill(WHITE)
        SCREEN.blit(END_TEXT, pygame.Rect(50, 30, 20, 30))
        SCREEN.blit(END_TIP, pygame.Rect(30, 400, 20, 30))
        pygame.display.flip()

    def draw_high_scores(self):
        for row in self.scores:
            self.draw(row[0], row[1], self.count)
            self.count += 1
            if self.count > 5:
                break
        pygame.display.flip()

    def draw(self, name, score, number):
        text = END_FONT.render(
            f'{number}: {name} - {score} points', True, BLACK, WHITE)
        SCREEN.blit(text, pygame.Rect(60, 60+30*number, 20, 30))
