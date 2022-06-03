from gwent.cards.unit.unit_card import UnitCard


class MedicCard(UnitCard):

    def get_targets(self, player):
        revivable_units = [card for card in player.graveyard if isinstance(card, UnitCard) and card.hero is False]

        if len(revivable_units) > 0:
            return revivable_units
        else:
            return None

    def battlecry(self, board, player, opponent, opponent_board, target):
        targets = self.get_targets(player)
        chosen_card = None

        # TODO think about if args need to be refactored so that target is not an int?
        if targets is not None and targets[target].hero is False and isinstance(targets[target], UnitCard):
            chosen_card = targets[target]
            chosen_card.place_card(board, player, opponent, opponent_board, target)
            player.graveyard.remove(chosen_card)
