from gwent.cards.special.special_card import SpecialCard


class WeatherCard(SpecialCard):

    def place_card(self, board, player, opponent, opponent_board, target):
        for b in [board, opponent_board]:
            b.rows[self.row].append(self)
