import os
from unittest import TestCase
from balancing_system import *


class TestSimulationCycle(TestCase):

    def setUp(self):
        self.parent_dir = os.path.dirname(__file__)
        file_name = "./../../gwent/data/card_data.csv"
        self.cycle = SimulationCycle(os.path.join(self.parent_dir, file_name), 3, 0.1)

    def test_simulate(self):
        self.cycle.simulate()
        self.assertTrue(os.path.exists(os.path.join(self.parent_dir, "../../balancing_system/stats/sim_output.json")))

    def test_run_game(self):
        nd_m_v_ni, _, _, _, _, _ = self.cycle.create_root_nodes()
        data = self.cycle.run_game(nd_m_v_ni)
        self.assertTrue(len(data.get('score')) >= 4)

    def test_create_root_nodes(self):
        nd_m_v_ni, nd_m_v_no, nd_m_v_s, nd_ni_v_no, nd_ni_v_s, nd_no_v_s = self.cycle.create_root_nodes()
        node_list = [nd_m_v_ni, nd_m_v_no, nd_m_v_s, nd_ni_v_no, nd_ni_v_s, nd_no_v_s]

        for nd in node_list:
            self.assertEqual(nd.wins, 0)
            self.assertEqual(nd.number_visits, 0)
            self.assertIsNone(nd.parent)

    def test_create_boards(self):
        b_m, b_ni, b_no, b_s = self.cycle.create_boards()

        self.assertEqual(b_m.player.faction, "monster")
        self.assertEqual(b_ni.player.faction, "nilfgaardian")
        self.assertEqual(b_no.player.faction, "northern")
        self.assertEqual(b_s.player.faction, "scoiatael")
