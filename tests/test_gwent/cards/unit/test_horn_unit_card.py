import os
from unittest import TestCase
from gwent import *
from gwent.cards import *
from gwent.data.card_db import CardDB


class TestHornUnitCard(TestCase):

    def setUp(self):
        self.unitCard1 = UnitCard("1", "dummy1", "Monster", 0, 11, False, False)
        self.unitCard2 = UnitCard("2", "dummy2", "Monster", 0, 12, False, False)
        self.unitHero = UnitCard("3", "dummy3", "Monster", 0, 10, True, True)
        self.horn1 = HornUnitCard("4", "dummy4", "Monster", 0, 7, False, False)
        self.horn2 = HornUnitCard("4", "dummy4", "Monster", 0, 4, False, False)

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
        pass

    def test_init(self):
        self.assertTrue(self.horn1.horn)

    def test_effect(self):
        self.board1.rows[0].append(self.unitCard1)
        self.board1.rows[0].append(self.unitCard2)
        self.board1.rows[0].append(self.unitHero)
        self.board1.rows[0].append(self.horn1)

        self.assertEqual(self.unitCard1.get_active_strength(self.board1), 22)
        self.assertEqual(self.unitCard2.get_active_strength(self.board1), 24)
        self.assertEqual(self.unitHero.get_active_strength(self.board1), 10)
        self.assertEqual(self.horn1.get_active_strength(self.board1), 7)

    def test_multiple_units(self):
        self.board1.rows[0].append(self.unitCard1)
        self.board1.rows[0].append(self.unitCard2)
        self.board1.rows[0].append(self.unitHero)
        self.board1.rows[0].append(self.horn1)
        self.board1.rows[0].append(self.horn2)

        self.assertEqual(self.unitCard1.get_active_strength(self.board1), 44)
        self.assertEqual(self.unitCard2.get_active_strength(self.board1), 48)
        self.assertEqual(self.unitHero.get_active_strength(self.board1), 10)
        self.assertEqual(self.horn1.get_active_strength(self.board1), 14)
        self.assertEqual(self.horn2.get_active_strength(self.board1), 8)
