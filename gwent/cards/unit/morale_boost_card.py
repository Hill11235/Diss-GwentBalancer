from gwent.cards.unit.unit_card import UnitCard


# morale boost unit card.
class MoraleBoostCard(UnitCard):

    def __init__(self, card_id, name, faction, row, strength, hero, agile):
        super().__init__(card_id, name, faction, row, strength, hero, agile)
        self.morale_boost = True
