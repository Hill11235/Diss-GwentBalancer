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
        dir_path = os.path.dirname(os.path.realpath(__file__))

        with open(os.path.join(dir_path, self.file_path), encoding='utf-8-sig') as file:
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

    def create_deck(self, faction, size):
        # create a deck list based on the faction, deck size, and random seed information provided
        card_list = copy.deepcopy(self.all_cards)
        applicable_cards = self.get_faction_cards(card_list, faction)
        self.deck = random.sample(applicable_cards, size)

    def create_deck_using_list(self, deck_list_path):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        monster_deck = []
        nilf_deck = []
        northern_deck = []
        scoiatael_deck = []

        with open(os.path.join(dir_path, deck_list_path), encoding='utf-8-sig') as file:
            card_data = csv.DictReader(file)
            for cards in card_data:
                monster_deck.append(self.get_card_by_id(cards['Monster'])) if cards['Monster'] != "" else None
                nilf_deck.append(self.get_card_by_id(cards['Nilfgaardian'])) if cards['Nilfgaardian'] != "" else None
                northern_deck.append(self.get_card_by_id(cards['Northern'])) if cards['Northern'] != "" else None
                scoiatael_deck.append(self.get_card_by_id(cards['Scoiatael'])) if cards['Scoiatael'] != "" else None

        return monster_deck, nilf_deck, northern_deck, scoiatael_deck

    def get_faction_cards(self, cards, faction):
        relevant_cards = []
        for c in cards:
            if c.faction in [faction, 'neutral']:
                relevant_cards.append(c)

        return relevant_cards

    def get_card_by_id(self, card_id):
        card_list = copy.deepcopy(self.all_cards)
        for c in card_list:
            if c.card_id == card_id:
                return c

    def get_deck(self):
        return self.deck
