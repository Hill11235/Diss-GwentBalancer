from gwent.cards.unit.unit_card import UnitCard


class SpyCard(UnitCard):

    def battlecry(self, player, board, opponent_board):
        player.draw_card()
        player.draw_card()

    def place_card(self, board, rows, player, opponent, opponent_board):
        opponent_board.rows[self.row].append(self)
        self.battlecry(player, board, opponent_board)
