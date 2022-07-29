import os
from unittest import TestCase
from gwent.cards import *
from gwent.data.card_db import CardDB
from gwent import *


class TestMoraleBoostCard(TestCase):

    def setUp(self):
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

    def test_init(self):
        morale = MoraleBoostCard("1", "morale1", "Monster", 0, 5, False, False)
        self.assertTrue(morale.morale_boost)

    def test_effect(self):
        morale = MoraleBoostCard("1", "morale1", "Monster", 0, 1, False, False)
        unit1 = UnitCard("2", "unit1", "Monster", 0, 5, False, False)
        unit2 = UnitCard("3", "unit2", "Monster", 0, 5, False, False)
        hero = UnitCard("4", "unit3", "Monster", 0, 10, True, False)
        horn = HornUnitCard("5", "horn1", "Monster", 0, 1, False, False)

        # create units and add to row, check strength
        self.board1.rows[0].append(unit1)
        self.board1.rows[0].append(unit2)
        self.board1.rows[0].append(hero)
        self.assertEqual(unit1.get_active_strength(self.board1), 5)
        self.assertEqual(unit2.get_active_strength(self.board1), 5)
        self.assertEqual(hero.get_active_strength(self.board1), 10)

        # add morale and check strength updates
        self.board1.rows[0].append(morale)
        self.assertEqual(unit1.get_active_strength(self.board1), 6)
        self.assertEqual(unit2.get_active_strength(self.board1), 6)
        self.assertEqual(hero.get_active_strength(self.board1), 10)
        self.assertEqual(morale.get_active_strength(self.board1), 1)

        # add horn and check strength updates
        self.board1.rows[0].append(horn)
        self.assertEqual(unit1.get_active_strength(self.board1), 12)
        self.assertEqual(unit2.get_active_strength(self.board1), 12)
        self.assertEqual(hero.get_active_strength(self.board1), 10)
        self.assertEqual(morale.get_active_strength(self.board1), 2)
        self.assertEqual(horn.get_active_strength(self.board1), 2)
