import os
from unittest import TestCase
from gwent import *
from gwent.data.card_db import CardDB
from gwent.cards import *


class TestTightBondCard(TestCase):

    def setUp(self):
        self.tight1 = TightBondCard("1", "dummy1", "Monster", 0, 10, False, False)
        self.tight2 = TightBondCard("2", "dummy1", "Monster", 0, 10, False, False)
        self.tight3 = TightBondCard("3", "dummy1", "Monster", 0, 10, False, False)

        test_decks = "data/test_decks.csv"
        parent_dir = os.path.dirname(__file__)
        file_name = "./../../../../gwent/data/card_data.csv"
        faction = "Nilfgaardian"
        size = 22
        seed = 123

        self.card_db = CardDB(os.path.join(parent_dir, file_name))
        self.deck = Deck(self.card_db, faction, size, seed)
        monster, nilf, northern, scoiatael = self.deck.create_deck_using_list(test_decks)
        self.player1 = Player("p1", "Nilfgaardian", nilf)
        self.board1 = Board(self.player1)

    def test_get_active_strength(self):
        self.board1.rows[0].append(self.tight1)
        self.assertEqual(self.tight1.get_active_strength(self.board1), 10)

        self.board1.rows[0].append(self.tight2)
        self.assertEqual(self.tight1.get_active_strength(self.board1), 20)
        self.assertEqual(self.tight2.get_active_strength(self.board1), 20)

        self.board1.rows[0].append(self.tight3)
        self.assertEqual(self.tight1.get_active_strength(self.board1), 30)
        self.assertEqual(self.tight2.get_active_strength(self.board1), 30)
        self.assertEqual(self.tight3.get_active_strength(self.board1), 30)

    def test_horn_and_morale(self):
        horn = HornUnitCard("4", "dummy2", "Monster", 0, 5, False, False)
        morale = MoraleBoostCard("5", "dummy3", "Monster", 0, 6, False, False)

        self.board1.rows[0].append(self.tight1)
        self.board1.rows[0].append(self.tight2)
        self.board1.rows[0].append(self.tight3)
        self.board1.rows[0].append(horn)
        self.board1.rows[0].append(morale)

        self.assertEqual(self.tight1.get_active_strength(self.board1), 62)
        self.assertEqual(self.tight2.get_active_strength(self.board1), 62)
        self.assertEqual(self.tight3.get_active_strength(self.board1), 62)
        self.assertEqual(horn.get_active_strength(self.board1), 6)
        self.assertEqual(morale.get_active_strength(self.board1), 12)
