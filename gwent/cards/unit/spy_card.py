from gwent.cards.unit.unit_card import UnitCard


# spy unit card.
class SpyCard(UnitCard):

    def battlecry(self, board, opponent_board, row, target):
        # draw two cards for the player of this card.
        draw_count = 0

        while draw_count < 2 and len(board.player.deck) > 0:
            board.player.draw_card()
            draw_count += 1

    def place_card(self, board, opponent_board, row, target):
        # place card on opponent's board.

        opponent_board.rows[self.row].append(self)
        board.player.remove_card_from_hand(self.card_id)
        self.battlecry(board, opponent_board, row, target)
