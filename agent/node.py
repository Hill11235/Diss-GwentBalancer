import random

# node within search tree.
class Node:

    def __init__(self, game, parent):
        self.state = game
        self.parent = parent
        self.number_visits = 0
        self.wins = 0
        self.children = []

    def is_leaf(self):
        # return boolean indicating whether this node has been expanded or not.

        return len(self.children) == 0

    def is_terminal(self):
        # check whether the underlying game state is complete or not.

        return self.state.check_game_complete()

    def get_all_children(self):
        # return a list of all possible child nodes and set children attribute.
        children = []

        child_games = self.state.get_all_children()
        for child in child_games:
            nd = Node(child, self)
            children.append(nd)

        self.children = children
        return children

    def get_random_child(self):
        if len(self.children) > 0:
            return random.choice(self.children)
