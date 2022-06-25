from unittest import TestCase
from gwent import *
from gwent.cards import *


class TestSpecialCard(TestCase):

    def setUp(self):
        self.spec1 = SpecialCard("1", "dummy1", "Monster", 0, 8, False, False)
        self.spec2 = SpecialCard("2", "dummy2", "Monster", 0, 10, False, False)
        self.decoy = DecoyCard("2", "dummy2", "Monster", 0, 10, False, False)

        test_decks = "data/test_decks.csv"
        file_name = "data/card_data.csv"
        faction = "Nilfgaardian"
        size = 22
        seed = 123

        self.deck = Deck(file_name, faction, size, seed)
        monster, nilf, northern, scoiatael = self.deck.create_deck_using_list(test_decks)
        self.player1 = Player("p1", "Nilfgaardian", nilf)
        self.board1 = Board(self.player1)

    def test_place_card(self):
        self.player1.hand.append(self.spec1)
        self.player1.hand.append(self.spec2)
        self.player1.hand.append(self.decoy)
        self.assertEqual(len(self.player1.hand), 13)

        self.spec1.place_card(self.board1, self.player1, None, None, 0, None)
        self.spec2.place_card(self.board1, self.player1, None, None, 0, None)
        self.decoy.place_card(self.board1, self.player1, None, None, 0, None)

        self.assertFalse(self.player1.hand.__contains__(self.spec1))
        self.assertFalse(self.player1.hand.__contains__(self.spec2))
        self.assertFalse(self.player1.hand.__contains__(self.decoy))
        print(self.board1.get_data())
        self.assertEqual(len(self.board1.rows[0]), 3)

    def test_get_active_strength(self):
        self.assertEqual(self.spec1.get_active_strength(self.board1), 0)
        self.assertEqual(self.spec2.get_active_strength(self.board1), 0)
        self.assertEqual(self.decoy.get_active_strength(self.board1), 0)
