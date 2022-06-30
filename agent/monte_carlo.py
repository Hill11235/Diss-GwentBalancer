import math
import copy


class MCTS:

    def __init__(self):
        
        # exploration parameter
        self.exp_constant = math.sqrt(2)

    def run_search(self, node, time_limit=0.1):
        # run search until time limit is exceeded
        pass

    def get_best_play(self):
        # based on search statistics, make best play
        pass

    # TODO implement and test
    def selection(self, node):

        pass

    # TODO implement and test
    def expand(self, node):

        pass

    # TODO test
    def simulate(self, node):
        # given a node, randomly simulate until the end of the game and return the winner
        gamestate = copy.deepcopy(node.state)

        while not gamestate.check_game_complete():
            gamestate.make_random_play()

        return gamestate.get_final_result()

    # TODO test
    def backpropagate(self, node, result):

        while node is not None:
            node.number_visits += 1
            if node.state.starter == result:
                node.wins += 1
            node = node.parent

    # TODO test
    def get_ucb1(self, node):
        if node.number_visits == 0:
            return None
        exploitation_term = (node.wins / node.number_visits)
        exploration_term = self.exp_constant * (math.sqrt(math.log(node.parent.number_visits) / node.number_visits))
        return exploitation_term + exploration_term
