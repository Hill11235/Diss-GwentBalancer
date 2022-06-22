import unittest
from gwent import *
from gwent.cards import *


class BoardTest(unittest.TestCase):

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
        self.board1 = Board(self.player1)
        self.board2 = Board(self.player2)

    def test_score(self):
        self.assertEqual(self.board1.score(), [0, 0, 0])
        self.assertEqual(self.board2.score(), [0, 0, 0])

        card1 = UnitCard("1", "dummy1", "Monster", 0, 8, False, False)
        card2 = UnitCard("2", "dummy2", "Northern", 1, 5, True, False)

        card1.place_card(self.board1, self.player1, self.player2, self.board2, card1.row, None)
        card2.place_card(self.board2, self.player2, self.player1, self.board1, card2.row, None)
        self.assertEqual(self.board1.score(), [8, 0, 0])
        self.assertEqual(self.board2.score(), [0, 5, 0])

    def test_clear_board(self):
        card1 = UnitCard("1", "dummy1", "Monster", 0, 8, False, False)
        card2 = UnitCard("2", "dummy2", "Northern", 1, 5, True, False)

        card1.place_card(self.board1, self.player1, self.player2, self.board2, card1.row, None)
        card2.place_card(self.board2, self.player2, self.player1, self.board1, card2.row, None)
        self.assertEqual(self.board1.score(), [8, 0, 0])
        self.assertEqual(self.board2.score(), [0, 5, 0])

        self.board1.clear_board()
        self.board2.clear_board()

        self.assertEqual(self.board1.score(), [0, 0, 0])
        self.assertEqual(self.board2.score(), [0, 0, 0])

        self.assertEqual(len(self.player1.graveyard), 1)
        self.assertEqual(len(self.player2.graveyard), 1)

    def test_get_data(self):
        card1 = UnitCard("1", "dummy1", "Monster", 0, 8, False, False)
        card2 = UnitCard("2", "dummy2", "Northern", 1, 5, True, False)

        card1.place_card(self.board1, self.player1, self.player2, self.board2, card1.row, None)
        card2.place_card(self.board2, self.player2, self.player1, self.board1, card2.row, None)

        self.assertEqual(self.board1.get_data().get('total_score'), [8, 0, 0])
