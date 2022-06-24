import unittest
from gwent import *
from gwent.cards import *


class CardTest(unittest.TestCase):

    def setUp(self):
        self.card = Card("1", "dummy1", "Monster", 0, 8, False, False)

    def test_get_active_strength(self):
        self.assertEqual(self.card.get_active_strength(None), 8)

    def test_get_row(self):
        self.assertEqual(self.card.get_row(), [0])

    def test_get_targets(self):
        self.assertIsNone(self.card.get_targets(None, None))

    def test_destroy(self):
        test_decks = "data/test_decks.csv"
        file_name = "data/card_data.csv"
        faction = "Nilfgaardian"
        size = 22
        seed = 123

        deck = Deck(file_name, faction, size, seed)
        monster, nilf, northern, scoiatael = deck.create_deck_using_list(test_decks)

        player1 = Player("p1", "Nilfgaardian", nilf)
        board1 = Board(player1)
        board1.rows[0].append(self.card)

        self.card.destroy(board1, player1)
        self.assertTrue(player1.graveyard.__contains__(self.card))
        player1.graveyard.clear()

        board1.rows[0].append(self.card)
        self.card.destroy(board1, player1, True)
        self.assertFalse(player1.graveyard.__contains__(self.card))

    def test_get_data(self):
        card_dict = self.card.get_data()

        self.assertEqual(len(card_dict), 11)
        self.assertEqual(card_dict.get('card_id'), "1")
        self.assertEqual(card_dict.get('faction'), "Monster")
        self.assertEqual(card_dict.get('hero'), False)
        self.assertEqual(card_dict.get('horn'), False)