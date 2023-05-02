import pygame
from config.dice import Dices
from repositories.constants import DICE_Y, DICE_X, DICE_A, DICE_GAP, BLACK
from repositories.constants import DICE_ROLLER, ROLL_TEXT, GRAY, RED, WHITE


class DrawDice:
    """Class to draw dices to the plane"""

    def __init__(self, dices: Dices, surface):
        self.dices = dices
        self.surface = surface

    def dice_side_1(self, dice_number):
        """Defining dice side 1"""
        pygame.draw.rect(self.surface, BLACK, pygame.Rect(DICE_X + DICE_GAP*dice_number +
                    DICE_A*dice_number, DICE_Y, DICE_A, DICE_A), 2)
        pygame.draw.circle(self.surface, BLACK, (DICE_X + DICE_GAP*dice_number +
                    DICE_A/2 + dice_number*DICE_A, DICE_Y + DICE_A/2), 5)

    def dice_side_2(self, dice_number):
        """Defining dice side 2"""
        pygame.draw.rect(self.surface, BLACK, pygame.Rect(DICE_X + DICE_GAP*dice_number +
                    DICE_A*dice_number, DICE_Y, DICE_A, DICE_A), 2)
        pygame.draw.circle(self.surface, BLACK, (DICE_X + DICE_GAP*dice_number + DICE_A/4
                    + dice_number*DICE_A, DICE_Y + DICE_A/2), 5)
        pygame.draw.circle(self.surface, BLACK, (DICE_X + DICE_GAP*dice_number + 3*DICE_A/4
                        + dice_number*DICE_A, DICE_Y + DICE_A/2), 5)

    def dice_side_3(self, dice_number):
        """Defining dice side 3"""
        pygame.draw.rect(self.surface, BLACK, pygame.Rect(DICE_X + DICE_GAP*dice_number +
                        DICE_A*dice_number, DICE_Y, DICE_A, DICE_A), 2)
        pygame.draw.circle(self.surface, BLACK, (DICE_X + DICE_GAP*dice_number + DICE_A/4
                                                 + dice_number*DICE_A, DICE_Y + DICE_A/4), 5)
        pygame.draw.circle(self.surface, BLACK, (DICE_X + DICE_GAP*dice_number + DICE_A/2
                                                 + dice_number*DICE_A, DICE_Y + DICE_A/2), 5)
        pygame.draw.circle(self.surface, BLACK, (DICE_X + DICE_GAP*dice_number + 3*DICE_A/4
                                                 + dice_number*DICE_A, DICE_Y + 3*DICE_A/4), 5)

    def dice_side_4(self, dice_number):
        """Defining dice side 4"""
        pygame.draw.rect(self.surface, BLACK, pygame.Rect(DICE_X + DICE_GAP*dice_number +
                        DICE_A*dice_number, DICE_Y, DICE_A, DICE_A), 2)
        pygame.draw.circle(self.surface, BLACK, (DICE_X + DICE_GAP*dice_number + DICE_A/4
                                                 + dice_number*DICE_A, DICE_Y + DICE_A/4), 5)
        pygame.draw.circle(self.surface, BLACK, (DICE_X + DICE_GAP*dice_number + 3*DICE_A/4
                                                 + dice_number*DICE_A, DICE_Y + DICE_A/4), 5)
        pygame.draw.circle(self.surface, BLACK, (DICE_X + DICE_GAP*dice_number + DICE_A/4
                                                 + dice_number*DICE_A, DICE_Y + 3*DICE_A/4), 5)
        pygame.draw.circle(self.surface, BLACK, (DICE_X + DICE_GAP*dice_number + 3*DICE_A/4
                                                 + dice_number*DICE_A, DICE_Y + 3*DICE_A/4), 5)

    def dice_side_5(self, dice_number):
        """Defining dice side 5"""
        pygame.draw.rect(self.surface, BLACK, pygame.Rect(DICE_X + DICE_GAP*dice_number
                        + DICE_A*dice_number, DICE_Y, DICE_A, DICE_A), 2)
        pygame.draw.circle(self.surface, BLACK, (DICE_X + DICE_GAP*dice_number +
                        DICE_A/2 + dice_number*DICE_A, DICE_Y + DICE_A/2), 5)
        pygame.draw.circle(self.surface, BLACK, (DICE_X + DICE_GAP*dice_number +
                        DICE_A/4 + dice_number*DICE_A, DICE_Y + DICE_A/4), 5)
        pygame.draw.circle(self.surface, BLACK, (DICE_X + DICE_GAP*dice_number +
                        3*DICE_A/4 + dice_number*DICE_A, DICE_Y + DICE_A/4), 5)
        pygame.draw.circle(self.surface, BLACK, (DICE_X + DICE_GAP*dice_number +
                        DICE_A/4 + dice_number*DICE_A, DICE_Y + 3*DICE_A/4), 5)
        pygame.draw.circle(self.surface, BLACK, (DICE_X + DICE_GAP*dice_number +
                        3*DICE_A/4 + dice_number*DICE_A, DICE_Y + 3*DICE_A/4), 5)

    def dice_side_6(self, dice_number):
        """Defining dice side 6"""
        pygame.draw.rect(self.surface, BLACK, pygame.Rect(DICE_X +
                        DICE_GAP*dice_number + DICE_A*dice_number, DICE_Y, DICE_A, DICE_A), 2)
        pygame.draw.circle(self.surface, BLACK, (DICE_X + DICE_GAP*dice_number +
                        DICE_A/4 + dice_number*DICE_A, DICE_Y + 3*DICE_A/4), 5)
        pygame.draw.circle(self.surface, BLACK, (DICE_X + DICE_GAP*dice_number +
                        3*DICE_A/4 + dice_number*DICE_A, DICE_Y + 3*DICE_A/4), 5)
        pygame.draw.circle(self.surface, BLACK, (DICE_X + DICE_GAP*dice_number +
                        DICE_A/4 + dice_number*DICE_A, DICE_Y + DICE_A/2), 5)
        pygame.draw.circle(self.surface, BLACK, (DICE_X + DICE_GAP*dice_number +
                        3*DICE_A/4 + dice_number*DICE_A, DICE_Y + DICE_A/2), 5)
        pygame.draw.circle(self.surface, BLACK, (DICE_X + DICE_GAP*dice_number +
                        DICE_A/4 + dice_number*DICE_A, DICE_Y + DICE_A/4), 5)
        pygame.draw.circle(self.surface, BLACK, (DICE_X + DICE_GAP*dice_number +
                        3*DICE_A/4 + dice_number*DICE_A, DICE_Y + DICE_A/4), 5)

    def draw_dices(self):
        """Draw dices according to earlier methods"""
        for i in range(5):
            if self.dices.dice[i] == 1:
                self.dice_side_1(i)

            elif self.dices.dice[i] == 2:
                self.dice_side_2(i)

            elif self.dices.dice[i] == 3:
                self.dice_side_3(i)

            elif self.dices.dice[i] == 4:
                self.dice_side_4(i)

            elif self.dices.dice[i] == 5:
                self.dice_side_5(i)

            elif self.dices.dice[i] == 6:
                self.dice_side_6(i)

    def draw_dice_roller(self):
        """Draw an object that can roll the dice with a click """
        self.surface.blit(DICE_ROLLER, (550, 5))
        self.surface.blit(ROLL_TEXT, (550, 90))
        pygame.draw.rect(self.surface, GRAY, pygame.Rect(548, 3, 154, 110), 2)

    def draw_select_dice(self, dice_number):
        pygame.draw.rect(self.surface, RED, pygame.Rect(DICE_X + DICE_GAP*(dice_number-1)
                        + DICE_A*(dice_number-1)-4, DICE_Y-4, DICE_A+8, DICE_A+8), 2)

    def draw_rolled_dice(self):
        pygame.draw.rect(self.surface, WHITE, pygame.Rect(100, 0, 600, 115))

    def draw_unselect_dice(self):
        for dice_number in range(5):
            pygame.draw.rect(self.surface, WHITE, pygame.Rect(DICE_X +
                                                              DICE_GAP *
                                                              (dice_number) + DICE_A *
                                                              (dice_number) -
                                                              4, DICE_Y-4,
                                                              DICE_A+8, DICE_A+8), 2)

    def draw_all(self):
        """Draw all objects"""
        self.draw_dice_roller()
        self.draw_dices()
