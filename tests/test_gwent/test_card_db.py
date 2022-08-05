import unittest
import os
from gwent.data.card_db import CardDB
from gwent.cards.unit.medic_card import MedicCard


class DeckTest(unittest.TestCase):

    def setUp(self):
        parent_dir = os.path.dirname(__file__)
        file_name = "./../../gwent/data/card_data.csv"
        self.card_db = CardDB(os.path.join(parent_dir, file_name))

    def test_all_card_size(self):
        self.assertEqual(len(self.card_db.all_cards), 185)

    def test_hero_card(self):
        for card in self.card_db.all_cards:
            if card.card_id == "yen":
                self.assertTrue(card.hero)
                self.assertTrue(isinstance(card, MedicCard))
                self.assertEqual(card.strength, 7)

    def test_all_card_faction(self):
        for card in self.card_db.all_cards:
            self.assertIn(card.faction, ["nilfgaardian", "neutral", "northern", "scoiatael", "monster"])

    def test_faction_count(self):
        northern_cards = [card for card in self.card_db.all_cards if card.faction == "northern"]
        nilf_cards = [card for card in self.card_db.all_cards if card.faction == "nilfgaardian"]
        monster_cards = [card for card in self.card_db.all_cards if card.faction == "monster"]
        neutral_cards = [card for card in self.card_db.all_cards if card.faction == "neutral"]
        scoiatael_cards = [card for card in self.card_db.all_cards if card.faction == "scoiatael"]

        self.assertEqual(len(northern_cards), 36)
        self.assertEqual(len(nilf_cards), 37)
        self.assertEqual(len(monster_cards), 40)
        self.assertEqual(len(neutral_cards), 35)
        self.assertEqual(len(scoiatael_cards), 37)

    def test_get_all_cards(self):
        copy = self.card_db.get_all_cards()
        for i in range(len(self.card_db.all_cards)):
            self.assertEqual(self.card_db.all_cards[i].card_id, copy[i].card_id)
