from balancing_system import *


# Class which brings all three sections together and runs balancing iterations
class Balancer:

    def __init__(self, card_file, time_limit=0.1, iters=3):
        self.card_file = card_file
        self.time_limit = time_limit
        self.iters = iters

    def run_balancing(self):
        # TODO add card_stats.csv removal from stats file
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


if __name__ == '__main__':
    Balancer("./../gwent/data/card_data.csv").run_balancing()
