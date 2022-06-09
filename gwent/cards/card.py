class Card:
    """
    Class used to represent an individual card in the game.

    Attributes
    __________

    name : String
        name of a given card
    faction : String
        name of a given card's faction, empty indicates neutral card
    row : int
        the row that this card can be added to.
    strength : int
        the card's strength
    hero : boolean
        indicates whether the card is a hero card or not
    horn : boolean
        indicates whether the card has a commander's horn effect

    Methods
    _______

    TODO add methods once complete
    """

    def __init__(self, card_id, name, faction, row, strength):
        self.card_id = card_id
        self.name = name
        self.faction = faction
        self.row = row
        self.strength = strength
        self.hero = False
        self.agile = False
        self.morale_boost = False
        self.horn = False
        self.horn_special = False
        self.weather = False
        self.unit = True

    def get_active_strength(self, board):
        return self.strength

    # TODO consider if card needs to be removed from hand when placed
    # TODO Refactor to reduce number of arguments (add boards as an attribute of player?)
    def place_card(self, board, player, opponent, opponent_board, row, target):
        pass

    def get_row(self):
        return [self.row]

    def get_targets(self, player, board):
        return None

    def destroy(self, board, player, decoy=False):
        # Remove from row in board (board attribute)
        board.rows[self.row].remove(self)

        # add to graveyard if not a decoy card (player attribute)
        if not decoy:
            player.graveyard.append(self)

    def get_name(self):
        return self.name

    def get_data(self, board):
        card_data = {
            'card_id': self.card_id,
            'name': self.name,
            'faction': self.faction,
            'row': self.row,
            'strength': self.strength,
            'effective_strength': self.get_active_strength(board),
            'hero': self.hero,
            'agile': self.agile,
            'morale_boost': self.morale_boost,
            'horn': self.horn,
            'horn_special': self.horn_special,
            'weather': self.weather
        }

        return card_data
