import random


class Player:

    def __init__(self, name, faction, deck):
        self.name = name
        self.faction = faction

        self.passed = False
        self.lives = 2

        self.hand = []
        self.deck = deck
        self.set_hand()
        self.graveyard = []

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
        hand_dict = {}
        for cards in self.hand:
            card_dict = cards.get_data()
            hand_dict[cards.card_id] = card_dict

        graveyard_dict = {}
        for cards in self.graveyard:
            card_dict = cards.get_data()
            graveyard_dict[cards.card_id] = card_dict

        player_data = {
            "name": self.name,
            "faction": self.faction,
            "lives": self.lives,
            "hand size": len(self.hand),
            "hand": hand_dict,
            "graveyard size": len(self.graveyard),
            "graveyard": graveyard_dict,
            "size of deck": len(self.deck)
        }

        return player_data
