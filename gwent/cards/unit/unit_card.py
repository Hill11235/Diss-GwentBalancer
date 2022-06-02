from gwent.cards.card import Card
from gwent.cards.unit.horn_unit_card import HornUnitCard
from gwent.cards.special.weather_card import WeatherCard


class UnitCard(Card):

    def __init__(self, name, faction, row, strength, hero, agile):
        super().__init__(name, faction, row, strength)
        self.hero = hero
        self.agile = agile
        self.morale_boost = False

    def get_row(self):
        if self.agile:
            return [0, 1]
        return [self.row]

    def place_card(self, board, rows, player, opponent, opponent_board):
        if self.agile:
            # TODO think about how to best make call on where to place an agile card
            self.row = rows[0]

        board.rows[self.row].append(self)
        self.battlecry(player, board, opponent_board)

    def battlecry(self, player, board, opponent_board):
        # calls any abilities when a card is played, overridden in subclasses
        pass

    def get_active_strength(self, board):
        horn_buff = self.get_horn_buff(board)
        morale_buff = self.get_morale_buff(board)

        if self.hero:
            return self.strength
        elif any(isinstance(card, WeatherCard) for card in board.rows[self.row]):
            return (1 + morale_buff) * horn_buff
        else:
            return (self.strength + morale_buff) * horn_buff

    def get_horn_buff(self, board):
        horn = 1

        for card in board.rows[self.row]:
            if isinstance(card, HornUnitCard):
                horn *= 2

        return horn

    def get_morale_buff(self, board):
        morale = -1 if self.morale_boost else 0

        for card in board.rows[self.row]:
            if isinstance(card, UnitCard) and card.morale_boost:
                morale += 1
        return morale

    def get_current_status(self, board=None):
        current_status = {
            "name": self.name,
            "faction": self.faction,
            "row": self.get_row(),
            "strength": self.strength,
            "hero": self.hero
        }
        if board is not None:
            current_status["active_strength"] = self.get_active_strength(board)

        return current_status
