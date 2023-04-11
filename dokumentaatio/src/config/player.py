import config.dice as Dices


class Player:
    def __init__(self):

        # Idea for this dictionary was taken from chatGPT
        self.minutes = {
            1: None,
            2: None,
            3: None,
            4: None,
            5: None,
            6: None,
            "Three of a Kind": None,
            "Four of a Kind": None,
            "Full House": None,
            "Small Straight": None,
            "Large Straight": None,
            "Yatzy": None,
            "Chance": None}

    def set_upper_part(self, dices: Dices, number: int):
        if self.minutes[number] is None:
            points = 0

            for dice_number in dices.dice:
                if dice_number == number:
                    points += dice_number

            self.minutes[number] = points
        else:
            return

    def set_three_of_a_kind(self, dices: Dices):
        if self.minutes["Three of a Kind"] is None:
            number_to_set = max(set(dices.dice), key=dices.dice.count)

            self.minutes["Three of a Kind"] = number_to_set*3
        else:
            return

    def set_four_of_a_kind(self, dices: Dices):
        if self.minutes["Four of a Kind"] is None:
            number_to_set = max(set(dices.dice), key=dices.dice.count)

            self.minutes["Four of a Kind"] = number_to_set*4
        else:
            return

    def set_full_house(self, dices: Dices):
        if self.minutes["Full House"] is None and len(set(dices.dice)) == 2:
            self.minutes["Full House"] = sum(dices.dice)
        else:
            return

    def set_straight(self, dices: Dices):
        if self.minutes["Large Straight"] is None and len(set(
                dices.dice)) == 5 and sum(dices.dice) == 20:
            self.minutes["Large Straight"] = sum(dices.dice)
        elif self.minutes["Small Straight"] is None and len(
                set(dices.dice)) == 5 and sum(dices.dice) == 15:
            self.minutes["Small Straight"] = sum(dices.dice)
        else:
            return

    def set_yatzy(self, dices: Dices):
        if self.minutes["Yatzy"] is None and len(set(dices.dice)) == 1:
            self.minutes["Yatzy"] = 50
        else:
            return

    def set_chance(self, dices: Dices):
        if self.minutes["Chance"] is None:
            self.minutes["Chance"] = sum(dices.dice)
        else:
            return
