from gwent.cards.special.special_card import SpecialCard
from collections import deque


# clear weather special card.
class ClearWeatherCard(SpecialCard):

    def place_card(self, board, opponent_board, row, target):
        # card is played and doesn't get added to the board.

        board.player.remove_card_from_hand(self.card_id)
        self.battlecry(board, opponent_board, row, target)

    def battlecry(self, board, opponent_board, row, target):
        # clear all weather cards from the board.

        for b in [board, opponent_board]:
            for row in b.rows:
                self.clear_row(b, row)

    def clear_row(self, board, row):
        # given a row, create a stack with all indices of clear weather cards
        stack = deque()
        index = 0

        for card in row:
            if card.weather:
                stack.append(index)
            index += 1

        # use stack to destroy all necessary cards
        while len(stack) > 0:
            index = stack.pop()
            card = row[index]
            card.destroy(board)
