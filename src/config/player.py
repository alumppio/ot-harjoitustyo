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
            "Pair": None,
            "Two Pair": None,
            "Three of a Kind": None,
            "Four of a Kind": None,
            "Small Straight": None,
            "Large Straight": None,
            "Full House": None,
            "Chance": None,
            "Yatzy": None}

    def set_upper_part(self, dices: Dices, number: int):
        if self.minutes[number] is None:
            points = 0

            for dice_number in dices.dice:
                if dice_number == number:
                    points += dice_number

            self.minutes[number] = points

            if points == 0:
                self.minutes[number] = 'x'
        else:
            return

    def set_pair(self, dices: Dices):
        if self.minutes["Pair"] is None:
            pair = {number for number in dices.dice
                        if dices.dice.count(number) > 1}
            if len(pair) == 0:
                self.minutes["Pair"] = 'x'
            else:
                self.minutes["Pair"] = max(list(pair))*2

        else:
            return

    def set_two_pair(self, dices: Dices):
        if self.minutes["Two Pair"] is None:
            pair = {number for number in dices.dice
                        if dices.dice.count(number) > 1}

            if len(pair) <= 1:
                self.minutes["Two Pair"] = 'x'
            else:
                self.minutes["Two Pair"] = sorted(pair, reverse=True)[
                    0]*2 + sorted(pair, reverse=True)[1]*2
        else:
            return

    def set_3_of_a_kind(self, dices: Dices):
        if self.minutes["Three of a Kind"] is None:
            number_to_set = [number for number in dices.dice
                             if dices.dice.count(number) > 2]

            if len(number_to_set) == 0:
                self.minutes["Three of a Kind"] = 'x'
            else:
                self.minutes["Three of a Kind"] = number_to_set[0]*3
        else:
            return

    def set_4_of_a_kind(self, dices: Dices):
        if self.minutes["Four of a Kind"] is None:
            number_to_set = [number for number in dices.dice
                             if dices.dice.count(number) > 3]

            if len(number_to_set) == 0:
                self.minutes["Four of a Kind"] = 'x'
            else:
                self.minutes["Four of a Kind"] = number_to_set[0]*4
        else:
            return

    def set_full_house(self, dices: Dices):
        if self.minutes["Full House"] is None and len(set(dices.dice)) == 2:
            self.minutes["Full House"] = sum(dices.dice)

        else:
            self.minutes["Full House"] = 'x'
            return

    def set_small_straight(self, dices: Dices):
        if self.minutes["Small Straight"] is None and len(set(
                dices.dice)) == 5 and sum(dices.dice) == 15:
            self.minutes["Small Straight"] = 15
        else:
            self.minutes["Small Straight"] = 'x'

    def set_large_straight(self, dices: Dices):
        if self.minutes["Large Straight"] is None and len(set(
                dices.dice)) == 5 and sum(dices.dice) == 20:
            self.minutes["Large Straight"] = 20
        else:
            self.minutes["Large Straight"] = 'x'

    def set_yatzy(self, dices: Dices):
        if self.minutes["Yatzy"] is None and len(set(dices.dice)) == 1:
            self.minutes["Yatzy"] = 50
        else:
            self.minutes["Yatzy"] = 'x'

    def set_chance(self, dices: Dices):
        if self.minutes["Chance"] is None:
            self.minutes["Chance"] = sum(dices.dice)
        else:
            self.minutes["Chance"] = 'x'

    def check_upper(self):
        for i in range(1, 7):
            if self.minutes[i] is None:
                return False
        return True

    def check_total(self):
        for points in self.minutes.items():
            if points[1] is None:
                return False
        return True
    