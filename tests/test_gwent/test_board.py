import unittest
import os
from gwent import *
from gwent.cards import *
from gwent.data.card_db import CardDB


class BoardTest(unittest.TestCase):

    def setUp(self):
        test_decks = "data/test_decks.csv"
        parent_dir = os.path.dirname(__file__)
        file_name = "./../../gwent/data/card_data.csv"
        faction = "Nilfgaardian"
        size = 22
        seed = 123

        self.card_db = CardDB(os.path.join(parent_dir, file_name))
        self.deck = Deck(self.card_db, faction, size, seed)
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

        card1.place_card(self.board1, self.board2, card1.row, None)
        card2.place_card(self.board2,  self.board1, card2.row, None)
        self.assertEqual(self.board1.score(), [8, 0, 0])
        self.assertEqual(self.board2.score(), [0, 5, 0])

    def test_clear_board(self):
        card1 = UnitCard("1", "dummy1", "Monster", 0, 8, False, False)
        card2 = UnitCard("2", "dummy2", "Northern", 1, 5, True, False)

        card1.place_card(self.board1, self.board2, card1.row, None)
        card2.place_card(self.board2, self.board1, card2.row, None)
        self.assertEqual(self.board1.score(), [8, 0, 0])
        self.assertEqual(self.board2.score(), [0, 5, 0])

        self.board1.clear_board()
        self.board2.clear_board()

        self.assertEqual(self.board1.score(), [0, 0, 0])
        self.assertEqual(self.board2.score(), [0, 0, 0])

        self.assertEqual(len(self.player1.graveyard), 1)
        self.assertEqual(len(self.player2.graveyard), 1)

    def test_arachas_muster_clear(self):
        muster1 = MusterCard("arachas1", "Arachas", "Monster", 0, 4, False, False)
        muster2 = MusterCard("arachas2", "Arachas", "Monster", 0, 4, False, False)
        muster3 = MusterCard("arachas3", "Arachas", "Monster", 0, 4, False, False)

        self.player1.hand.append(muster1)
        self.player1.hand.append(muster2)
        self.player1.hand.append(muster3)

        muster1.place_card(self.board1, self.board2, 0, None)
        self.assertTrue(self.board1.rows[0].__contains__(muster1))
        self.assertTrue(self.board1.rows[0].__contains__(muster2))
        self.assertTrue(self.board1.rows[0].__contains__(muster3))
        self.assertEqual(len(self.board1.rows[0]), 3)

        self.board1.clear_board()
        self.assertFalse(self.board1.rows[0].__contains__(muster1))
        self.assertFalse(self.board1.rows[0].__contains__(muster2))
        self.assertFalse(self.board1.rows[0].__contains__(muster3))

    def test_get_data(self):
        card1 = UnitCard("1", "dummy1", "Monster", 0, 8, False, False)
        card2 = UnitCard("2", "dummy2", "Northern", 1, 5, True, False)

        card1.place_card(self.board1, self.board2, card1.row, None)
        card2.place_card(self.board2, self.board1, card2.row, None)

        self.assertEqual(self.board1.get_data().get('total_score'), [8, 0, 0])
