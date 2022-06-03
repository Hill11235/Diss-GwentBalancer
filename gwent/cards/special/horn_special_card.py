from gwent.cards.special.special_card import SpecialCard


class HornSpecialCard(SpecialCard):

    def place_card(self, board, player, opponent, opponent_board, target):
        self.row = target
        board.rows[self.row].append(self)
