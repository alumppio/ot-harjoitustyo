import unittest
import pygame
from config.game_setup import Setup
from config.player import Player


class TestGameSetup(unittest.TestCase):
    def setUp(self):
        self.game_setup = Setup()
        self.game_setup.name = 'TEST'
        self.game_setup.players_amount = '4'

    def test_setup_exists(self):
        self.assertNotEqual(self.game_setup, None)

    def test_name_setup_loop_backspace(self):
        test_name = 'TEST'
        event = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_BACKSPACE})
        pygame.event.post(event)
        self.game_setup.name_setup_loop(Player(), 1)

        self.assertNotEqual(self.game_setup.name, test_name)

    def test_name_setup_loop_typing(self):
        test_name = 'TESTT'
        event = pygame.event.Event(
            pygame.KEYDOWN, {'key': 715517, 'unicode': 't'})
        pygame.event.post(event)
        self.game_setup.name_setup_loop(Player(), 1)

        self.assertEqual(self.game_setup.name, test_name)

    def test_name_setup_loop_enter(self):
        player = Player()
        event = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_RETURN})
        pygame.event.post(event)
        self.game_setup.name_setup_loop(player, 1)

        self.assertEqual(self.game_setup.name, player.minutes['Name'])
        self.assertEqual(self.game_setup.running, False)

    def test_players_amount_backspace(self):
        event = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_BACKSPACE})
        pygame.event.post(event)
        self.game_setup.amount_of_players_loop()

        self.assertEqual(self.game_setup.players_amount, '')

    def test_players_amount_typing(self):
        event_1 = pygame.event.Event(
            pygame.KEYDOWN, {'key': pygame.K_BACKSPACE})
        pygame.event.post(event_1)
        event_2 = pygame.event.Event(
            pygame.KEYDOWN, {'key': 1234, 'unicode': '2'})
        pygame.event.post(event_2)
        self.game_setup.amount_of_players_loop()

        self.assertEqual(self.game_setup.players_amount, '2')

    def test_players_amount_enter(self):
        event = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_RETURN})
        pygame.event.post(event)
        self.game_setup.amount_of_players_loop()

        self.assertEqual(self.game_setup.running, False)
