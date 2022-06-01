from gwent.cards.card import Card

class UnitCard(Card):

    def __init__(self, name, faction, row, strength, hero, agile):
        super().__init__(self, name, faction, row, strength)
        self.hero = hero
        self.agile = agile

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