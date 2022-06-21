import random


class Player:

    def __init__(self, name, faction, deck):
        self.name = name
        self.faction = faction

        self.passed = False
        self.ready = False
        self.lives = 2
        self.mulligan = 0

        self.hand = []
        self.deck = deck
        self.set_hand()
        self.graveyard = []

    # TODO general getter methods
    # TODO think about how to add initial decks
    # TODO get JSON data method

    def set_hand(self):
        for i in range(10):
            self.draw_card()

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
