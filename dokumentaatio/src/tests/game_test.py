import unittest
import config.dice as dice
import config.player as player


class TestGame(unittest.TestCase):
    def setUp(self):
        self.Dice = dice.Dices()
        self.Player = player.Player()

    def test_dices(self):
        self.assertNotEqual(self.Dice, None)

    def test_roll_dice(self):
        another_dice = dice.Dices()
        another_dice.roll_dice([])

        self.assertEqual(another_dice.roll_amount, 2)

    def test_max_dice_roll(self):
        another_dice = dice.Dices()
        another_dice.roll_dice([0, 1, 2])

        for i in range(5):
            another_dice.roll_dice([])

        self.assertEqual(another_dice.roll_amount, 3)

    def test_player(self):
        self.assertNotEqual(self.Player, None)

    def test_set_upper_part(self):
        self.Player.set_upper_part(self.Dice, 1)
        for i in range(1, 7):
            self.Player.set_upper_part(self.Dice, i)
            self.assertNotEqual(self.Player.minutes[i], None)

    def test_set_pair(self):
        another_dice = dice.Dices()
        another_dice.dice = [4, 4, 6, 6, 2]
        self.Player.set_pair(another_dice)
        self.assertEqual(self.Player.minutes["Pair"], 12)

    def test_set_two_pair(self):
        another_dice = dice.Dices()
        another_dice.dice = [5, 5, 6, 6, 2]
        self.Player.set_two_pair(another_dice)
        self.assertEqual(self.Player.minutes["Two Pair"], 22)

    def test_set_3_of_a_kind(self):
        another_dice = dice.Dices()
        another_dice.dice = [1, 1, 1, 2, 3]

        self.Player.set_3_of_a_kind(another_dice)
        self.Player.set_3_of_a_kind(another_dice)
        self.assertNotEqual(self.Player.minutes["Three of a Kind"], None)

    def test_set_4_of_a_kind(self):
        another_dice = dice.Dices()
        another_dice.dice = [4, 4, 4, 4, 2]

        self.Player.set_4_of_a_kind(another_dice)
        self.Player.set_4_of_a_kind(another_dice)
        self.assertNotEqual(self.Player.minutes["Four of a Kind"], None)

    def test_set_full_house(self):
        another_dice = dice.Dices()
        another_dice.dice = [4, 4, 4, 2, 2]

        self.Player.set_full_house(another_dice)
        self.Player.set_full_house(another_dice)
        self.assertNotEqual(self.Player.minutes["Full House"], None)

    def test_set_small_straight(self):
        another_dice = dice.Dices()
        another_dice.dice = [1, 2, 3, 4, 5]

        self.Player.set_small_straight(another_dice)
        self.Player.set_small_straight(another_dice)
        self.assertNotEqual(self.Player.minutes["Small Straight"], None)

    def test_set_large_straight(self):
        another_dice = dice.Dices()
        another_dice.dice = [2, 3, 4, 5, 6]

        self.Player.set_large_straight(another_dice)
        self.Player.set_large_straight(another_dice)
        self.assertNotEqual(self.Player.minutes["Large Straight"], None)

    def test_set_yatzy(self):
        another_dice = dice.Dices()
        another_dice.dice = [1, 1, 1, 1, 1]

        self.Player.set_yatzy(another_dice)
        self.Player.set_yatzy(another_dice)
        self.assertNotEqual(self.Player.minutes["Yatzy"], None)

    def test_set_chance(self):
        self.Player.set_chance(self.Dice)
        self.Player.set_chance(self.Dice)
        self.assertNotEqual(self.Player.minutes["Chance"], None)
