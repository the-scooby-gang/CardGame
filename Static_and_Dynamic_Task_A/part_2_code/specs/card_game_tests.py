import unittest
from src.card import Card
from src.card_game import CardGame as cardgame
from src.card_game import *

class TestCardGame(unittest.TestCase):
            
    
    def setUp(self):
        self.card=Card('hearts',5)
        self.card1=Card('spades',1)
        self.card2=Card('diamonds',4)
        self.game1=CardGame()
        

    def test_ace_finder(self):
        result=self.game1.check_for_ace(self.card1)
        self.assertEqual(True,result)

    def test_highest_card(self):
        result=self.game1.highest_card(self.card1,self.card2)
        self.assertEqual(4,result.value)

    def test_cards_total(self):
        cards=[self.card1,self.card2]
        result=self.game1.cards_total(cards)
        self.assertEqual("You have a total of 5",result)