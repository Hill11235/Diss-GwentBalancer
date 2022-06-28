import math


class MCTS:

    def __init__(self):
        
        # exploration parameter
        self.c = math.sqrt(2)
