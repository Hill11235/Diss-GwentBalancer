from gwent.cards.special.special_card import SpecialCard


# horn special card.
class HornSpecialCard(SpecialCard):

    def __init__(self, card_id, name, faction, row, strength, hero, agile):
        super().__init__(card_id, name, faction, row, strength, hero, agile)
        self.horn_special = True

    def place_card(self, board, opponent_board, row, target):
        # remove from hand, if chosen row is contains no other special horn cards, add to that row.

        self.row = row
        board.player.remove_card_from_hand(self.card_id)
        possible_rows = self.get_row(board)

        if row in possible_rows:
            board.rows[self.row].append(self)

    def get_row(self, board):
        # only one special horn card allowed per row.
        # return a list of all row indices where there is no horn special card.

        targets = []

        for i in range(len(board.rows)):
            special_horn_flag = False
            for card in board.rows[i]:
                if card.horn_special:
                    special_horn_flag = True

            if not special_horn_flag:
                targets.append(i)

        return targets
