import random


class Player:

    def __init__(self, name, faction, deck):
        self.name = name
        self.faction = faction

        self.passed = False
        self.ready = False
        self.lives = 2
        self.mulligan = 0

        self.deck = deck
        self.graveyard = []
        self.hand = []

    # TODO general getter methods
    # TODO think about how to add initial decks
    # TODO get JSON data method

    def set_deck_and_hand(self):
        # set deck based on deck class
        # set hand by calling draw_card 10 times
        pass

    def draw_card(self):
        random_card_index = random.randint(0, len(self.deck) - 1)
        drawn_card = self.deck.pop(random_card_index)
        self.hand.append(drawn_card)

    def pass_round(self):
        self.passed = True

    def reset_round(self):
        self.passed = False

    def lose_round(self):
        self.lives -= 1
        return self.lives

    def get_player_data(self):
        # get name, lives, hand size, faction, passed etc as JSON/dictionary
        pass
