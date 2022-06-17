class Node:

    def __init__(self):
        # holds a game state
        # number of visits to this node
        # number of wins this node has
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

