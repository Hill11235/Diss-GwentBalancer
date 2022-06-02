from gwent.cards.unit.unit_card import UnitCard
from gwent.cards.special.weather_card import WeatherCard


class TightBondCard(UnitCard):

    def get_active_strength(self, board):
        num_comrades = 0
        horn_buff = self.get_horn_buff(board)
        morale_buff = self.get_morale_buff(board)

        for card in board.rows[self.row]:
            if card.name == self.name:
                num_comrades += 1

        if any(isinstance(card, WeatherCard) for card in board.rows[self.row]):
            return (num_comrades + morale_buff) * horn_buff
        else:
            return ((self.strength * num_comrades) + morale_buff) * horn_buff
