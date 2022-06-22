from gwent.cards.special.special_card import SpecialCard


class WeatherCard(SpecialCard):

    def __init__(self, card_id, name, faction, row, strength, hero, agile):
        super().__init__(card_id, name, faction, row, strength, hero, agile)
        self.weather = True

    def place_card(self, board, player, opponent, opponent_board, row, target):
        player.remove_card_from_hand(self.card_id)
        for b in [board, opponent_board]:
            b.rows[self.row].append(self)
