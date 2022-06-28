import os
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

    def __init__(self, card_db, faction, size, seed):
        random.seed(seed)
        self.faction = faction
        self.size = size
        self.all_cards = card_db.get_all_cards()
        self.deck = []

        self.create_deck(faction, size)

    def create_deck(self, faction, size):
        # create a deck list based on the faction, deck size, and random seed information provided
        applicable_cards = self.get_faction_cards(self.all_cards, faction)
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
        for c in self.all_cards:
            if c.card_id == card_id:
                return c
