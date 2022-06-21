from gwent.cards.unit.unit_card import UnitCard


class SpyCard(UnitCard):

    def battlecry(self, board, player, opponent, opponent_board, row, target):
        player.draw_card()
        player.draw_card()

    def place_card(self, board, player, opponent, opponent_board, row, target):
        opponent_board.rows[self.row].append(self)
        self.battlecry(board, player, opponent, opponent_board, row, target)

    def deep_copy(self):
        copy = SpyCard(self.card_id,
                       self.name,
                       self.faction,
                       self.row,
                       self.strength,
                       self.hero,
                       self.agile)
        return copy
