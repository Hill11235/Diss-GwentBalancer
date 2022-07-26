import os
from unittest import TestCase
from balancing_system import *


class TestGraphicCreation(TestCase):

    def setUp(self):
        self.graphic = GraphicCreation(0)

    def test_create_matrix(self):
        # TODO implement on completion of faction v faction data.
        self.fail()

    def test_create_line_charts(self):
        self.graphic.create_line_charts()
        self.assertTrue(os.path.exists("visualisations/all_factions_win_rate_plot.png"))
        self.assertTrue(os.path.exists("visualisations/monster_win_rate_plot.png"))
        self.assertTrue(os.path.exists("visualisations/nilfgaardian_win_rate_plot.png"))
        self.assertTrue(os.path.exists("visualisations/northern_win_rate_plot.png"))
        self.assertTrue(os.path.exists("visualisations/scoiatael_win_rate_plot.png"))

    def test_create_box_charts(self):
        self.fail()

    def test_get_extreme_card_summary(self):
        self.fail()
