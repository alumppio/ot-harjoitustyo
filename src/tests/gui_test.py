import unittest
import config.main_loop as main
import config.dice as dice
import config.player as player


class TestGUI(unittest.TestCase):
    def setUp(self):
        self.dice = dice.Dices()
        self.player = player.Player()
        self.game = main.MainLoop(self.dice, self.player)

    def test_game_loop(self):
        self.game.handle_events()
