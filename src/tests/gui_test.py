import unittest
import config.gui
import config.dice as dice
import config.player as player


class TestGUI(unittest.TestCase):
    def setUp(self):
        self.dice = dice.Dices()
        self.player = player.Player()
