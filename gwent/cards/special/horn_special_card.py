from gwent.cards.special.special_card import SpecialCard


class HornSpecialCard(SpecialCard):

    # TODO add check to ensure that a horn special card isn't already present on a row

    def __init__(self, card_id, name, faction, row, strength, hero, agile):
        super().__init__(card_id, name, faction, row, strength, hero, agile)
        self.horn_special = True

    def place_card(self, board, player, opponent, opponent_board, row, target):
        self.row = target
        board.rows[self.row].append(self)
