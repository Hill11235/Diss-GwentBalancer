# Represents each player's board and stores cards in each row.
class Board:

    def __init__(self, player):
        self.player = player
        self.rows = [[], [], []]

    def score(self):
        # returns a list showing the total score in each row.
        total = [sum([card.get_active_strength(self) for card in row]) for row in self.rows]
        return total

    def clear_board(self):
        # loops through each row in the board and clears it of all cards.
        for row in self.rows:
            for card in row:
                self.player.graveyard.append(card)
            row.clear()

    def get_data(self):
        # returns a dictionary containing the board data.
        board = {'total_score': self.score()}
        for i in range(3):
            row = ['melee', 'distance', 'siege'][i]
            board[row] = {'cards': [card.get_data() for card in self.rows[i]],
                          'score': sum(card.get_active_strength(self) for card in self.rows[i])}

        return board
