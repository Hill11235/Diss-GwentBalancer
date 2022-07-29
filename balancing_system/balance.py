import glob
import os
from balancing_system import *


# Class which brings all three sections together and runs balancing iterations
class Balancer:

    def __init__(self, card_file, time_limit=0.1, iters=3):
        self.card_file = card_file
        self.time_limit = time_limit
        self.iters = iters

    def run_balancing(self):
        self.clear_stats_and_viz()
        initial_cycle = SimulationCycle(self.card_file, time_limit=self.time_limit)
        initial_cycle.simulate()
        initial_reader = JsonReader("stats/sim_output.json",
                                    "./../gwent/data/card_data.csv",
                                    "stats/card_data.csv")
        initial_reader.run_balance(0)

        graphics = GraphicCreation()
        graphics.create_matrix("win_rate", 0)
        graphics.create_box_charts(0)
        graphics.get_extreme_card_summary("win_rate", 0)

        for i in range(1, self.iters):
            cycle = SimulationCycle("stats/card_data.csv", time_limit=self.time_limit)
            cycle.simulate()
            reader = JsonReader("stats/sim_output.json",
                                "stats/card_data.csv",
                                "stats/card_data.csv")
            reader.run_balance(i)

        graphics.create_matrix("win_rate", self.iters - 1)
        graphics.create_line_charts("win_rate")
        graphics.create_box_charts(self.iters - 1)
        graphics.get_extreme_card_summary("win_rate", self.iters - 1)

    def clear_stats_and_viz(self):
        parent_dir = os.path.dirname(__file__)
        stats = "stats/*"
        viz = "visualisations/*"
        stats_path = glob.glob(os.path.join(parent_dir, stats))
        viz_path = glob.glob(os.path.join(parent_dir, viz))

        for f in stats_path:
            os.remove(f)

        for f in viz_path:
            os.remove(f)


if __name__ == '__main__':
    parent_dir = os.path.dirname(__file__)
    Balancer(os.path.join(parent_dir, "./../gwent/data/card_data.csv"), iters=10).run_balancing()
