import random


# represents each player, stores deck and hand, and has methods for each player action in a turn.
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
        # draw ten starting cards into the player's hand.
        for i in range(10):
            self.draw_card()

    def draw_card(self):
        # draws a random card from the player's deck into their hand.
        random_card_index = random.randint(0, len(self.deck) - 1)
        drawn_card = self.deck.pop(random_card_index)
        self.hand.append(drawn_card)

    def remove_card_from_hand(self, card_ident):
        # takes a specified card and removes it from the player's hand.
        i = 0
        for cards in self.hand:
            if cards.card_id == card_ident:
                return self.hand.pop(i)
            i += 1

        return None

    def pass_round(self):
        # allows the player to pass the round.
        self.passed = True

    def reset_round(self):
        # resets the pass boolean.
        self.passed = False

    def lose_round(self):
        # decrements the life variable.
        self.lives -= 1
        return self.lives

    def get_player_data(self):
        # returns player data in a dictionary, with nested dictionaries for the player's hand and graveyard.
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
