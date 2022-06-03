from gwent.cards.unit.unit_card import UnitCard


class MoraleBoostCard(UnitCard):

    def __init__(self, name, faction, row, strength, hero, agile):
        super().__init__(name, faction, row, strength, hero, agile)
        self.morale_boost = True
