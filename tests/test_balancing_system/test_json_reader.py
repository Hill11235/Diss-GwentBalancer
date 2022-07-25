from unittest import TestCase
from balancing_system import *


class TestJsonReader(TestCase):

    def setUp(self):
        self.jrdr = JsonReader("stats/output.json", "./../../gwent/data/card_data.csv", "stats/card_data.csv")

    def test_get_faction_stats(self):
        df = self.jrdr.get_faction_stats(1)
        self.assertEqual(df.shape, (4, 5))
        self.assertEqual(sum(df['games']), df.loc["monster", "games"] * 4)
        self.assertEqual(df.loc["monster", "iteration"], 1)

    def test_get_card_stats(self):
        df = self.jrdr.get_card_stats(1)
        self.assertEqual(df.shape[1], 6)
        print(df.nlargest(10, 'adjustment'))
        self.jrdr.create_new_card_data_file(df)

    def test_create_new_card_data_file(self):
        self.fail()
