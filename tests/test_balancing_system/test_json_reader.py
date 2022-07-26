import os
from unittest import TestCase
from balancing_system import *


class TestJsonReader(TestCase):

    def setUp(self):
        self.destination = "stats/card_data.csv"
        self.jrdr = JsonReader("stats/sim_output.json",
                               "./../../gwent/data/card_data.csv",
                               self.destination)

    def test_get_faction_stats(self):
        df = self.jrdr.get_faction_overview_stats(2)
        self.assertEqual(df.shape, (4, 5))
        self.assertEqual(sum(df['games']), df.loc["monster", "games"] * 4)
        self.assertEqual(df.loc["monster", "iteration"], 1)

    def test_get_card_stats(self):
        df = self.jrdr.get_card_stats(2)
        self.assertEqual(df.shape[1], 6)

    def test_run_balance(self):
        self.jrdr.run_balance(2, "stats/faction_stats.csv", "stats/card_stats.csv")
        self.assertTrue(os.path.exists(self.destination))
