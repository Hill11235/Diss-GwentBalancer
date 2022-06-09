from gwent.cards.card import Card


class SpecialCard(Card):

    def __init__(self, card_id, name, faction, row, strength):
        super().__init__(card_id, name, faction, row, strength)
        self.unit = False

    def place_card(self, board, player, opponent, opponent_board, row, target):
        board.rows[self.row].append(self)
        self.battlecry(board, player, opponent, opponent_board, row, target)

    def battlecry(self, board, player, opponent, opponent_board, row, target):
        pass

    def get_active_strength(self, board):
        return 0
