import os
from unittest import TestCase
from balancing_system import *


class TestJsonReader(TestCase):

    def setUp(self):
        self.parent_dir = os.path.dirname(__file__)
        self.destination = "stats/card_data.csv"
        self.output = "stats/sim_output.json"
        self.card_data = "./../../gwent/data/card_data.csv"
        self.iteration = 0
        self.jrdr = JsonReader(os.path.join(self.parent_dir, self.output),
                               os.path.join(self.parent_dir, self.card_data),
                               os.path.join(self.parent_dir, self.destination))

    def test_get_faction_stats(self):
        df = self.jrdr.get_faction_overview_stats(self.iteration)
        self.assertEqual(df.shape, (4, 5))
        self.assertEqual(sum(df['games']), df.loc["monster", "games"] * 4)
        self.assertEqual(df.loc["monster", "iteration"], self.iteration)

    def test_get_card_stats(self):
        df = self.jrdr.get_card_stats(self.iteration)
        self.assertEqual(df.shape[1], 6)

    def test_run_balance(self):
        self.jrdr.run_balance(self.iteration)
        self.assertTrue(os.path.exists(os.path.join(self.parent_dir, self.destination)))

    def test_get_game_duration_stats(self):
        df = self.jrdr.get_game_duration_stats(self.iteration)
        self.assertTrue(df.shape[1], 3)

    def test_get_f_v_f_stats(self):
        df = self.jrdr.get_faction_v_faction_stats(self.iteration)
        self.assertTrue(df.shape[1], 7)
