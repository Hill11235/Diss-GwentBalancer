import unittest
from gwent.deck import Deck
from gwent.cards.unit.medic_card import MedicCard


class DeckTest(unittest.TestCase):

    def test_generated_deck(self):
        file_name = "data/card_data.csv"
        faction = "Nilfgaardian"
        size = 22
        seed = 123

        nilf_deck = Deck(file_name, faction, size, seed)
        self.assertEqual(len(nilf_deck.deck), size)

        for card in nilf_deck.deck:
            self.assertIn(card.faction, [faction, "neutral"])
            self.assertNotIn(card.faction, ["northern", "scoiatael", "monster"])

    def test_all_card_size(self):
        file_name = "data/card_data.csv"
        faction = "northern"
        size = 22
        seed = 123

        northern_deck = Deck(file_name, faction, size, seed)
        self.assertEqual(len(northern_deck.all_cards), 179)

    def test_hero_card(self):
        file_name = "data/card_data.csv"
        faction = "northern"
        size = 22
        seed = 123

        northern_deck = Deck(file_name, faction, size, seed)

        for card in northern_deck.all_cards:
            if card.card_id == "yen":
                self.assertTrue(card.hero)
                self.assertTrue(isinstance(card, MedicCard))
                self.assertEqual(card.strength, 7)

    def test_all_card_faction(self):
        file_name = "data/card_data.csv"
        faction = "northern"
        size = 22
        seed = 123

        northern_deck = Deck(file_name, faction, size, seed)

        for card in northern_deck.all_cards:
            self.assertIn(card.faction, ["nilfgaardian", "neutral", "northern", "scoiatael", "monster"])

    def test_faction_count(self):
        file_name = "data/card_data.csv"
        faction = "monster"
        size = 22
        seed = 123

        deck = Deck(file_name, faction, size, seed)
        northern_cards = [card for card in deck.all_cards if card.faction == "northern"]
        nilf_cards = [card for card in deck.all_cards if card.faction == "nilfgaardian"]
        monster_cards = [card for card in deck.all_cards if card.faction == "monster"]
        neutral_cards = [card for card in deck.all_cards if card.faction == "neutral"]
        scoiatael_cards = [card for card in deck.all_cards if card.faction == "scoiatael"]

        self.assertEqual(len(northern_cards), 36)
        self.assertEqual(len(nilf_cards), 37)
        self.assertEqual(len(monster_cards), 40)
        self.assertEqual(len(neutral_cards), 29)
        self.assertEqual(len(scoiatael_cards), 37)

    def test_get_card_by_id(self):
        file_name = "data/card_data.csv"
        faction = "Nilfgaardian"
        size = 22
        seed = 123

        nilf_deck = Deck(file_name, faction, size, seed)
        card = nilf_deck.get_card_by_id("yen")

        self.assertEqual(card.card_id, "yen")
        self.assertTrue(card.hero)
        self.assertFalse(card.agile)
        self.assertEqual(card.strength, 7)

    def test_create_deck_using_list(self):
        # check that the decks created match what is expected. Particular attention to nilf spy deck.
        test_decks = "data/test_decks.csv"
        file_name = "data/card_data.csv"
        faction = "Nilfgaardian"
        size = 22
        seed = 123

        card_ids = ["arachas1", "arachas2", "arachas3",
                    "kayran", "leshen", "werewolf",
                    "frightener", "harpy", "earth_elemental", "griffin"]

        deck = Deck(file_name, faction, size, seed)
        monster_deck, nilf_deck, northern_deck, scoiatael_deck = deck.create_deck_using_list(test_decks)

        self.assertEqual(len(monster_deck), 10)
        self.assertEqual(len(nilf_deck), 16)
        self.assertEqual(len(northern_deck), 10)
        self.assertEqual(len(scoiatael_deck), 10)

        i = 0
        for ident in card_ids:
            self.assertEqual(monster_deck[i].card_id, ident)
            i += 1

        for cards in nilf_deck:
            self.assertEqual(cards.card_id, "vattier_de_rideaux")
