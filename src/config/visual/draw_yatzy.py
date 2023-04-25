import pygame
from repositories.constants import YATZY_PAPER, GRAY, WHITE, BLACK


class DrawYatzy:
    def __init__(self, surface, font):
        self.surface = surface
        self.surface.blit(YATZY_PAPER, (5, 90))
        self.font = font
        tip_1 = self.font.render(
            'MOUSE1 TO ROLL OR SELECT DICE', True, GRAY, WHITE)
        tip_2 = self.font.render('MOUSE1 TO SET SCORES', True, GRAY, WHITE)
        tip_3 = self.font.render(
            'UNDO SELECTION WITH ESCAPE', True, GRAY, WHITE)
        tips = [tip_1, tip_2, tip_3]

        for i in range(3):
            self.surface.blit(tips[i], pygame.Rect(590, 150+30*i, 20, 30))

    def set_upper_part(self, number, dice, player):
        if player.minutes[number] is None:
            player.set_upper_part(dice, number)
            points = self.font.render(
                str(player.minutes[number]), True, BLACK, WHITE)
            self.surface.blit(points, pygame.Rect(
                152, 170+(number-1)*25, 100, 25))
            return True

        return False

    def set_pair(self, dice, player):
        if player.minutes["Pair"] is None:
            player.set_pair(dice)
            points = self.font.render(
                str(player.minutes["Pair"]), True, BLACK, WHITE)
            self.surface.blit(points, pygame.Rect(152, 345, 100, 25))
            return True

        return False

    def set_two_pair(self, dice, player):
        if player.minutes["Two Pair"] is None:
            player.set_two_pair(dice)
            points = self.font.render(
                str(player.minutes["Two Pair"]), True, BLACK, WHITE)
            self.surface.blit(points, pygame.Rect(152, 369, 100, 25))

    def set_3_of_a_kind(self, dice, player):
        if player.minutes["Three of a Kind"] is None:
            player.set_3_of_a_kind(dice)
            points = self.font.render(
                str(player.minutes["Three of a Kind"]), True, BLACK, WHITE)
            self.surface.blit(points, pygame.Rect(152, 393, 100, 25))
            return True

        return False

    def set_4_of_a_kind(self, dice, player):
        if player.minutes["Four of a Kind"] is None:
            player.set_4_of_a_kind(dice)
            points = self.font.render(
                str(player.minutes["Four of a Kind"]), True, BLACK, WHITE)
            self.surface.blit(points, pygame.Rect(152, 417, 100, 25))
            return True

        return False

    def set_small_straight(self, dice, player):
        if player.minutes["Small Straight"] is None:
            player.set_small_straight(dice)
            points = self.font.render(
                str(player.minutes["Small Straight"]), True, BLACK, WHITE)
            self.surface.blit(points, pygame.Rect(152, 443, 100, 25))
            return True

        return False

    def set_large_straight(self, dice, player):
        if player.minutes["Large Straight"] is None:
            player.set_large_straight(dice)
            points = self.font.render(
                str(player.minutes["Large Straight"]), True, BLACK, WHITE)
            self.surface.blit(points, pygame.Rect(152, 467, 100, 25))
            return True

        return False

    def set_full_house(self, dice, player):
        if player.minutes["Full House"] is None:
            player.set_full_house(dice)
            points = self.font.render(
                str(player.minutes["Full House"]), True, BLACK, WHITE)
            self.surface.blit(points, pygame.Rect(152, 491, 100, 25))
            return True

        return False

    def set_chance(self, dice, player):
        if player.minutes["Chance"] is None:
            player.set_chance(dice)
            points = self.font.render(
                str(player.minutes["Chance"]), True, BLACK, WHITE)
            self.surface.blit(points, pygame.Rect(152, 515, 100, 25))
            return True

        return False

    def set_yatzy(self, dice, player):
        if player.minutes["Yatzy"] is None:
            player.set_yatzy(dice)
            points = self.font.render(
                str(player.minutes["Yatzy"]), True, BLACK, WHITE)
            self.surface.blit(points, pygame.Rect(152, 538, 100, 25))
            return True

        return False
