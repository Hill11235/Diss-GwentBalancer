import json
import copy
from gwent import *
from agent import *
from gwent.data.card_db import CardDB


class SimulationCycle:

    def __init__(self, card_file, iters=100, time_limit=0.1):
        self.size = 22
        self.seed = 123
        self.iters = iters
        self.time_limit = time_limit
        self.card_db = CardDB(card_file)

        self.deck = Deck(self.card_db, "Monster", self.size, self.seed)
        self.mcts = MCTS()
        # set up rotating seed? ASK CHRIS

    def simulate(self):
        output = []

        for i in range(self.iters):

            nd_m_v_ni, nd_m_v_no, nd_m_v_s, nd_ni_v_no, nd_ni_v_s, nd_no_v_s = self.create_root_nodes()
            node_list = [nd_m_v_ni, nd_m_v_no, nd_m_v_s, nd_ni_v_no, nd_ni_v_s, nd_no_v_s]

            for nd in node_list:
                game_data = self.run_game(nd)
                output.append(game_data)

        self.write_to_json("stats/output.json", output)

    def run_game(self, nd):
        while not nd.is_terminal():
            nd = self.mcts.run_search(nd, self.time_limit)
        return nd.state.get_game_data()

    def write_to_json(self, file, game_list):
        with open(file, 'w') as res:
            json.dump(game_list, res)

    def create_root_nodes(self):
        board_monster, board_nilf, board_northern, board_scoiatael = self.create_boards()

        # consider whether deep copies needed
        monster_vs_nilf = GameState(copy.deepcopy(board_monster), copy.deepcopy(board_nilf))
        monster_vs_northern = GameState(copy.deepcopy(board_monster), copy.deepcopy(board_northern))
        monster_vs_scoiatael = GameState(copy.deepcopy(board_monster), copy.deepcopy(board_scoiatael))
        nilf_vs_northern = GameState(copy.deepcopy(board_nilf), copy.deepcopy(board_northern))
        nilf_vs_scoiatael = GameState(copy.deepcopy(board_nilf), copy.deepcopy(board_scoiatael))
        northern_vs_scoiatael = GameState(copy.deepcopy(board_northern), copy.deepcopy(board_scoiatael))

        node_mon_v_nilf = Node(monster_vs_nilf, None)
        node_mon_v_nort = Node(monster_vs_northern, None)
        node_mon_v_scoi = Node(monster_vs_scoiatael, None)
        node_nilf_v_nort = Node(nilf_vs_northern, None)
        node_nilf_v_scoi = Node(nilf_vs_scoiatael, None)
        node_nort_v_scoi = Node(northern_vs_scoiatael, None)

        return node_mon_v_nilf, node_mon_v_nort, node_mon_v_scoi, node_nilf_v_nort, node_nilf_v_scoi, node_nort_v_scoi

    def create_boards(self):
        monster_deck, nilf_deck, northern_deck, scoiatael_deck = self.deck.create_four_random_decks()
        player_monster = Player("p1", "monster", monster_deck)
        player_nilf = Player("p2", "nilfgaardian", nilf_deck)
        player_northern = Player("p3", "northern", northern_deck)
        player_scoiatael = Player("p4", "scoiatael", scoiatael_deck)

        board_monster = Board(player_monster)
        board_nilf = Board(player_nilf)
        board_northern = Board(player_northern)
        board_scoiatael = Board(player_scoiatael)

        return board_monster, board_nilf, board_northern, board_scoiatael
