from gwent.cards.card import Card


# special card class, superclass for all other special cards.
class SpecialCard(Card):

    def __init__(self, card_id, name, faction, row, strength, hero, agile):
        super().__init__(card_id, name, faction, row, strength, hero, agile)
        self.unit = False

    def place_card(self, board, opponent_board, row, target):
        # set row, remove from the player's hand, add to the specified row, and call battlecry.

        self.row = row
        board.player.remove_card_from_hand(self.card_id)
        board.rows[self.row].append(self)
        self.battlecry(board, opponent_board, row, target)

    def battlecry(self, board, opponent_board, row, target):
        # default battlecry to be overridden.
        pass

    def get_active_strength(self, board):
        # all special cards contribute zero score.

        return 0
