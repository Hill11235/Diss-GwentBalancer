from gwent.cards.unit.unit_card import UnitCard


class MusterCard(UnitCard):

    def battlecry(self, board, player, opponent, opponent_board, row, target):
        explored = [self.card_id]

        for card in player.deck:
            if card.name == self.name and card.card_id not in explored:
                explored.append(card.card_id)
                card.place_card(board, player, opponent, opponent_board, card.get_row()[0], target)

        player.deck = [card for card in player.deck if not card.name == self.name]

        for card in player.hand:
            if card.name == self.name and card.card_id not in explored:
                explored.append(card.card_id)
                card.place_card(board, player, opponent, opponent_board, card.get_row()[0], target)

        player.hand = [card for card in player.hand if not card.name == self.name]
