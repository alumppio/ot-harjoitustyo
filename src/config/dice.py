import random


class Dices:
    def __init__(self):
        ''' 
        Class that resembles the dices in Yatzy. 5 random integers between 1-6 in a list.
        '''

        self.dice = [random.randint(1, 6) for i in range(5)]
        self.roll_amount = 1

    def roll_dice(self, dices_to_hold):
        '''
        Method to roll the dice.

        Args:
            dices_to_hold (list) : what dices to hold when rolling.
        '''
        if self.roll_amount < 3:
            for dice_index in [0, 1, 2, 3, 4]:
                if dice_index not in dices_to_hold:
                    self.dice[dice_index] = random.randint(1, 6)

            self.roll_amount += 1
        else:
            return

    def next_turn(self):
        self.dice = [random.randint(1, 6) for i in range(5)]
        self.roll_amount = 1
