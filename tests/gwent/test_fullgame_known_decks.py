import unittest
from unittest import mock
from gwent import *


class FullGameKnownDecksTest(unittest.TestCase):

    def setUp(self):
        test_decks = "data/test_decks.csv"
        file_name = "data/card_data.csv"
        faction = "Nilfgaardian"
        size = 22
        seed = 123

        self.deck = Deck(file_name, faction, size, seed)
        self.monster, self.nilf, self.northern, self.scoiatael = self.deck.create_deck_using_list(test_decks)

        self.playerNilf = Player("p1", "Nilfgaardian", self.nilf)
        self.playerMonster = Player("p2", "Monster", self.monster)
        self.playerNorth = Player("p3", "Northern", self.northern)
        self.playerScoi = Player("p4", "Scoiatael", self.scoiatael)
        self.board1 = Board(self.playerNilf)
        self.board2 = Board(self.playerMonster)
        self.board3 = Board(self.playerNorth)
        self.board4 = Board(self.playerScoi)

    #@mock.patch('FullGameKnownDecksTest.input', create=True)
    #def test_monster_vs_northern(self, mocked_input):
    #    mocked_input.side_effect = ['', '', '']
    #    game = GameState(self.board2, self.board3)
    #    game.starter = 0

        #game.game_loop()

    def test_monster_vs_scoiatael(self):
        pass

    def test_monster_vs_nilf(self):
        pass

    def test_northern_vs_scoiatael(self):
        pass

    def test_northern_vs_nilf(self):
        pass

    def test_nilf_vs_scoiatael(self):
        pass
