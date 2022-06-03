from gwent.cards.unit.unit_card import UnitCard

SCORCH_LIMIT = 10


class ScorchUnitCard(UnitCard):

    def battlecry(self, board, player, opponent, opponent_board):
        max_strength = 0
        total_strength = 0

        for card in opponent_board.rows[self.row]:
            card_strength = card.get_active_strength(board)
            total_strength += card_strength

            if not card.hero and card_strength > max_strength:
                max_strength = card_strength

        if total_strength >= SCORCH_LIMIT:
            for card in opponent_board.rows[self.row]:
                if card.get_active_strength(board) == max_strength:
                    card.destroy(board, player)
