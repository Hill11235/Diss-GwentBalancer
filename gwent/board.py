class Board:

    def __init__(self, game, player):
        self.game = game
        self.player = player
        self.rows = [[], [], []]

    def score(self):
        total = [sum([card.get_strength() for card in row]) for row in self.rows]
        return total

    # string representation method

    # JSON method?
