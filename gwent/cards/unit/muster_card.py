from gwent.cards.unit.unit_card import UnitCard


class MusterCard(UnitCard):

    def battlecry(self, board, opponent_board, row, target):
        explored = [self.card_id]

        for card in board.player.deck:
            if card.name == self.name and card.card_id not in explored:
                explored.append(card.card_id)
                card.place_card(board, opponent_board, card.get_row(board)[0], target)

        board.player.deck = [card for card in board.player.deck if not card.name == self.name]

        for card in board.player.hand:
            if card.name == self.name and card.card_id not in explored:
                explored.append(card.card_id)
                card.place_card(board, opponent_board, card.get_row(board)[0], target)

        board.player.hand = [card for card in board.player.hand if not card.name == self.name]
