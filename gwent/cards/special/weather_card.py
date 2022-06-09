from gwent.cards.special.special_card import SpecialCard


class WeatherCard(SpecialCard):

    def __init__(self, card_id, name, faction, row, strength):
        super().__init__(card_id, name, faction, row, strength)
        self.weather = True

    def place_card(self, board, player, opponent, opponent_board, row, target):
        for b in [board, opponent_board]:
            b.rows[self.row].append(self)
