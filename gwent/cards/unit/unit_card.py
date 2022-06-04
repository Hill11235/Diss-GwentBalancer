from gwent.cards.card import Card
from gwent.cards.unit.horn_unit_card import HornUnitCard
from gwent.cards.special.horn_special_card import HornSpecialCard
from gwent.cards.special.weather_card import WeatherCard


class UnitCard(Card):

    def __init__(self, card_id, name, faction, row, strength, hero, agile):
        super().__init__(card_id, name, faction, row, strength)
        self.hero = hero
        self.agile = agile
        self.morale_boost = False

    def get_row(self):
        if self.agile:
            return [0, 1]
        return [self.row]

    def place_card(self, board, player, opponent, opponent_board, row, target):
        self.row = row
        board.rows[self.row].append(self)
        self.battlecry(board, player, opponent, opponent_board, row, target)

    def battlecry(self, board, player, opponent, opponent_board, row, target):
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
            if isinstance(card, HornUnitCard) or isinstance(card, HornSpecialCard):
                horn *= 2

        return horn

    def get_morale_buff(self, board):
        # TODO check that the -1 behaves correctly
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
