from unittest import TestCase
from balancing_system import *


class TestJsonReader(TestCase):

    def setUp(self):
        self.jrdr = JsonReader("output.json")

    def test_read(self):
        print(self.jrdr.data_list)
        print()
        print(self.jrdr.data_list[0])
        print()
        print(self.jrdr.data_list[0].get("winning_faction"))
        print(self.jrdr.data_list[0].get("player2"))
        print(len(self.jrdr.data_list))

    def test_get_faction_stats(self):
        df = self.jrdr.get_faction_stats(1)
        self.assertEqual(df.shape, (4, 4))
        self.assertEqual(sum(df['games']), df.loc["monster", "games"] * 4)
        self.assertEqual(df.loc["monster", "iteration"], 1)

    def test_get_card_stats(self):
        self.fail()

    def test_create_new_card_data_file(self):
        self.fail()

    def test_create_iter_visualisations(self):
        self.fail()
