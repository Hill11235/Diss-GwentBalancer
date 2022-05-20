class Card:

    def __init__(self, name, faction, ability, row, strength, hero=False):
        self.name = name
        self.faction = faction
        self.ability = ability
        self.row = row
        self.strength = strength
        self.hero = hero

    def get_strength(self):
        return self.strength

    def get_name(self):
        return self.name

    def destroy(self):
        a = 1
        # add to graveyard (player attribute)
        # Remove from row in board (board attribute)
