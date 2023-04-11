import random


class Dices:
    def __init__(self):
        self.dice = [random.randint(1, 6) for i in range(5)]
        self.roll_amount = 1

    def roll_dice(self, dices_to_hold):
        if self.roll_amount < 3:
            for dice_index in [0, 1, 2, 3, 4]:
                if dice_index not in dices_to_hold:
                    self.dice[dice_index] = random.randint(1, 6)

            self.roll_amount += 1
        else:
            return