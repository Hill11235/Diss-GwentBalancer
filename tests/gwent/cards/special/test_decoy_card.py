from unittest import TestCase
from gwent import *
from gwent.cards import *


class TestDecoyCard(TestCase):

    def setUp(self):
        self.unitCard1 = UnitCard("1", "dummy1", "Monster", 0, 11, False, False)
        self.unitCard2 = UnitCard("3", "dummy2", "Monster", 1, 7, False, False)
        self.unitHero = UnitCard("3", "dummy3", "Monster", 0, 10, True, True)
        self.decoy = DecoyCard("4", "dummy4", "Monster", 0, 7, False, False)

        test_decks = "data/test_decks.csv"
        file_name = "data/card_data.csv"
        faction = "Nilfgaardian"
        size = 22
        seed = 123

        self.deck = Deck(file_name, faction, size, seed)
        monster, nilf, northern, scoiatael = self.deck.create_deck_using_list(test_decks)
        self.player1 = Player("p1", "Nilfgaardian", nilf)
        self.board1 = Board(self.player1)

    def test_get_targets(self):
        self.board1.rows[0].append(self.unitCard1)
        self.board1.rows[0].append(self.unitHero)
        self.board1.rows[1].append(self.unitCard2)

        targets = self.decoy.get_targets(self.board1)

        self.assertTrue(targets.__contains__(self.unitCard1))
        self.assertTrue(targets.__contains__(self.unitCard2))
        self.assertFalse(targets.__contains__(self.unitHero))
        self.assertEqual(len(targets), 2)

    def test_place_card(self):
        self.board1.rows[0].append(self.unitCard1)

        self.decoy.place_card(self.board1, None, self.unitCard1.row, self.unitCard1)
        self.assertTrue(self.player1.hand.__contains__(self.unitCard1))
        self.assertTrue(self.board1.rows[0].__contains__(self.decoy))
        self.assertFalse(self.player1.graveyard.__contains__(self.unitCard1))
        self.assertFalse(self.player1.hand.__contains__(self.decoy))

    def test_decoy_alone(self):
        self.assertEqual(len(self.player1.hand), 10)
        self.decoy.place_card(self.board1, None, 0, None)
        self.assertTrue(self.board1.rows[0].__contains__(self.decoy))
        self.assertEqual(len(self.player1.hand), 10)
