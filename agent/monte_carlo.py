import math
import time
import copy


class MCTS:

    def __init__(self):
        # exploration parameter
        self.exp_constant = math.sqrt(2)

    def run_search(self, node, time_limit=0.1):
        start_time = time.time()
        elapsed_time = time.time() - start_time
        root = node

        if node.parent is None:
            node.get_all_children()

        while elapsed_time < time_limit:

            node = self.traverse(root)
            if not node.is_terminal():
                node.get_all_children()
            winner = self.simulate(node)
            self.backpropagate(node, winner)
            elapsed_time = time.time() - start_time

        return self.get_best_child(root)

    def traverse(self, node):
        # while node has children, repeatedly choose child with highest UCB1
        while node.children is not None and node.children != []:
            node = self.get_best_child(node)

        return node

    def get_best_child(self, node):
        children = node.children
        max_ucb = 0
        index = 0

        for i in range(len(children)):
            ucb = self.get_ucb1(children[i])
            if ucb > max_ucb:
                index = i
                max_ucb = ucb

        return children[index]

    def simulate(self, node):
        # given a node, randomly simulate until the end of the game and return the winner
        gamestate = copy.deepcopy(node.state)

        while not gamestate.check_game_complete():
            gamestate.make_random_play()

        return gamestate.get_result()

    def backpropagate(self, node, result):

        while node is not None:
            node.number_visits += 1
            if node.state.starter == result:
                node.wins += 1
            node = node.parent

    def get_ucb1(self, node):
        if node.number_visits == 0 or node.parent.number_visits == 0:
            return 100000000
        exploitation_term = (node.wins / node.number_visits)
        exploration_term = self.exp_constant * (math.sqrt(math.log(node.parent.number_visits) / node.number_visits))
        return exploitation_term + exploration_term
