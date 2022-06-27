from unittest import TestCase
from gwent.cards import *
from gwent import *


class TestMusterCard(TestCase):

    def setUp(self):
        self.must1 = MusterCard("1", "dummy1", "Monster", 0, 8, False, False)
        self.must2 = MusterCard("2", "dummy1", "Monster", 0, 10, False, False)
        self.must3 = MusterCard("3", "dummy1", "Monster", 1, 7, False, False)
        self.must4 = MusterCard("4", "dummy1", "Monster", 1, 9, False, False)
        self.med1 = MedicCard("4", "med1", "Northern", 1, 4, False, False)

        test_decks = "data/test_decks.csv"
        file_name = "data/card_data.csv"
        faction = "Nilfgaardian"
        size = 22
        seed = 123

        self.deck = Deck(file_name, faction, size, seed)
        monster, nilf, northern, scoiatael = self.deck.create_deck_using_list(test_decks)
        self.player1 = Player("p1", "Nilfgaardian", nilf)
        self.board1 = Board(self.player1)

    def test_battlecry(self):
        # checks that all instances of a muster card are played from hand and deck
        self.player1.hand.append(self.must1)
        self.player1.hand.append(self.must2)
        self.player1.hand.append(self.must4)
        self.player1.deck.append(self.must3)

        # checks that all instances have been played to the correct rows and have been removed from the hand and deck.
        self.must1.place_card(self.board1, None, self.must1.row, None)
        self.assertTrue(self.board1.rows[0].__contains__(self.must1))
        self.assertTrue(self.board1.rows[0].__contains__(self.must2))
        self.assertTrue(self.board1.rows[1].__contains__(self.must3))
        self.assertTrue(self.board1.rows[1].__contains__(self.must4))
        self.assertFalse(self.player1.hand.__contains__(self.must1))
        self.assertFalse(self.player1.hand.__contains__(self.must2))
        self.assertFalse(self.player1.deck.__contains__(self.must3))
        self.assertFalse(self.player1.hand.__contains__(self.must4))
        self.assertEqual(len(self.board1.rows[0]), 2)
        self.assertEqual(len(self.board1.rows[1]), 2)

    def test_no_graveyard(self):
        # test that cards are not summoned from graveyard
        self.player1.hand.append(self.must1)
        self.player1.graveyard.append(self.must2)
        self.player1.graveyard.append(self.must4)
        self.player1.graveyard.append(self.must3)

        self.must1.place_card(self.board1, None, self.must1.row, None)
        self.assertTrue(self.board1.rows[0].__contains__(self.must1))
        self.assertTrue(self.player1.graveyard.__contains__(self.must2))
        self.assertTrue(self.player1.graveyard.__contains__(self.must3))
        self.assertTrue(self.player1.graveyard.__contains__(self.must4))
        self.assertEqual(len(self.board1.rows[0]), 1)
        self.assertEqual(len(self.board1.rows[1]), 0)

    def test_medic_summon(self):
        # tests that muster happens when medic summons card
        self.player1.hand.append(self.med1)
        self.player1.graveyard.append(self.must1)
        self.player1.hand.append(self.must2)
        self.player1.hand.append(self.must4)
        self.player1.deck.append(self.must3)

        self.med1.place_card(self.board1, None, self.med1.row, self.must1)
        self.assertTrue(self.board1.rows[0].__contains__(self.must1))
        self.assertTrue(self.board1.rows[0].__contains__(self.must2))
        self.assertTrue(self.board1.rows[1].__contains__(self.must3))
        self.assertTrue(self.board1.rows[1].__contains__(self.must4))
        self.assertTrue(self.board1.rows[1].__contains__(self.med1))
        self.assertFalse(self.player1.graveyard.__contains__(self.must1))
        self.assertFalse(self.player1.hand.__contains__(self.must2))
        self.assertFalse(self.player1.deck.__contains__(self.must3))
        self.assertFalse(self.player1.hand.__contains__(self.must4))
        self.assertEqual(len(self.board1.rows[0]), 2)
        self.assertEqual(len(self.board1.rows[1]), 3)
