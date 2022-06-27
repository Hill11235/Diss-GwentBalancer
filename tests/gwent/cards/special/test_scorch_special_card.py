from unittest import TestCase
from gwent.cards import *
from gwent import *


class TestScorchSpecialCard(TestCase):

    def setUp(self):
        self.unitCard1 = UnitCard("1", "dummy1", "Monster", 0, 11, False, False)
        self.unitCard2 = UnitCard("2", "dummy2", "Monster", 0, 11, False, False)
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
        unito = UnitCard("2", "dummy2", "Monster", 1, 11, False, False)
        self.board1.rows[0].append(self.unitCard1)
        self.board1.rows[0].append(self.unitHero)
        self.board2.rows[1].append(unito)

        self.scorchio.place_card(self.board1, self.board2, None, None)
        self.assertTrue(self.player1.graveyard.__contains__(self.unitCard1))
        self.assertFalse(self.player1.graveyard.__contains__(self.unitHero))
        self.assertTrue(self.player2.graveyard.__contains__(unito))
        self.assertTrue(self.board1.rows[0].__contains__(self.unitHero))

    def test_battlecry(self):
        unito = UnitCard("2", "dummy2", "Monster", 1, 11, False, False)
        self.board1.rows[0].append(self.unitCard1)
        self.board1.rows[0].append(self.unitHero)
        self.board2.rows[1].append(unito)

        self.scorchio.battlecry(self.board1, self.board2, None, None)
        self.assertTrue(self.player1.graveyard.__contains__(self.unitCard1))
        self.assertFalse(self.player1.graveyard.__contains__(self.unitHero))
        self.assertTrue(self.player2.graveyard.__contains__(unito))
        self.assertTrue(self.board1.rows[0].__contains__(self.unitHero))

    def test_scorch_row(self):
        self.unitCard3 = UnitCard("5", "dummy5", "Monster", 0, 11, False, False)

        self.board1.rows[0].append(self.unitCard1)
        self.board1.rows[0].append(self.unitCard2)
        self.board1.rows[0].append(self.unitCard3)

        self.scorchio.scorch_row(self.board1, self.board1.rows[0], 11)

        self.assertEqual(len(self.board1.rows[0]), 0)

    def test_multiple(self):
        # test that scorch can be used to get rid of many cards with the same max effective strength
        unitCard3 = UnitCard("5", "dummy5", "Monster", 0, 11, False, False)
        unitCard4 = UnitCard("6", "dummy6", "Monster", 0, 11, False, False)
        unitCard5 = UnitCard("7", "dummy7", "Monster", 1, 11, False, False)
        unitCard6 = UnitCard("8", "dummy8", "Monster", 2, 11, False, False)
        unitCard7 = UnitCard("9", "dummy9", "Monster", 2, 11, False, False)

        self.board1.rows[0].append(self.unitCard1)
        self.board1.rows[0].append(self.unitCard2)
        self.board1.rows[0].append(unitCard3)
        self.board2.rows[0].append(unitCard4)
        self.board1.rows[1].append(unitCard5)
        self.board2.rows[2].append(unitCard6)
        self.board2.rows[2].append(unitCard7)

        self.scorchio.battlecry(self.board1, self.board2, None, None)

        self.assertFalse(self.board1.rows[0].__contains__(self.unitCard1))
        self.assertFalse(self.board1.rows[0].__contains__(self.unitCard2))
        self.assertFalse(self.board1.rows[0].__contains__(unitCard3))
        self.assertFalse(self.board2.rows[0].__contains__(unitCard4))
        self.assertFalse(self.board1.rows[1].__contains__(unitCard5))
        self.assertFalse(self.board2.rows[2].__contains__(unitCard6))
        self.assertFalse(self.board2.rows[2].__contains__(unitCard7))
