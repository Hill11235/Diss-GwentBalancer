import os
import csv
import random
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


# TODO potentially split into reader and deck classes?
class Deck:

    def __init__(self, file_path, faction, size, seed):
        random.seed(seed)
        self.file_path = file_path
        self.faction = faction
        self.size = size
        self.all_cards = []
        self.deck = []

        self.read_card_information()
        self.create_deck(faction, size)

    def read_card_information(self):
        # read in csv file provided and create and store cards in list
        with open(os.path.join("./gwent/data/", self.file_path)) as file:
            card_data = csv.DictReader(file)
            for cards in card_data:
                if cards[self.faction] != "":
                    for i in range(cards['Quantity']):
                        if cards['power'] == -1:
                            new_card = constructor_dic[cards['ability']](
                                cards['id'],
                                cards['name'],
                                cards['faction'],
                                cards['type'],
                                cards['power']
                            )
                            self.all_cards.append(new_card)
                        else:
                            new_card = constructor_dic[cards['ability'].split(',')[0]](
                                cards['id'],
                                cards['name'],
                                cards['faction'],
                                cards['type'],
                                cards['power'],
                                'hero' in cards['ability'].split(','),
                                'agile' in cards['ability'].split(',')
                            )
                            self.all_cards.append(new_card)

    def create_deck(self, faction, size):
        # create a deck list based on the faction, deck size, and random seed information provided
        card_list = copy.deepcopy(self.all_cards)
        applicable_cards = self.get_relevant_cards(card_list, faction)
        self.deck = random.sample(applicable_cards, size)

    def get_relevant_cards(self, cards, faction):
        relevant_cards = []
        for c in cards:
            if c.faction in [faction, 'neutral']:
                relevant_cards.append(c)

        return relevant_cards

    def get_deck(self):
        return self.deck
