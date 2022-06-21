import unittest
from gwent.deck import Deck
from gwent.player import Player


class PlayerTest(unittest.TestCase):

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

    def test_initial_player_set_up(self):
        self.assertFalse(self.player1.passed)
        self.assertEqual(self.player1.faction, "Nilfgaardian")
        self.assertEqual(self.player1.name, "p1")
        self.assertEqual(len(self.player1.hand), 10)
        self.assertEqual(len(self.player1.graveyard), 0)
        self.assertEqual(len(self.player1.deck), 6)

    def test_draw_card(self):
        self.player1.draw_card()
        self.assertEqual(len(self.player1.hand), 11)
        self.assertEqual(len(self.player1.graveyard), 0)
        self.assertEqual(len(self.player1.deck), 5)

    def test_pass_and_reset_round(self):
        self.player2.pass_round()
        self.assertTrue(self.player2.passed)
        self.player2.reset_round()
        self.assertFalse(self.player2.passed)

    def test_lose_round(self):
        self.player2.lose_round()
        self.assertEqual(self.player2.lives, 1)

    def test_get_player_data(self):
        # test format and correct key/value pairs
        pass
