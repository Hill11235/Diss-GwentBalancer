from unittest import TestCase
from gwent import *
from gwent.data.card_db import CardDB
from gwent.cards import *


class TestClearWeatherCard(TestCase):

    def setUp(self):
        self.unitCard1 = UnitCard("1", "dummy1", "Monster", 0, 11, False, False)
        self.unitCard3 = UnitCard("7", "dummy7", "Monster", 0, 8, False, False)
        self.unitCard2 = UnitCard("2", "dummy2", "Monster", 1, 11, False, False)
        self.unitHero = UnitCard("3", "dummy3", "Monster", 0, 11, True, True)
        self.frost = WeatherCard("4", "dummy4", "Monster", 0, -1, False, False)
        self.fog = WeatherCard("5", "dummy5", "Monster", 1, -1, False, False)
        self.rain = WeatherCard("6", "dummy6", "Monster", 2, -1, False, False)
        self.clear = ClearWeatherCard("8", "dummy8", "Monster", 0, -1, False, False)

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

    def test_place_card(self):
        self.player1.hand.append(self.clear)
        self.frost.place_card(self.board1, self.board2, 0, None)
        self.assertTrue(self.board1.rows[0].__contains__(self.frost))
        self.assertTrue(self.board2.rows[0].__contains__(self.frost))

        self.clear.place_card(self.board1, self.board2, 0, None)
        self.assertFalse(self.board1.rows[0].__contains__(self.frost))
        self.assertFalse(self.board2.rows[0].__contains__(self.frost))
        self.assertFalse(self.player1.hand.__contains__(self.clear))

    def test_battlecry(self):
        self.frost.place_card(self.board1, self.board2, 0, None)
        self.fog.place_card(self.board1, self.board2, 1, None)
        self.rain.place_card(self.board1, self.board2, 2, None)

        self.clear.battlecry(self.board1, self.board2, 0, None)

        self.assertFalse(self.board1.rows[0].__contains__(self.frost))
        self.assertFalse(self.board2.rows[0].__contains__(self.frost))
        self.assertFalse(self.board1.rows[1].__contains__(self.fog))
        self.assertFalse(self.board2.rows[1].__contains__(self.fog))
        self.assertFalse(self.board1.rows[2].__contains__(self.rain))
        self.assertFalse(self.board2.rows[2].__contains__(self.rain))

    def test_multiple_weather(self):
        frost1 = WeatherCard("1", "frost1", "Monster", 0, -1, False, False)
        frost2 = WeatherCard("1", "frost1", "Monster", 0, -1, False, False)
        frost3 = WeatherCard("1", "frost1", "Monster", 0, -1, False, False)
        frost4 = WeatherCard("1", "frost1", "Monster", 0, -1, False, False)

        self.board1.rows[0].append(frost1)
        self.board1.rows[0].append(frost2)
        self.board1.rows[0].append(frost3)
        self.board1.rows[0].append(frost4)
        self.assertEqual(len(self.board1.rows[0]), 4)

        self.clear.battlecry(self.board1, self.board2, 0, None)
        self.assertEqual(len(self.board1.rows[0]), 0)
        self.assertFalse(self.board1.rows[0].__contains__(frost1))
        self.assertFalse(self.board1.rows[0].__contains__(frost2))
        self.assertFalse(self.board1.rows[0].__contains__(frost3))
        self.assertFalse(self.board1.rows[0].__contains__(frost4))
