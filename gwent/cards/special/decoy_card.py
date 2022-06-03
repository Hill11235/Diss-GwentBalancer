from gwent.cards.special.special_card import SpecialCard
from gwent.cards.unit.unit_card import UnitCard


class DecoyCard(SpecialCard):

    def get_targets(self, player, board):
        targets = []

        for row in board.rows:
            for card in row:
                if card.hero is False and isinstance(card, UnitCard):
                    targets.append(card)

        return targets

    def place_card(self, board, player, opponent, opponent_board, row, target):
        # need to think about how to get target card and selection to work in this case
        # once card is selected then add decoy to its row
        # add target card to player's hand
        # destroy target card with decoy setting toggled
        pass
