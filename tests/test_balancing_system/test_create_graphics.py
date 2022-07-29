import os
from unittest import TestCase
from balancing_system import *


class TestGraphicCreation(TestCase):

    def setUp(self):
        self.parent_dir = os.path.dirname(__file__)
        file_name = "./../../gwent/data/card_data.csv"
        self.cycle = SimulationCycle(os.path.join(self.parent_dir, file_name), 3, 1)
        self.destination = "stats/card_data.csv"
        self.output = "stats/sim_output.json"
        self.card_data = "./../../gwent/data/card_data.csv"
        self.iteration = 0
        self.jrdr = JsonReader(os.path.join(self.parent_dir, self.output),
                               os.path.join(self.parent_dir, self.card_data),
                               os.path.join(self.parent_dir, self.destination))
        self.graphic = GraphicCreation()

    def test_create_matrix(self):
        self.graphic.create_matrix("win_rate")
        file_path = os.path.join(self.parent_dir, "../../balancing_system/visualisations/all_factions_win_rate_plot.png")
        self.assertTrue(os.path.exists(file_path))

    def test_create_line_charts(self):
        self.graphic.create_line_charts("win_rate")
        self.assertTrue(os.path.exists(
            os.path.join(self.parent_dir, "../../balancing_system/visualisations/all_factions_win_rate_plot.png")))
        self.assertTrue(os.path.exists(
            os.path.join(self.parent_dir, "../../balancing_system/visualisations/monster_win_rate_plot.png")))
        self.assertTrue(os.path.exists(
            os.path.join(self.parent_dir, "../../balancing_system/visualisations/nilfgaardian_win_rate_plot.png")))
        self.assertTrue(os.path.exists(
            os.path.join(self.parent_dir, "../../balancing_system/visualisations/northern_win_rate_plot.png")))
        self.assertTrue(os.path.exists(
            os.path.join(self.parent_dir, "../../balancing_system/visualisations/scoiatael_win_rate_plot.png")))

    def test_create_box_charts(self):
        self.graphic.create_box_charts()
        self.assertTrue(os.path.exists(
            os.path.join(self.parent_dir, "../../balancing_system/visualisations/game_duration_box_plots.png")))

        self.graphic.create_box_charts(0)
        self.assertTrue(os.path.exists(
            os.path.join(self.parent_dir,
                         "../../balancing_system/visualisations/game_duration_box_plots_iteration0.png")))

    def test_get_extreme_card_summary(self):
        self.graphic.get_extreme_card_summary("win_rate", 0)
        self.assertTrue(os.path.exists(
            os.path.join(self.parent_dir,
                         "../../balancing_system/visualisations/extreme_card_summary_iteration0_low.png")))
        self.assertTrue(os.path.exists(
            os.path.join(self.parent_dir,
                         "../../balancing_system/visualisations/extreme_card_summary_iteration0_high.png")))
