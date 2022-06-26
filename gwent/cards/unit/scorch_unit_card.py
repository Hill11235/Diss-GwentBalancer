from gwent.cards.unit.unit_card import UnitCard
from collections import deque

SCORCH_LIMIT = 10


class ScorchUnitCard(UnitCard):

    def battlecry(self, board, player, opponent, opponent_board, row, target):
        max_strength = 0
        total_strength = 0

        for card in opponent_board.rows[self.row]:
            card_strength = card.get_active_strength(opponent_board)
            total_strength += card_strength

            if not card.hero and card.unit and card_strength > max_strength:
                max_strength = card_strength

        if total_strength >= SCORCH_LIMIT:
            self.scorch_row(opponent_board, opponent_board.rows[self.row], max_strength)

    def scorch_row(self, board, row, max_strength):
        # given a row, create a stack with all indices of max strength cards (non-hero, unit)
        stack = deque()
        index = 0

        for card in row:
            card_strength = card.get_active_strength(board)
            if not card.hero and card_strength == max_strength and card.unit:
                stack.append(index)
            index += 1

        # use stack to destroy all necessary cards
        while len(stack) > 0:
            index = stack.pop()
            card = row[index]
            card.destroy(board, board.player)