from unittest import TestCase
from gwent.cards import *
from gwent.data.card_db import CardDB
from gwent import *


class TestUnitCard(TestCase):

    def setUp(self):
        self.unitCard = UnitCard("1", "dummy1", "Monster", 0, 8, False, False)
        self.unitHero = UnitCard("2", "dummy2", "Monster", 0, 10, True, True)
        self.horn = HornUnitCard("3", "dummy3", "Monster", 0, 2, False, False)
        self.morale = MoraleBoostCard("4", "dummy4", "Monster", 0, 1, False, False)

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

    def test_get_row(self):
        self.assertEqual(self.unitCard.get_row(self.board1), [0])
        self.assertEqual(self.unitHero.get_row(self.board1), [0, 1])

    def test_place_card(self):
        self.player1.hand.append(self.unitCard)
        self.player1.hand.append(self.unitHero)
        self.assertEqual(len(self.player1.hand), 12)

        self.unitCard.place_card(self.board1, None, 0, None)
        self.unitHero.place_card(self.board1, None, 0, None)

        for cards in self.player1.hand:
            self.assertNotEqual(cards.card_id, self.unitCard.card_id)
            self.assertNotEqual(cards.card_id, self.unitHero.card_id)

        self.assertEqual(len(self.board1.rows[0]), 2)

    def test_get_active_strength(self):
        self.morale.place_card(self.board1, None, 0, None)
        self.unitCard.place_card(self.board1, None, 0, None)
        self.horn.place_card(self.board1, None, 0, None)
        self.unitHero.place_card(self.board1, None, 0, None)
        self.assertEqual(self.unitCard.get_active_strength(self.board1), 18)
        self.assertEqual(self.unitHero.get_active_strength(self.board1), 10)
        self.assertEqual(self.morale.get_active_strength(self.board1), 2)
        self.assertEqual(self.horn.get_active_strength(self.board1), 3)

    def test_get_horn_buff(self):
        self.horn.place_card(self.board1, None, 0, None)
        self.unitCard.place_card(self.board1, None, 0, None)
        self.assertEqual(self.unitCard.get_horn_buff(self.board1), 2)

    def test_get_morale_buff(self):
        self.morale.place_card(self.board1, None, 0, None)
        self.unitCard.place_card(self.board1, None, 0, None)
        self.assertEqual(self.unitCard.get_morale_buff(self.board1), 1)
        self.assertEqual(self.morale.get_morale_buff(self.board1), 0)

    def test_get_current_status(self):
        card_dict = self.unitCard.get_data()

        self.assertEqual(card_dict.get("name"), "dummy1")
        self.assertEqual(card_dict.get("faction"), "Monster")
        self.assertEqual(card_dict.get("row"), 0)
        self.assertEqual(card_dict.get("strength"), 8)
        self.assertEqual(card_dict.get("hero"), False)
