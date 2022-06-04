from gwent.cards.unit.unit_card import UnitCard


class MoraleBoostCard(UnitCard):

    def __init__(self, card_id, name, faction, row, strength, hero, agile):
        super().__init__(card_id, name, faction, row, strength, hero, agile)
        self.morale_boost = True
