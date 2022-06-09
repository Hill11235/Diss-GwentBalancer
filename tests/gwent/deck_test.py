import unittest
from gwent.deck import Deck

class DeckTest(unittest.TestCase):

    def full_test(self):
       file_name = "card_data.csv"
       faction = "Monster"
       size = 22
       seed = 123

       Deck(file_name, faction, size, seed)
