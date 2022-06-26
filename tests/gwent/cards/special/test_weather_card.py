from unittest import TestCase
from gwent import *
from gwent.cards import *


class TestWeatherCard(TestCase):

    def setUp(self):
        self.unitCard1 = UnitCard("1", "dummy1", "Monster", 0, 11, False, False)
        self.unitCard3 = UnitCard("7", "dummy7", "Monster", 0, 8, False, False)
        self.unitCard2 = UnitCard("2", "dummy2", "Monster", 1, 11, False, False)
        self.unitHero = UnitCard("3", "dummy3", "Monster", 0, 11, True, True)
        self.frost = WeatherCard("4", "dummy4", "Monster", 0, -1, False, False)
        self.fog = WeatherCard("5", "dummy5", "Monster", 1, -1, False, False)
        self.rain = WeatherCard("6", "dummy6", "Monster", 2, -1, False, False)

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

    def test_constructor(self):
        self.assertTrue(self.frost.weather)

    def test_place_card(self):
        self.frost.place_card(self.board1, self.player1, self.player2, self.board2, 0, None)
        self.assertTrue(self.board1.rows[0].__contains__(self.frost))
        self.assertTrue(self.board2.rows[0].__contains__(self.frost))

    def test_frost(self):
        self.frost.place_card(self.board1, self.player1, self.player2, self.board2, 0, None)
        self.board1.rows[0].append(self.unitCard1)
        self.board1.rows[0].append(self.unitHero)
        self.board2.rows[0].append(self.unitCard3)
        self.board2.rows[1].append(self.unitCard2)

        self.assertEqual(self.unitCard1.get_active_strength(self.board1), 1)
        self.assertEqual(self.unitHero.get_active_strength(self.board1), 11)
        self.assertEqual(self.unitCard3.get_active_strength(self.board2), 1)
        self.assertEqual(self.unitCard2.get_active_strength(self.board2), 11)
