import random

class Dices:
    def __init__(self):
        self.dice = [random.randint(1,6) for i in range(5)]
        self.roll_amount = 1
    
    def roll_dice(self):
        if self.roll_amount<3:
            self.dice = [random.randint(1,6) for i in range(5)]
            self.roll_amount += 1
        else:
            return 



class Player:
    def __init__(self):

        #Idea for this dictionary was taken from chatGPT
        self.minutes = {
            "Ones": None,
            "Twos": None,
            "Threes": None,
            "Fours": None,
            "Fives": None,
            "Sixes": None,
            "Three of a Kind": None,
            "Four of a Kind": None,
            "Full House": None,
            "Small Straight": None,
            "Large Straight": None,
            "Yatzy": None,
            "Chance": None,
            }

    def Set_Ones(self, dices):
        if self.minutes['Ones'] is None:
            sum = 0

            for x in dices.dice:
                if x == 1:
                    sum += x

            self.minutes['Ones'] = sum