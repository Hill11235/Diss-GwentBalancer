import os
import random

from gwent import *
from agent import *
from gwent.data.card_db import CardDB


class TestAgent:

    def __init__(self, card_file):
        self.size = 22
        self.seed = 123
        self.card_db = CardDB(card_file)

        self.mcts = MCTS()
        # add to dataframe or something to preserve results

    def run_agent_comparison(self, time_limit1, time_limit2, iters=50):
        p1_win_count = 0
        p2_win_count = 0
        draws = 0

        for i in range(iters):
            nd = self.create_root_node()
            nd.state.starter = 0
            game_data = self.run_game(nd, time_limit1, time_limit2)
            winner = game_data.get('result')
            if winner is None:
                draws += 1
            elif winner == 0:
                p1_win_count += 1
            else:
                p2_win_count += 1
            self.seed += 1
            random.seed(self.seed)

        print("p1 wins with ", time_limit1, " search time: ", p1_win_count)
        print("p2 wins with ", time_limit2, " search time: ", p2_win_count)
        print("draws: ", draws)

    def run_game(self, nd, time_limit1, time_limit2):
        while not nd.is_terminal():
            if nd.state.starter == 0:
                nd_par = nd
                new_nd = self.mcts.run_search(nd, time_limit=time_limit1)
                game = new_nd.state
                nd = Node(game, nd_par)
            else:
                nd_par = nd
                new_nd = self.mcts.run_search(nd, time_limit=time_limit2)
                game = new_nd.state
                nd = Node(game, nd_par)
        return nd.state.get_game_data()

    def create_root_node(self):
        board_one, board_two = self.create_random_boards()
        game = GameState(board_one, board_two)
        nd = Node(game, None)

        return nd

    def create_random_boards(self):
        factions = ["monster", "nilfgaardian", "northern", "scoiatael"]
        f1 = random.choice(factions)
        f2 = random.choice(factions)
        deck1 = Deck(self.card_db, f1, self.size, self.seed)
        deck2 = Deck(self.card_db, f2, self.size, self.seed)

        player_one = Player("p1", f1, deck1.deck)
        player_two = Player("p2", f2, deck2.deck)

        board_one = Board(player_one)
        board_two = Board(player_two)

        return board_one, board_two


if __name__ == '__main__':
    parent_dir = os.path.dirname(__file__)
    comp = TestAgent(os.path.join(parent_dir, "./../gwent/data/card_data.csv"))
    comp.run_agent_comparison(1, 0.00001)
