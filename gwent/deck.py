import os
import csv
import random


# Deck class to store cards for each player.
class Deck:

    def __init__(self, card_db, faction, size, seed):
        random.seed(seed)
        self.faction = faction
        self.size = size
        self.all_cards = card_db.get_all_cards()
        self.deck = []

        self.create_deck(faction, size)

    def create_deck(self, faction, size):
        # create a deck list based on the faction, deck size, and random seed information provided.
        applicable_cards = self.get_faction_cards(self.all_cards, faction)
        self.deck = random.sample(applicable_cards, size)
        return self.deck

    def create_four_random_decks(self):
        # creates and returns a random deck for each faction.
        monster_deck = self.create_deck("monster", self.size)
        nilf_deck = self.create_deck("nilfgaardian", self.size)
        northern_deck = self.create_deck("northern", self.size)
        scoiatael_deck = self.create_deck("scoiatael", self.size)

        return monster_deck, nilf_deck, northern_deck, scoiatael_deck

    def create_deck_using_list(self, deck_list_path):
        # create a deck based on a provided csv of card ids.
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
        # return all neutral cards and cards of a given faction.
        relevant_cards = []
        for c in cards:
            if c.faction in [faction, 'neutral']:
                relevant_cards.append(c)

        return relevant_cards

    def get_card_by_id(self, card_id):
        # return a given card based on the provided card id.
        for c in self.all_cards:
            if c.card_id == card_id:
                return c
