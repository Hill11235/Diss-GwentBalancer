import csv
import random
from gwent.cards import *

constructor_dic = {
    'tight_bond': TightBondCard,
    'spy': SpyCard,
    'medic': MedicCard,
    'morale_boost': MoraleBoostCard,
    'scorch': ScorchUnitCard,
    'muster': MusterCard,
    'hero': UnitCard,
    'commanders_horn': HornUnitCard,
    'agile': UnitCard,
    '': UnitCard,
    'weather': WeatherCard,
    'decoy': DecoyCard,
    'scorch_card': ScorchSpecialCard,
    'weather_clear': ClearWeatherCard,
    'commanders_horn_card': HornSpecialCard,
}


class Deck:

    deck = []

    def __init__(self, file_path, faction, size, seed):
        self.file_path = file_path
        self.faction = faction
        self.size = size
        random.seed(seed)
        self.read_card_information(file_path)
        self.create_deck(faction, size, seed)

    def read_card_information(self, file_path):
        # read in csv file provided and create and store cards in list
        x = 3

    def create_deck(self, faction, size, seed):
        # create a deck list based on the faction, deck size, and random seed information provided
        x = 3

    def get_deck(self):
        return self.deck
