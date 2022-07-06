import random
from gwent.cards.unit.unit_card import UnitCard


class MedicCard(UnitCard):

    def get_targets(self, board):
        revivable_units = [card for card in board.player.graveyard if card.unit and card.hero is False]

        if len(revivable_units) > 0:
            return revivable_units
        else:
            return None

    def battlecry(self, board, opponent_board, row, target):
        if target is not None and target.hero is False and target.unit:
            chosen_card = target
            board.player.graveyard.remove(chosen_card)

            chosen_row = random.choice(chosen_card.get_row(board))
            chosen_targets = chosen_card.get_targets(board)

            if chosen_targets is not None:
                chosen_target = random.choice(chosen_targets)
            else:
                chosen_target = None

            chosen_card.place_card(board, opponent_board, chosen_row, chosen_target)
