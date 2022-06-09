import unittest
from gwent.deck import Deck


class DeckTest(unittest.TestCase):

    def test_faction(self):
        file_name = "data/card_data.csv"
        faction = "Nilfgaardian"
        size = 22
        seed = 123

        nilf_deck = Deck(file_name, faction, size, seed)

        for card in nilf_deck.deck:
            self.assertIn(card.faction, [faction, "neutral"])

    def test_deck_length(self):
        file_name = "data/card_data.csv"
        faction = "Monster"
        size = 22
        seed = 123

        monster_deck = Deck(file_name, faction, size, seed)
        self.assertEqual(len(monster_deck.deck), size)


if __name__ == '__main__':
    unittest.main()
