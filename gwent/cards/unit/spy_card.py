from gwent.cards.unit.unit_card import UnitCard


class SpyCard(UnitCard):

    def battlecry(self, board, player, opponent, opponent_board, row, target):
        draw_count = 0

        while draw_count < 2 and len(player.deck) > 0:
            player.draw_card()
            draw_count += 1

    def place_card(self, board, player, opponent, opponent_board, row, target):
        opponent_board.rows[self.row].append(self)
        player.remove_card_from_hand(self.card_id)
        self.battlecry(board, player, opponent, opponent_board, row, target)
