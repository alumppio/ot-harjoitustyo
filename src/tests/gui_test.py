import unittest
import pygame
import config.gui as gui
import config.dice as dice
import config.player as player
from repositories.constants import DICE_Y, DICE_X, DICE_A, DICE_GAP

class TestGUI(unittest.TestCase):
    def setUp(self):
        self.dice = dice.Dices()
        self.player = player.Player()
        self.player.minutes['Name'] = 'testuser'
        self.event_handler = gui.EventHandler(self.dice, self.player, 1)
        self.false_event1 = pygame.event.Event(pygame.KEYDOWN, {'pos':(0,0), 'key':'no_key'})
        self.false_event2 = pygame.event.Event(pygame.MOUSEMOTION, {'pos':(0,0), 'key':'no_key'})


    def test_select_dice_false_events(self):
        self.event_handler.hold_dice(self.false_event1)
        self.event_handler.hold_dice(self.false_event2)
        
        self.assertEqual(len(self.event_handler.dices_to_hold),0)

    def test_select_dice(self):
        for i in range(5):    
            event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {'pos': 
            (DICE_X+DICE_A/2+DICE_A*i+DICE_GAP*i, DICE_Y+DICE_A/2)})
            self.event_handler.hold_dice(event)

        self.assertNotEqual(len(self.event_handler.dices_to_hold),0)

    def test_undo_hold_dice(self):
        event = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_ESCAPE})
        self.event_handler.undo_hold_dice(event)

        self.assertEqual(len(self.event_handler.dices_to_hold),0)
    
    def test_false_events_undo_hold_dice(self):
        self.event_handler.undo_hold_dice(self.false_event1)
        self.event_handler.undo_hold_dice(self.false_event2)

        self.assertEqual(len(self.event_handler.dices_to_hold),0)

    def test_false_roll_dice(self):
        start_dice = self.event_handler.dices.dice
        self.event_handler.roll_dice(self.false_event1)
        self.event_handler.roll_dice(self.false_event2)

        self.assertEqual(self.event_handler.dices.dice, start_dice)

    def test_roll_dice(self):
        event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {'pos': 
        (600, 50)})
        self.event_handler.roll_dice(event)
        
        self.assertNotEqual(self.event_handler.dices.roll_amount,1)

    def test_set_upper_part(self):
        for i in range(6):
            event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {'pos': 
            (200, 170 + 25*i)})
            self.event_handler.set_upper_part(event)
            self.assertNotEqual(self.event_handler.player.minutes[i+1], None)


    def test_set_lower_part_false_events(self):
        self.event_handler.set_lower_part(self.false_event1)
        self.event_handler.set_lower_part(self.false_event2)

        self.assertEqual(self.event_handler.player.minutes['Pair'], None)
        self.assertEqual(self.event_handler.player.minutes['Two Pair'], None)
        self.assertEqual(self.event_handler.player.minutes['Three of a Kind'], None)
        self.assertEqual(self.event_handler.player.minutes['Four of a Kind'], None)
        self.assertEqual(self.event_handler.player.minutes['Small Straight'], None)
        self.assertEqual(self.event_handler.player.minutes['Large Straight'], None)
        self.assertEqual(self.event_handler.player.minutes['Full House'], None)
        self.assertEqual(self.event_handler.player.minutes['Chance'], None)
        self.assertEqual(self.event_handler.player.minutes['Yatzy'], None)


    def test_set_pair(self):
        event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {'pos': 
        (200, 350)})
        self.event_handler.dices.dice = [6,6,4,4,1]
        self.event_handler.set_pair(event)
        self.assertEqual(self.event_handler.player.minutes['Pair'], 12)


    def test_set_two_pair(self):
        event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {'pos': 
        (200, 370)})
        self.event_handler.dices.dice = [6,6,5,5,1]
        self.event_handler.set_two_pair(event)
        self.assertEqual(self.event_handler.player.minutes['Two Pair'], 22)


    def test_set_3_of_a_kind(self):
        event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {'pos': 
        (200, 400)})
        self.event_handler.dices.dice = [3,3,3,4,1]
        self.event_handler.set_3_of_a_kind(event)
        self.assertEqual(self.event_handler.player.minutes['Three of a Kind'], 9)

    
    def test_set_4_of_a_kind(self):
        event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {'pos': 
        (200, 420)})
        self.event_handler.dices.dice = [5,5,5,5,1]
        self.event_handler.set_4_of_a_kind(event)
        self.assertEqual(self.event_handler.player.minutes['Four of a Kind'], 20)


    def test_set_small_straight(self):
        event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {'pos': 
        (200, 450)})
        self.event_handler.dices.dice = [5,4,3,2,1]
        self.event_handler.set_small_straight(event)
        self.assertEqual(self.event_handler.player.minutes['Small Straight'], 15)

    def test_set_large_straight(self):
        event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {'pos': 
        (200, 480)})
        self.event_handler.dices.dice = [6,5,4,3,2]
        self.event_handler.set_large_straight(event)
        self.assertEqual(self.event_handler.player.minutes['Large Straight'], 20)

    def test_set_full_house(self):
        event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {'pos': 
        (200, 500)})
        self.event_handler.dices.dice = [6,6,6,2,2]
        self.event_handler.set_full_house(event)
        self.assertEqual(self.event_handler.player.minutes['Full House'], 22)

    def test_set_chance(self):
        event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {'pos': 
        (200, 530)})
        self.event_handler.dices.dice = [6,6,5,4,3]
        self.event_handler.set_chance(event)
        self.assertEqual(self.event_handler.player.minutes['Chance'], 24)

    def test_set_yatzy(self):
        event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {'pos': 
        (200, 540)})
        self.event_handler.dices.dice = [1,1,1,1,1]
        self.event_handler.set_yatzy(event)
        self.assertEqual(self.event_handler.player.minutes['Yatzy'], 50)

    def test_next_turn(self):
        self.event_handler.dices.roll_dice([])
        self.event_handler.next_turn()

        self.assertEqual(self.event_handler.running, False)
        self.assertEqual(self.event_handler.dices.roll_amount, 1)
