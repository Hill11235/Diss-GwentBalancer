import os
from unittest import TestCase
from balancing_system import *


class TestSimulationCycle(TestCase):

    def setUp(self):
        parent_dir = os.path.dirname(__file__)
        file_name = "./../../gwent/data/card_data.csv"
        self.cycle = SimulationCycle(os.path.join(parent_dir, file_name), 3, 1)

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
