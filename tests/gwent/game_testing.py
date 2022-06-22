import unittest
from gwent import *


class GameTest(unittest.TestCase):

    def setUp(self):
        test_decks = "data/test_decks.csv"
        file_name = "data/card_data.csv"
        faction = "Nilfgaardian"
        size = 22
        seed = 123

        self.deck = Deck(file_name, faction, size, seed)
        self.monster, self.nilf, self.northern, self.scoiatael = self.deck.create_deck_using_list(test_decks)

        self.player1 = Player("p1", "Nilfgaardian", self.nilf)
        self.player2 = Player("p2", "Monster", self.monster)
        # boards
        # game
        pass

    # TODO test that games can be set up and that the initial board are empty and score are zero, hand sizes are 10
