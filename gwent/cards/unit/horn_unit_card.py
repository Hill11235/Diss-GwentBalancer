from gwent.cards.unit.unit_card import UnitCard


# class for unit cards with a horn effect.
class HornUnitCard(UnitCard):

    def __init__(self, card_id, name, faction, row, strength, hero, agile):
        super().__init__(card_id, name, faction, row, strength, hero, agile)
        self.horn = True
