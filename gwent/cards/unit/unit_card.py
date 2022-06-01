from gwent.cards.card import Card

class UnitCard(Card):

    def __init__(self, name, faction, row, strength, hero, agile):
        super().__init__(self, name, faction, row, strength)
        self.hero = hero
        self.agile = agile

