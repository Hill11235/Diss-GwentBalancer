class Board:

    def __init__(self, player):
        self.player = player
        self.rows = [[], [], []]

    def score(self):
        total = [sum([card.get_active_strength(self) for card in row]) for row in self.rows]
        return total

    def clear_board(self):
        for row in self.rows:
            for card in row:
                self.player.graveyard.append(card)
            row.clear()

    def get_data(self):
        board = {'total_score': self.score()}
        for i in range(3):
            row = ['melee', 'distance', 'siege'][i]
            board[row] = {'cards': [card.get_data() for card in self.rows[i]],
                          'score': sum(card.get_active_strength(self) for card in self.rows[i])}

        return board
