from gwent.cards.special.special_card import SpecialCard


class ClearWeatherCard(SpecialCard):

    def place_card(self, board, opponent_board, row, target):
        board.player.remove_card_from_hand(self.card_id)
        self.battlecry(board, opponent_board, row, target)

    def battlecry(self, board, opponent_board, row, target):
        for b in [board, opponent_board]:
            for row in b.rows:
                for card in row:
                    if card.weather:
                        card.destroy(b, b.player)
