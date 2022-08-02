from gwent.cards.special.special_card import SpecialCard


# decoy special card.
class DecoyCard(SpecialCard):

    def get_targets(self, board):
        # return a list of all non-hero unit cards on the player's board.

        targets = []

        for row in board.rows:
            for card in row:
                if card.hero is False and card.unit:
                    targets.append(card)

        return targets

    def place_card(self, board, opponent_board, row, target):
        # place card and if a valid target is specified, return it to the player's hand.

        targets = self.get_targets(board)
        board.player.remove_card_from_hand(self.card_id)

        if target in targets and target.hero is False and target.unit:
            self.row = target.row
            board.player.hand.append(target)
            target.destroy(board, decoy=True)
        else:
            self.row = 0

        board.rows[self.row].append(self)
