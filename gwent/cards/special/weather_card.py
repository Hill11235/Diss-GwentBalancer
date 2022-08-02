from gwent.cards.special.special_card import SpecialCard


# weather special card.
class WeatherCard(SpecialCard):

    def __init__(self, card_id, name, faction, row, strength, hero, agile):
        super().__init__(card_id, name, faction, row, strength, hero, agile)
        self.weather = True

    def place_card(self, board, opponent_board, row, target):
        # remove from hand, and add to both boards.

        board.player.remove_card_from_hand(self.card_id)
        for b in [board, opponent_board]:
            b.rows[self.row].append(self)
