from unittest import TestCase
from gwent.cards import *
from gwent import *


class TestScorchSpecialCard(TestCase):

    def setUp(self):
        self.unitCard1 = UnitCard("1", "dummy1", "Monster", 0, 11, False, False)
        self.unitCard2 = UnitCard("2", "dummy2", "Monster", 1, 11, False, False)
        self.unitHero = UnitCard("3", "dummy3", "Monster", 0, 11, True, True)
        self.scorchio = ScorchSpecialCard("4", "dummy4", "Monster", 0, 7, False, False)

        test_decks = "data/test_decks.csv"
        file_name = "data/card_data.csv"
        faction = "Nilfgaardian"
        size = 22
        seed = 123

        self.deck = Deck(file_name, faction, size, seed)
        monster, nilf, northern, scoiatael = self.deck.create_deck_using_list(test_decks)
        self.player1 = Player("p1", "Nilfgaardian", nilf)
        self.board1 = Board(self.player1)
        self.player2 = Player("p2", "Monster", monster)
        self.board2 = Board(self.player2)

    def test_place_card(self):
        self.board1.rows[0].append(self.unitCard1)
        self.board1.rows[0].append(self.unitHero)
        self.board2.rows[1].append(self.unitCard2)

        self.scorchio.place_card(self.board1, self.player1, self.player2, self.board2, None, None)
        self.assertTrue(self.player1.graveyard.__contains__(self.unitCard1))
        self.assertFalse(self.player1.graveyard.__contains__(self.unitHero))
        self.assertTrue(self.player2.graveyard.__contains__(self.unitCard2))
        self.assertTrue(self.board1.rows[0].__contains__(self.unitHero))

    def test_battlecry(self):
        self.board1.rows[0].append(self.unitCard1)
        self.board1.rows[0].append(self.unitHero)
        self.board2.rows[1].append(self.unitCard2)

        self.scorchio.battlecry(self.board1, self.player1, self.player2, self.board2, None, None)
        self.assertTrue(self.player1.graveyard.__contains__(self.unitCard1))
        self.assertFalse(self.player1.graveyard.__contains__(self.unitHero))
        self.assertTrue(self.player2.graveyard.__contains__(self.unitCard2))
        self.assertTrue(self.board1.rows[0].__contains__(self.unitHero))
