from gwent.cards.special.special_card import SpecialCard
from gwent.cards.unit.unit_card import UnitCard


class ScorchSpecialCard(SpecialCard):

    def place_card(self, board, player, opponent, opponent_board, row, target):
        self.battlecry(board, player, opponent, opponent_board, row, target)

    def battlecry(self, board, player, opponent, opponent_board, row, target):
        max_strength = 0

        for b in [board, opponent_board]:
            for row in b.rows:
                for card in row:
                    card_strength = card.get_active_strength(b)
                    if not card.hero and card_strength > max_strength and isinstance(card, UnitCard):
                        max_strength = card_strength

        for b in [board, opponent_board]:
            for row in b.rows:
                for card in row:
                    card_strength = card.get_active_strength(b)
                    if not card.hero and card_strength == max_strength and isinstance(card, UnitCard):
                        card.destroy(b, b.player)
