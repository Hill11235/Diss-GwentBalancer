from gwent.cards.special.special_card import SpecialCard


class DecoyCard(SpecialCard):

    def get_targets(self, player, board):
        targets = []

        for row in board.rows:
            for card in row:
                if card.hero is False and card.unit:
                    targets.append(card)

        return targets

    def place_card(self, board, player, opponent, opponent_board, row, target):
        targets = self.get_targets(player, board)

        if target in targets and target.hero is False and target.unit:
            self.row = target.row
            player.hand.append(target)
            target.destroy(board, player, decoy=True)
            board.rows[self.row].append(self)
