import pygame
from config.dice import Dices
from config.visual.draw_dice import DrawDice
from config.visual.draw_yatzy import DrawYatzy
from repositories.constants import DICE_Y, DICE_X, DICE_A, DICE_GAP, SCREEN, FONT

class EventHandler:
    """Class to handle events in the game """

    def __init__(self, dices: Dices, players: list):
        self.dices = dices
        self.dices_to_hold = []
        self.players = players
        self.dice_drawer = DrawDice(self.dices, SCREEN)
        self.running = True
        self.yatzy_sheet = DrawYatzy(SCREEN, FONT)
        self.yatzy_sheet.draw_name(players, 1)

    def select_dice(self, dice_number):
        """Method to select the dice"""
        self.dice_drawer.draw_select_dice(dice_number)
        self.dices_to_hold.append(dice_number-1)

    def unselect_dice(self):
        """Method to unselect the dice"""
        self.dice_drawer.draw_unselect_dice()
        self.dices_to_hold = []

    def hold_dice(self, event):
        """Check if dices were selected"""
        if event.type == pygame.MOUSEBUTTONDOWN and DICE_Y <= event.pos[1] <= DICE_Y+DICE_A:
            if DICE_X <= event.pos[0] <= DICE_X+DICE_A:
                self.select_dice(1)
            elif DICE_X + DICE_GAP + DICE_A <= event.pos[0] <= DICE_X + DICE_GAP + DICE_A*2:
                self.select_dice(2)
            elif DICE_X + DICE_GAP*2 + DICE_A*2 <= event.pos[0] <= DICE_X + DICE_GAP*2 + DICE_A*3:
                self.select_dice(3)
            elif DICE_X + DICE_GAP*3 + DICE_A*3 <= event.pos[0] <= DICE_X + DICE_GAP*3 + DICE_A*4:
                self.select_dice(4)
            elif DICE_X + DICE_GAP*4 + DICE_A*4 <= event.pos[0] <= DICE_X + DICE_GAP*4 + DICE_A*5:
                self.select_dice(5)

    def undo_hold_dice(self, event):
        """Check if user changed his/her mind"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.unselect_dice()

    def roll_dice(self, event):
        """Check if the dice roller was clicked"""
        if event.type == pygame.MOUSEBUTTONDOWN and 3 <= event.pos[1] <= 113:
            if 548 <= event.pos[0] <= 702:
                self.dices.roll_dice(self.dices_to_hold)
                self.dice_drawer.draw_rolled_dice()
                self.dice_drawer.draw_all()
                self.dices_to_hold = []

    def set_upper_part(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and 122 <= event.pos[0] <= 199:
            if 169 <= event.pos[1] <= 192:
                self.yatzy_sheet.set_upper_part(1, self.dices, self.players)
                self.next_turn()
            if 193 <= event.pos[1] <= 216:
                self.yatzy_sheet.set_upper_part(2, self.dices, self.players)
                self.next_turn()
            if 217 <= event.pos[1] <= 240:
                self.yatzy_sheet.set_upper_part(3, self.dices, self.players)
                self.next_turn()
            if 241 <= event.pos[1] <= 264:
                self.yatzy_sheet.set_upper_part(4, self.dices, self.players)
                self.next_turn()
            if 265 <= event.pos[1] <= 288:
                self.yatzy_sheet.set_upper_part(5, self.dices, self.players)
                self.next_turn()
            if 289 <= event.pos[1] <= 312:
                self.yatzy_sheet.set_upper_part(6, self.dices, self.players)
                self.next_turn()

    def set_pair(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and 122 <= event.pos[0] <= 199:
            if 342 <= event.pos[1] <= 365:
                if self.yatzy_sheet.set_pair(self.dices, self.players):
                    self.next_turn()

    def set_two_pair(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and 122 <= event.pos[0] <= 199:
            if 366 <= event.pos[1] <= 389:
                if self.yatzy_sheet.set_two_pair(self.dices, self.players):
                    self.next_turn()

    def set_3_of_a_kind(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and 122 <= event.pos[0] <= 199:
            if 390 <= event.pos[1] <= 413:
                if self.yatzy_sheet.set_3_of_a_kind(self.dices, self.players):
                    self.next_turn()

    def set_4_of_a_kind(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and 122 <= event.pos[0] <= 199:
            if 414 <= event.pos[1] <= 437:
                if self.yatzy_sheet.set_4_of_a_kind(self.dices, self.players):
                    self.next_turn()

    def set_small_straight(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and 122 <= event.pos[0] <= 199:
            if 438 <= event.pos[1] <= 461:
                if self.yatzy_sheet.set_small_straight(self.dices, self.players):
                    self.next_turn()

    def set_large_straight(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and 122 <= event.pos[0] <= 199:
            if 462 <= event.pos[1] <= 485:
                if self.yatzy_sheet.set_large_straight(self.dices, self.players):
                    self.next_turn()

    def set_full_house(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and 122 <= event.pos[0] <= 199:
            if 486 <= event.pos[1] <= 509:
                if self.yatzy_sheet.set_full_house(self.dices, self.players):
                    self.next_turn()

    def set_chance(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and 122 <= event.pos[0] <= 199:
            if 510 <= event.pos[1] <= 533:
                if self.yatzy_sheet.set_chance(self.dices, self.players):
                    self.next_turn()

    def set_yatzy(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and 122 <= event.pos[0] <= 199:
            if 534 <= event.pos[1] <= 557:
                if self.yatzy_sheet.set_yatzy(self.dices, self.players):
                    self.next_turn()

    def set_lower_part(self, event):
        self.set_pair(event)
        self.set_two_pair(event)
        self.set_3_of_a_kind(event)
        self.set_4_of_a_kind(event)
        self.set_small_straight(event)
        self.set_large_straight(event)
        self.set_full_house(event)
        self.set_chance(event)
        self.set_yatzy(event)

    def set_total(self):
        if self.players.check_total():
            self.yatzy_sheet.draw_total_points(self.players)

        if self.players.check_upper():
            self.yatzy_sheet.draw_upper_points(self.players)

    def next_turn(self):
        self.dices.next_turn()
        self.dice_drawer.draw_rolled_dice()
        self.dice_drawer.draw_all()

    def quit(self, event):
        """Method to quit the game"""
        if event.type == pygame.QUIT:
            self.running = False
