class Player:

    def __init__(self, name, faction):
        self.name = name
        self.faction = faction

        self.passed = False
        self.ready = False
        self.lives = 2
        self.mulligan = 0

        self.deck = []
        self.graveyard = []
        self.hand = []

    # TODO general getter methods
    # TODO think about how to add initial decks
    # TODO mulligan method
    # TODO draw card method
    # TODO get JSON data method

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
