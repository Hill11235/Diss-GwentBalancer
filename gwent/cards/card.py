# represents a card, superclass for all other card classes.
class Card:

    def __init__(self, card_id, name, faction, row, strength, hero, agile):
        self.card_id = card_id
        self.name = name
        self.faction = faction
        self.row = row
        self.strength = strength
        self.hero = hero
        self.agile = agile
        self.morale_boost = False
        self.horn = False
        self.horn_special = False
        self.weather = False
        self.unit = True

    def get_active_strength(self, board):
        # return the strength of a given card given all possible effects.

        return self.strength

    def place_card(self, board, opponent_board, row, target):
        # place a given card in a specified row, with a specified target.

        pass

    def get_row(self, board):
        # return the row associated with this card as a list.

        return [self.row]

    def get_targets(self, board):
        # return all available targets for this card.

        return None

    def destroy(self, board, decoy=False):
        # removes this cards from the board, if not being removed as a result of a decoy then add to the graveyard.

        if self.agile:
            if board.rows[0].__contains__(self):
                board.rows[0].remove(self)
            elif board.rows[1].__contains__(self):
                board.rows[1].remove(self)
        else:
            board.rows[self.row].remove(self)

        # add to graveyard if not a decoy card.
        if not decoy:
            board.player.graveyard.append(self)

    def get_data(self):
        # get card data in a dictionary.

        card_data = {
            'card_id': self.card_id,
            'name': self.name,
            'faction': self.faction,
            'row': self.row,
            'strength': self.strength,
            'hero': self.hero,
            'agile': self.agile,
            'morale_boost': self.morale_boost,
            'horn': self.horn,
            'horn_special': self.horn_special,
            'weather': self.weather
        }

        return card_data
