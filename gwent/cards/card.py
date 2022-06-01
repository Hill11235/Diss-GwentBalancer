class Card:

    def __init__(self, name, faction, row, strength):
        self.name = name
        self.faction = faction
        self.row = row
        self.strength = strength
        self.hero = False
        self.horn = False

    def get_active_strength(self):
        return self.strength

    def place_card(self):
        pass

    def destroy(self):
        # add to graveyard (player attribute)
        # Remove from row in board (board attribute)
        pass

    def get_name(self):
        return self.name
