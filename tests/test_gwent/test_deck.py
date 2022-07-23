import unittest
from gwent.deck import Deck
from gwent.data.card_db import CardDB


class DeckTest(unittest.TestCase):

    def setUp(self):
        file_name = "card_data.csv"
        self.faction = "Nilfgaardian"
        self.size = 22
        self.seed = 123

        self.card_db = CardDB(file_name)
        self.nilf_deck = Deck(self.card_db, self.faction, self.size, self.seed)

    def test_generated_deck(self):
        self.assertEqual(len(self.nilf_deck.deck), self.size)

        for card in self.nilf_deck.deck:
            self.assertIn(card.faction, [self.faction, "neutral"])
            self.assertNotIn(card.faction, ["northern", "scoiatael", "monster"])

    def test_get_card_by_id(self):
        card = self.nilf_deck.get_card_by_id("yen")

        self.assertEqual(card.card_id, "yen")
        self.assertTrue(card.hero)
        self.assertFalse(card.agile)
        self.assertEqual(card.strength, 7)

    def test_create_deck_using_list(self):
        # check that the decks created match what is expected. Particular attention to nilf spy deck.
        test_decks = "data/test_decks.csv"

        card_ids = ["arachas1", "arachas2", "arachas3",
                    "kayran", "leshen", "werewolf",
                    "frightener", "harpy", "earth_elemental", "griffin"]

        monster_deck, nilf_deck, northern_deck, scoiatael_deck = self.nilf_deck.create_deck_using_list(test_decks)

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

    def test_create_four_random_decks(self):

        monster_deck, nilf_deck, northern_deck, scoiatael_deck = self.nilf_deck.create_four_random_decks()

        self.assertEqual(len(monster_deck), 22)
        self.assertEqual(len(nilf_deck), 22)
        self.assertEqual(len(northern_deck), 22)
        self.assertEqual(len(scoiatael_deck), 22)

        for i in range(22):
            self.assertTrue(scoiatael_deck[i].faction == "scoiatael" or scoiatael_deck[i].faction == "neutral")
            self.assertTrue(monster_deck[i].faction == "monster" or monster_deck[i].faction == "neutral")
            self.assertTrue(nilf_deck[i].faction == "nilfgaardian" or nilf_deck[i].faction == "neutral")
            self.assertTrue(northern_deck[i].faction == "northern" or northern_deck[i].faction == "neutral")

    def test_random_deck_similarity(self):
        monster_deck, nilf_deck, northern_deck, scoiatael_deck = self.nilf_deck.create_four_random_decks()
        monster_deck1, nilf_deck1, northern_deck1, scoiatael_deck1 = self.nilf_deck.create_four_random_decks()

        sim_check = True

        for i in range(len(monster_deck)):
            if monster_deck[i].card_id != monster_deck1[i].card_id:
                sim_check = False

        self.assertFalse(sim_check)
