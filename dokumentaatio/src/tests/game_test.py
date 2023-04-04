import unittest
import game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.Dice = game.Dices()

    def test_Dices(self):
        self.assertNotEqual(self.Dice, None)