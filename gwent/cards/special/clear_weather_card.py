from gwent.cards.special.special_card import SpecialCard
from gwent.cards.special.weather_card import WeatherCard


class ClearWeatherCard(SpecialCard):

    def place_card(self, board, player, opponent, opponent_board, row, target):
        self.battlecry(board, player, opponent, opponent_board, row, target)

    def battlecry(self, board, player, opponent, opponent_board, row, target):
        for b in [board, opponent_board]:
            for row in b.rows:
                for card in row:
                    if isinstance(card, WeatherCard):
                        card.destroy(b, b.player)
