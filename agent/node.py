import random


class Node:

    def __init__(self, game, parent):
        self.state = game
        self.parent = parent
        self.number_visits = 0
        self.wins = 0
        self.children = []

    def is_leaf(self):
        return len(self.children) == 0

    def is_terminal(self):
        return self.state.check_game_complete()

    # TODO test
    def get_all_children(self):
        children = []

        child_games = self.state.get_all_children()
        for child in child_games:
            nd = Node(child, self)
            children.append(nd)

        self.children = children
        return children

    # TODO test (consider when this will be called and see if it needs to be changed)
    def get_random_child(self):
        return random.choice(self.children)

