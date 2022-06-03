from gwent.cards.unit.unit_card import UnitCard


class MedicCard(UnitCard):

    def get_targets(self, player):
        revivable_units = [card for card in player.graveyard if isinstance(card, UnitCard) and card.hero is False]

        if len(revivable_units) > 0:
            return revivable_units
        else:
            return None

    def battlecry(self, board, player, opponent, opponent_board):
        pass
