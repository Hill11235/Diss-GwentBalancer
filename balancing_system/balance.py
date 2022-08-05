import glob
import os
from balancing_system import *


# class which brings all three subsystems together and runs balancing iterations.
class Balancer:

    def __init__(self, card_file, time_limit=0.1, iters=3):
        self.card_file = card_file
        self.time_limit = time_limit
        self.iters = iters
        self.parent_dir = os.path.dirname(__file__)

    def run_balancing(self):
        # run the specified iterations of simulations and reading JSON files.

        self.clear_stats_and_viz()
        initial_cycle = SimulationCycle(self.card_file, time_limit=self.time_limit)
        initial_cycle.simulate()
        initial_reader = JsonReader(os.path.join(self.parent_dir, "stats/sim_output.json"),
                                    os.path.join(self.parent_dir, "./../gwent/data/card_data.csv"),
                                    os.path.join(self.parent_dir, "stats/card_data.csv"))
        initial_reader.run_balance(0)

        graphics = GraphicCreation()
        graphics.create_matrix("win_rate", 0)
        graphics.create_box_charts(0)
        graphics.get_extreme_card_summary("win_rate", 0)

        for i in range(1, self.iters):
            cycle = SimulationCycle(os.path.join(self.parent_dir, "stats/card_data.csv"), time_limit=self.time_limit)
            cycle.simulate()
            reader = JsonReader(os.path.join(self.parent_dir, "stats/sim_output.json"),
                                os.path.join(self.parent_dir, "stats/card_data.csv"),
                                os.path.join(self.parent_dir, "stats/card_data.csv"))
            reader.run_balance(i)

        graphics.create_matrix("win_rate", self.iters - 1)
        graphics.create_line_charts("win_rate")
        graphics.create_box_charts(self.iters - 1)
        graphics.get_extreme_card_summary("win_rate", self.iters - 1)

    def clear_stats_and_viz(self):
        # clears viz and stats directories.

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
    Balancer(os.path.join(parent_dir, "./../gwent/data/card_data.csv"), time_limit=0.2, iters=5).run_balancing()
