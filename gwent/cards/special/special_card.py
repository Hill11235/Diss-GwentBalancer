from gwent.cards.card import Card


class SpecialCard(Card):

    def __init__(self, name, faction, row, strength):
        super().__init__(self, name, faction, row, strength)
