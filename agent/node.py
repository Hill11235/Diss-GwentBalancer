class Node:

    def __init__(self, game, parent):
        self.state = game
        self.parent = parent
        self.number_visits = 0
        self.linked_wins = 0
        self.previous_action = 0
        # upper confidence bound 1 of node
        pass

    def is_terminal(self):
        return len(self.get_all_children()) == 0

    def get_all_children(self):
        children = []
        # get list of all children
        return children

    def get_random_child(self):
        # return a random child node
        pass

