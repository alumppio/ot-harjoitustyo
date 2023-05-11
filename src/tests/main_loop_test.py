import unittest
import config.gui as gui
import config.dice as dice
import config.player as player
from config.main_loop import MainLoop


class TestMainLoop(unittest.TestCase):
    def setUp(self):
        self.players = [gui.EventHandler(dice.Dices(), player.Player(), 1),
                        gui.EventHandler(dice.Dices(), player.Player(), 2),
                        gui.EventHandler(dice.Dices(), player.Player(), 3)]
        self.set_test_names()
        self.main_loop = MainLoop(self.players)

    def set_test_names(self):
        for i in range(3):
            self.players[i].player.minutes['Name'] = f'TestUser{i+1}'

    def test_names_set(self):
        for i in range(3):
            self.assertNotEqual(self.players[i].player.minutes['Name'], None)

    def test_main_loop_exists(self):
        self.assertNotEqual(self.main_loop, None)
        self.assertEqual(self.main_loop.running, True)

    def test_check_if_loop_done_works(self):
        self.main_loop.check_if_done()
        self.assertNotEqual(self.main_loop.running, False)
