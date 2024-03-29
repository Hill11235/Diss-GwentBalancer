import os
from unittest import TestCase
from gwent.cards import *
from gwent.data.card_db import CardDB
from gwent import *


class TestSpyCard(TestCase):

    def setUp(self):
        self.med1 = MedicCard("3", "med1", "Northern", 0, 4, False, False)
        self.spy = SpyCard("4", "dummy4", "Monster", 0, 10, False, False)

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
        self.player2 = Player("p2", "Monster", monster)
        self.board2 = Board(self.player2)

    def test_battlecry(self):
        hand_size_before = len(self.player1.hand)
        self.spy.battlecry(self.board1, self.board2, self.spy.row, None)
        self.assertEqual(len(self.player1.hand), hand_size_before + 2)

    def test_place_card(self):
        hand_size_before = len(self.player1.hand)
        self.spy.place_card(self.board1, self.board2, self.spy.row, None)
        self.assertTrue(self.board2.rows[0].__contains__(self.spy))
        self.assertFalse(self.board1.rows[0].__contains__(self.spy))
        self.assertEqual(len(self.player1.hand), hand_size_before + 2)

    def test_medic_use(self):
        self.player1.graveyard.append(self.spy)
        hand_size_before = len(self.player1.hand)
        self.med1.place_card(self.board1, self.board2, self.med1.row, self.spy)

        self.assertTrue(self.board2.rows[0].__contains__(self.spy))
        self.assertFalse(self.board1.rows[0].__contains__(self.spy))
        self.assertEqual(len(self.player1.hand), hand_size_before + 2)

    def test_dummy_switch(self):
        decoy = DecoyCard("5", "dec", "Northern", 0, -1, False, False)

        self.board1.rows[0].append(self.spy)
        decoy.place_card(self.board1, self.board2, self.spy.row, self.spy)

        self.assertTrue(self.board1.rows[0].__contains__(decoy))
        self.assertFalse(self.board1.rows[0].__contains__(self.spy))
        self.assertTrue(self.player1.hand.__contains__(self.spy))

        self.spy.place_card(self.board1, self.board2, self.spy.row, None)
        self.assertEqual(len(self.player1.hand), 12)
        self.assertTrue(self.board2.rows[0].__contains__(self.spy))

    def test_deck_empty(self):
        # test that spy doesn't crash game if the player's deck is empty
        self.player1.hand.clear()
        self.player1.deck.clear()
        self.assertEqual(len(self.player1.hand), 0)
        self.assertEqual(len(self.player1.deck), 0)

        self.player1.hand.append(self.spy)
        self.spy.place_card(self.board1, self.board2, self.spy.row, None)
        self.assertTrue(self.board2.rows[self.spy.row].__contains__(self.spy))
        self.assertEqual(len(self.player1.hand), 0)
        self.assertEqual(len(self.player1.deck), 0)
