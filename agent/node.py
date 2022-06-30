class Node:

    def __init__(self, game, parent):
        self.state = game
        self.parent = parent
        self.number_visits = 0
        self.wins = 0
        self.children = []

    def is_terminal(self):
        return len(self.get_all_children()) == 0

    def get_all_children(self):
        children = []
        # get list of all children
        return children

    def get_random_child(self):
        # return a random child node
        pass

