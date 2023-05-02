import config.dice as Dices


class Player:
    def __init__(self):

        '''Idea for this dictionary was taken from chatGPT. This dictionary
        represents the yatzy sheet that contains all the information about the
        points'''
        self.minutes = {
            'Name': None,
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
        '''Method that sets the upper part meaning the values of keys 
        1 to 6 in the minutes dictionary'''
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
        '''Method that sets the value of the pair key in the 
        minutes dictionary'''
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
        '''Method that sets the value of the two pair key in the 
        minutes dictionary'''
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
        '''Method that sets the value of the 3 of a kind key 
        in the minutes dictionary'''
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
        '''Method that sets the value of the 4 of a kind key 
        in the minutes dictionary'''
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
        '''Method that sets the value of the full house key 
        in the minutes dictionary'''
        if self.minutes["Full House"] is None and len(set(dices.dice)) == 2:
            self.minutes["Full House"] = sum(dices.dice)

        else:
            self.minutes["Full House"] = 'x'
            return

    def set_small_straight(self, dices: Dices):
        '''Method that sets the value of the small straight key 
        in the minutes dictionary'''
        if self.minutes["Small Straight"] is None and len(set(
                dices.dice)) == 5 and sum(dices.dice) == 15:
            self.minutes["Small Straight"] = 15
        else:
            self.minutes["Small Straight"] = 'x'

    def set_large_straight(self, dices: Dices):
        '''Method that sets the value of the large straight key 
        in the minutes dictionary'''
        if self.minutes["Large Straight"] is None and len(set(
                dices.dice)) == 5 and sum(dices.dice) == 20:
            self.minutes["Large Straight"] = 20
        else:
            self.minutes["Large Straight"] = 'x'

    def set_yatzy(self, dices: Dices):
        '''Method that sets the value of the yatzy key in the 
        minutes dictionary'''
        if self.minutes["Yatzy"] is None and len(set(dices.dice)) == 1:
            self.minutes["Yatzy"] = 50
        else:
            self.minutes["Yatzy"] = 'x'

    def set_chance(self, dices: Dices):
        '''Method that sets the value of the chance key in the 
        minutes dictionary'''
        if self.minutes["Chance"] is None:
            self.minutes["Chance"] = sum(dices.dice)
        else:
            self.minutes["Chance"] = 'x'

    def check_upper(self):
        '''Method that checks if every key in the upper part 
        portion of minutes dictionary has a value'''
        for i in range(1, 7):
            if self.minutes[i] is None:
                return False
        return True

    def check_total(self):
        '''Method that checks if every key in the minutes 
        dictionary has a value'''
        for points in self.minutes.items():
            if points[1] is None:
                return False
        return True

    def upper_total_points(self):
        '''Method that sets the total points of the upper part
        section of a player'''
        points = 0
        for i in range(1, 7):
            if isinstance(self.minutes[i], int):
                points += self.minutes[i]
        if points >= 52:
            return points
        return 0

    def total_points(self):
        '''Method that sets the total points of the player'''
        total_points = 0
        for item in self.minutes.items():
            if isinstance(item[1], int) and not isinstance(item[0], int):
                total_points += item[0]
        total_points += self.upper_total_points()
        return total_points
