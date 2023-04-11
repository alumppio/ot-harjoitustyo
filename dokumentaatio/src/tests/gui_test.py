import unittest
import gui
import game


class TestGUI(unittest.TestCase):
    def setUp(self):
        self.dice = game.Dices()
        self.player = game.Player()
