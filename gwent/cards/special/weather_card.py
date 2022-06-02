from gwent.cards.special.special_card import SpecialCard


class WeatherCard(SpecialCard):

    def __init__(self, name, faction, row, strength):
        super().__init__(name, faction, row, strength)
