from gwent.cards.unit.unit_card import UnitCard


class MusterCard(UnitCard):

    def battlecry(self, board, player, opponent, opponent_board, row, target):

        for card in player.deck:
            if card.name == self.name:
                card.place_card(board, player, opponent, opponent_board, row, target)
        player.deck = [card for card in player.deck if not card.name == self.name]
