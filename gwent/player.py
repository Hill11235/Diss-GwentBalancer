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
    # TODO pass method and reset passed method
    # TODO lose method, decrement lives
    # TODO think about how to add initial decks
    # TODO mulligan method
    # TODO draw card method
    # TODO get JSON data method
