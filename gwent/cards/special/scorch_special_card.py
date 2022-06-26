from gwent.cards.special.special_card import SpecialCard
from collections import deque


class ScorchSpecialCard(SpecialCard):

    def place_card(self, board, player, opponent, opponent_board, row, target):
        self.battlecry(board, player, opponent, opponent_board, row, target)
        player.remove_card_from_hand(self.card_id)

    def battlecry(self, board, player, opponent, opponent_board, row, target):
        max_strength = 0

        for b in [board, opponent_board]:
            for row in b.rows:
                for card in row:
                    card_strength = card.get_active_strength(b)
                    if not card.hero and card_strength > max_strength and card.unit:
                        max_strength = card_strength

        for b in [board, opponent_board]:
            for row in b.rows:
                self.scorch_row(b, row, max_strength)

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
