from gwent.cards.unit.unit_card import UnitCard


class MedicCard(UnitCard):

    def get_targets(self, player, board):
        revivable_units = [card for card in player.graveyard if card.unit and card.hero is False]

        if len(revivable_units) > 0:
            return revivable_units
        else:
            return None

    def battlecry(self, board, player, opponent, opponent_board, row, target):
        targets = self.get_targets(player, board)

        if target in targets and target.hero is False and target.unit:
            chosen_card = target
            chosen_card.place_card(board, player, opponent, opponent_board, row, target)
            player.graveyard.remove(chosen_card)
