import os
from unittest import TestCase
from balancing_system import *


class TestGraphicCreation(TestCase):

    def setUp(self):
        self.graphic = GraphicCreation()
        self.parent_dir = os.path.dirname(__file__)

    def test_create_matrix(self):
        self.graphic.create_matrix("win_rate")
        file_path = os.path.join(self.parent_dir, "visualisations/all_factions_win_rate_plot.png")
        self.assertTrue(os.path.exists(file_path))

    def test_create_line_charts(self):
        self.graphic.create_line_charts("win_rate")
        self.assertTrue(os.path.exists(os.path.join(self.parent_dir, "visualisations/all_factions_win_rate_plot.png")))
        self.assertTrue(os.path.exists(os.path.join(self.parent_dir, "visualisations/monster_win_rate_plot.png")))
        self.assertTrue(os.path.exists(os.path.join(self.parent_dir, "visualisations/nilfgaardian_win_rate_plot.png")))
        self.assertTrue(os.path.exists(os.path.join(self.parent_dir, "visualisations/northern_win_rate_plot.png")))
        self.assertTrue(os.path.exists(os.path.join(self.parent_dir, "visualisations/scoiatael_win_rate_plot.png")))

    def test_create_box_charts(self):
        self.graphic.create_box_charts()
        self.assertTrue(os.path.exists(os.path.join(self.parent_dir, "visualisations/game_duration_box_plots.png")))

        self.graphic.create_box_charts(4)
        self.assertTrue(os.path.exists(os.path.join(self.parent_dir,
                                                    "visualisations/game_duration_box_plots_iteration4.png")))

    def test_get_extreme_card_summary(self):
        self.graphic.get_extreme_card_summary("win_rate", 1)
        self.assertTrue(os.path.exists(os.path.join(self.parent_dir,
                                                    "visualisations/extreme_card_summary_iteration1_low.png")))
        self.assertTrue(os.path.exists(os.path.join(self.parent_dir,
                                                    "visualisations/extreme_card_summary_iteration1_high.png")))
