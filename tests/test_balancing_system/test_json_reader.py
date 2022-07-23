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
        self.fail()

    def test_get_card_stats(self):
        self.fail()

    def test_create_new_card_data_file(self):
        self.fail()

    def test_create_iter_visualisations(self):
        self.fail()
