from unittest import TestCase
from gwent.cards import *
from gwent import *


class TestHornSpecialCard(TestCase):

    def setUp(self):
        self.unitCard1 = UnitCard("1", "dummy1", "Monster", 0, 11, False, False)
        self.unitCard2 = UnitCard("2", "dummy2", "Monster", 1, 7, False, False)
        self.unitHero = UnitCard("3", "dummy3", "Monster", 0, 10, True, True)
        self.horn = HornSpecialCard("4", "dummy4", "Monster", 0, 7, False, False)

        test_decks = "data/test_decks.csv"
        file_name = "data/card_data.csv"
        faction = "Nilfgaardian"
        size = 22
        seed = 123

        self.deck = Deck(file_name, faction, size, seed)
        monster, nilf, northern, scoiatael = self.deck.create_deck_using_list(test_decks)
        self.player1 = Player("p1", "Nilfgaardian", nilf)
        self.board1 = Board(self.player1)

    def test_constructor(self):
        self.assertTrue(self.horn.horn_special)

    def test_place_card(self):
        self.player1.hand.append(self.horn)
        self.horn.place_card(self.board1, None, 0, None)
        self.assertTrue(self.board1.rows[0].__contains__(self.horn))
        self.assertFalse(self.player1.hand.__contains__(self.horn))

    def test_bad_placement(self):
        # tests that when a horn special card is played with full slots, it is essentially discarded
        horn1 = HornSpecialCard("5", "dummy5", "Monster", 0, 0, False, False)
        horn2 = HornSpecialCard("6", "dummy6", "Monster", 1, 0, False, False)
        horn3 = HornSpecialCard("7", "dummy7", "Monster", 2, 0, False, False)

        self.board1.rows[0].append(horn1)
        self.board1.rows[1].append(horn2)
        self.board1.rows[2].append(horn3)

        self.horn.place_card(self.board1, None, None, 0)
        self.assertEqual(len(self.board1.rows[0]), 1)
        self.assertFalse(self.board1.rows[0].__contains__(self.horn))

    def test_get_row(self):
        self.assertEqual(self.horn.get_row(self.board1), [0, 1, 2])

        horn1 = HornSpecialCard("5", "dummy5", "Monster", 0, 0, False, False)
        horn2 = HornSpecialCard("6", "dummy6", "Monster", 1, 0, False, False)
        horn3 = HornSpecialCard("7", "dummy7", "Monster", 2, 0, False, False)

        self.board1.rows[0].append(horn1)
        self.board1.rows[1].append(horn2)
        self.board1.rows[2].append(horn3)

        self.assertEqual(len(self.horn.get_row(self.board1)), 0)

    def test_effect(self):
        self.board1.rows[0].append(self.horn)
        self.board1.rows[0].append(self.unitCard1)
        self.board1.rows[0].append(self.unitHero)
        self.board1.rows[1].append(self.unitCard2)

        self.assertEqual(self.horn.get_active_strength(self.board1), 0)
        self.assertEqual(self.unitCard1.get_active_strength(self.board1), 22)
        self.assertEqual(self.unitHero.get_active_strength(self.board1), 10)
        self.assertEqual(self.unitCard2.get_active_strength(self.board1), 7)
