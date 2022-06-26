from gwent.cards.special.special_card import SpecialCard


class HornSpecialCard(SpecialCard):

    def __init__(self, card_id, name, faction, row, strength, hero, agile):
        super().__init__(card_id, name, faction, row, strength, hero, agile)
        self.horn_special = True

    def place_card(self, board, player, opponent, opponent_board, row, target):
        self.row = target
        player.remove_card_from_hand(self.card_id)
        targets = self.get_targets(player, board)

        if target in targets:
            board.rows[self.row].append(self)

    def get_targets(self, player, board):
        # return all rows in board where there isn't already a special horn card present
        targets = []

        for i in range(len(board.rows)):
            special_horn_flag = False
            for card in board.rows[i]:
                if card.horn_special:
                    special_horn_flag = True

            if not special_horn_flag:
                targets.append(i)

        return targets
