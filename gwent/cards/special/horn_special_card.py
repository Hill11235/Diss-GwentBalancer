from gwent.cards.special.special_card import SpecialCard


class HornSpecialCard(SpecialCard):

    def __init__(self, card_id, name, faction, row, strength):
        super().__init__(card_id, name, faction, row, strength)
        self.horn_special = True

    def place_card(self, board, player, opponent, opponent_board, row, target):
        self.row = target
        board.rows[self.row].append(self)
