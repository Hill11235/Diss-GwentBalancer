from unittest import TestCase
from gwent import *
from gwent.data.card_db import CardDB
from gwent.cards import *


class TestScorchUnitCard(TestCase):

    def setUp(self):
        self.unitCard1 = UnitCard("1", "dummy1", "Monster", 0, 11, False, False)
        self.unitHero = UnitCard("2", "dummy2", "Monster", 0, 10, True, True)
        self.unitCard2 = UnitCard("5", "dummy5", "Monster", 0, 7, False, False)
        self.med1 = MedicCard("3", "med1", "Northern", 0, 4, False, False)
        self.scorchio = ScorchUnitCard("4", "dummy4", "Monster", 0, 10, False, False)
        self.unitCard3 = UnitCard("6", "dummy6", "Monster", 0, 11, False, False)

        test_decks = "data/test_decks.csv"
        file_name = "card_data.csv"
        faction = "Nilfgaardian"
        size = 22
        seed = 123

        self.card_db = CardDB(file_name)
        self.deck = Deck(self.card_db, faction, size, seed)
        monster, nilf, northern, scoiatael = self.deck.create_deck_using_list(test_decks)
        self.player1 = Player("p1", "Nilfgaardian", nilf)
        self.board1 = Board(self.player1)
        self.player2 = Player("p2", "Monster", monster)
        self.board2 = Board(self.player2)

    def test_battlecry(self):
        self.board2.rows[0].append(self.unitCard1)
        self.board2.rows[0].append(self.unitCard2)
        self.assertTrue(len(self.board2.rows[0]), 2)

        self.scorchio.place_card(self.board1, self.board2, self.scorchio.row, None)
        self.assertTrue(len(self.board1.rows[0]), 1)
        self.assertTrue(len(self.board2.rows[0]), 1)
        self.assertTrue(self.player2.graveyard.__contains__(self.unitCard1))
        self.assertFalse(self.player2.graveyard.__contains__(self.unitCard2))

    def test_against_hero(self):
        self.board2.rows[0].append(self.unitHero)
        self.board2.rows[0].append(self.unitCard2)
        self.assertTrue(len(self.board2.rows[0]), 2)

        self.scorchio.place_card(self.board1, self.board2, self.scorchio.row, None)
        self.assertTrue(len(self.board1.rows[0]), 1)
        self.assertTrue(len(self.board2.rows[0]), 1)
        self.assertTrue(self.player2.graveyard.__contains__(self.unitCard2))
        self.assertFalse(self.player2.graveyard.__contains__(self.unitHero))
        self.assertTrue(self.board2.rows[0].__contains__(self.unitHero))

    def test_medic(self):
        self.board2.rows[0].append(self.unitCard1)
        self.board2.rows[0].append(self.unitCard2)
        self.board2.rows[0].append(self.unitCard3)
        self.assertTrue(len(self.board2.rows[0]), 3)

        self.player1.graveyard.append(self.scorchio)
        self.med1.place_card(self.board1, self.board2, self.med1.row, self.scorchio)
        self.assertTrue(len(self.board1.rows[0]), 2)
        self.assertTrue(len(self.board2.rows[0]), 1)
        self.assertTrue(self.player2.graveyard.__contains__(self.unitCard1))
        self.assertTrue(self.player2.graveyard.__contains__(self.unitCard3))
        self.assertFalse(self.player2.graveyard.__contains__(self.unitCard2))

        self.assertTrue(self.board2.rows[0].__contains__(self.unitCard2))

    def test_scorch_row(self):
        self.unitCard3 = UnitCard("5", "dummy5", "Monster", 0, 11, False, False)

        self.board2.rows[0].append(self.unitCard1)
        self.board2.rows[0].append(self.unitCard2)
        self.board2.rows[0].append(self.unitCard3)

        self.scorchio.scorch_row(self.board2, self.board2.rows[0], 11)

        self.assertEqual(len(self.board2.rows[0]), 1)
        self.assertTrue(self.board2.rows[0].__contains__(self.unitCard2))
        self.assertFalse(self.board2.rows[0].__contains__(self.unitCard1))
        self.assertFalse(self.board2.rows[0].__contains__(self.unitCard3))
        self.assertTrue(self.player2.graveyard.__contains__(self.unitCard1))
        self.assertTrue(self.player2.graveyard.__contains__(self.unitCard3))

    def test_weather_combo(self):
        frost = WeatherCard("11", "dummyWeather", "Neutral", 0, -1, False, False)

        self.board2.rows[0].append(self.unitHero)
        self.board2.rows[0].append(self.unitCard1)
        self.board2.rows[0].append(self.unitCard2)
        self.board2.rows[0].append(self.unitCard3)

        self.assertTrue(self.board2.rows[0].__contains__(self.unitCard2))

        frost.place_card(self.board1, self.board2, 0, None)

        self.scorchio.place_card(self.board1, self.board2, self.scorchio.row, None)

        self.assertTrue(self.board2.rows[0].__contains__(self.unitHero))
        self.assertFalse(self.board2.rows[0].__contains__(self.unitCard1))
        self.assertFalse(self.board2.rows[0].__contains__(self.unitCard2))
        self.assertFalse(self.board2.rows[0].__contains__(self.unitCard3))
