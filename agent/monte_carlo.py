import math
import time
import copy
import random


# search class.
class MCTS:

    def run_search(self, node, time_limit=0.1):
        # run MCTS search for provided time limit, then return child node with the best UCB1 score.
        start_time = time.time()
        elapsed_time = time.time() - start_time
        root = node

        if node.parent is None:
            node.get_all_children()

        while elapsed_time < time_limit:

            node = self.traverse(root)
            if not node.is_terminal():
                node.get_all_children()
                node = node.get_random_child()
            winner = self.simulate(node)
            self.backpropagate(node, winner)
            elapsed_time = time.time() - start_time

        return self.get_best_child(root, 0)

    def traverse(self, node):
        # while node has children, repeatedly choose child with highest UCB1.
        while node.children is not None and node.children != []:
            node = self.get_best_child(node)

        return node

    def get_best_child(self, node, exp_const=math.sqrt(2)):
        # return the child node with the highest UCB1 score.
        children = node.children
        max_ucb = 0
        indices = []

        for i in range(len(children)):
            ucb = self.get_ucb1(children[i], exp_const)
            if ucb > max_ucb:
                indices = []
                indices.append(i)
                max_ucb = ucb
            elif ucb == max_ucb:
                indices.append(i)

        return children[random.choice(indices)]

    def simulate(self, node):
        # given a node, randomly simulate until the end of the game and return the winner.
        gamestate = copy.deepcopy(node.state)

        while not gamestate.check_game_complete():
            gamestate.make_random_play()

        return gamestate.get_result()

    def backpropagate(self, node, result):
        # repeatedly run through parent nodes, update visited attribute and winner attribute based on active player.

        while node is not None:
            node.number_visits += 1
            if node.parent is not None:
                if node.state.starter != result and node.parent.state.starter == result:
                    node.wins += 1
                elif node.state.starter == result and node.parent.state.starter == result:
                    node.wins += 1
            node = node.parent

    def get_ucb1(self, node, exp_const=math.sqrt(2)):
        # return the UCB1 score for a given node.

        if node.number_visits == 0 or node.parent.number_visits == 0:
            return 100000000
        exploitation_term = (node.wins / node.number_visits)
        exploration_term = exp_const * (math.sqrt(math.log(node.parent.number_visits) / node.number_visits))
        return exploitation_term + exploration_term
