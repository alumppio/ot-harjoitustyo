import unittest
from config.end_game import EndGame
from config.gui import EventHandler
from config.dice import Dices
from config.player import Player
from services.connection import CONNECTION


class TestEndGame(unittest.TestCase):
    def setUp(self):
        self.players = [EventHandler(Dices(),Player(),1),
                        EventHandler(Dices(),Player(),2),
                        EventHandler(Dices(),Player(),3)]
        self.players[0].player.minutes['Yatzy'] = 50
        self.players[1].player.minutes['Large Straight'] = 20
        self.players[2].player.minutes['Pair'] = 12
        
        for i in range(3):
            self.players[i].player.minutes['Name'] = f'TestUser{i+1}'
        
        self.end_game = EndGame(self.players)

    def test_end_game_exists(self):
        self.assertNotEqual(self.end_game, None)

    def test_set_high_scores(self):
        self.end_game.set_high_scores()
        
        test_scores = CONNECTION.execute('''
            select name, score from High_Scores where name like 'TestUser%'
            ''')
        
        for score in test_scores:
            self.assertEqual(score[0].startswith('TestUser'), True)
            self.assertNotEqual(score[1], 0)
