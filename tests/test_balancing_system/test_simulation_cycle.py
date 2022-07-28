from unittest import TestCase
from balancing_system import *


class TestSimulationCycle(TestCase):

    def setUp(self):
        file_name = "card_data.csv"
        self.cycle = SimulationCycle(file_name, 10, 1)

    def test_simulate(self):
        self.cycle.simulate()

    def test_run_cycle(self):
        # TODO complete test or delete
        pass

    def test_create_root_nodes(self):
        # TODO complete test or delete
        pass

    def test_create_boards(self):
        # TODO complete test or delete
        pass
