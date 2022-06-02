from gwent.cards.card import Card
from gwent.cards.unit.horn_unit_card import HornUnitCard

# TODO add tightbond card
class UnitCard(Card):

    def __init__(self, name, faction, row, strength, hero, agile):
        super().__init__(self, name, faction, row, strength)
        self.hero = hero
        self.agile = agile
        self.morale_boost = False

    def get_row(self):
        if self.agile:
            return [0, 1]
        return [self.row]

    def get_active_strength(self, board):
        modifier = self.get_strength_modifier(self, board)

        if self.hero:
            return self.strength
        else:
            pass
        pass

    def get_strength_modifier(self, board):
        # check for morale boosts and horns

        return 1

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
