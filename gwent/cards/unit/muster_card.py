from gwent.cards.unit.unit_card import UnitCard


class MusterCard(UnitCard):

    def battlecry(self, board, opponent_board, row, target):
        self.card_search(board, opponent_board, target, board.player.deck)
        self.card_search(board, opponent_board, target, board.player.hand)

    def card_search(self, board, opponent_board, target, container):
        index = 10000

        for i in range(len(container)):
            card = container[i]
            if card.name == self.name:
                index = i
                break

        if index < 10000:
            active_card = container.pop(index)
            active_card.place_card(board, opponent_board, active_card.get_row(board)[0], target)
