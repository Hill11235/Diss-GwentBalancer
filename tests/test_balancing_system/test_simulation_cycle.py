from unittest import TestCase
from balancing_system import *


class TestSimulationCycle(TestCase):

    def setUp(self):
        file_name = "card_data.csv"
        self.cycle = SimulationCycle(file_name, 2)

    def test_simulate(self):
        self.cycle.simulate()

    def test_run_game(self):

        pass

    def test_write_to_json(self):

        pass

    def test_run_cycle(self):

        pass

    def test_create_root_nodes(self):

        pass

    def test_create_boards(self):

        pass
