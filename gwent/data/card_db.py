import os
import csv
import copy
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


# responsible for reading in card data and storing it in a list.
class CardDB:

    def __init__(self, file_path):
        self.file_path = file_path
        self.all_cards = []

        self.read_card_information()

    def read_card_information(self):
        # read in csv file provided and create and store cards in list.
        parent_dir = os.path.dirname(__file__)

        with open(os.path.join(parent_dir, "card_data.csv"), encoding='utf-8-sig') as file:
            card_data = csv.DictReader(file)
            for cards in card_data:
                for i in range(int(cards['Quantity'])):
                    new_card = constructor_dic[cards['ability'].split(',')[0]](
                        cards['card_id'],
                        cards['name'],
                        cards['faction'],
                        int(cards['type']),
                        int(cards['power']),
                        'hero' in cards['ability'].split(','),
                        'agile' in cards['ability'].split(',')
                    )
                    self.all_cards.append(new_card)

    def get_all_cards(self):
        # return a copy of list of all cards.

        return copy.deepcopy(self.all_cards)
