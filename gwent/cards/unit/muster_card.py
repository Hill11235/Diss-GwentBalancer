from gwent.cards.unit.unit_card import UnitCard


class MusterCard(UnitCard):

    def battlecry(self, board, player, opponent, opponent_board, row, target):
        # TODO check that modifying a list while iterating through it will not cause problems
        for card in player.deck:
            if card.name == self.name:
                player.deck.remove(card)
                card.place_card(board, player, opponent, opponent_board, row, target)
