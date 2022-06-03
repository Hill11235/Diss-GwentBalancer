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

    def __init__(self, name, faction, row, strength):
        self.name = name
        self.faction = faction
        self.row = row
        self.strength = strength
        self.hero = False
        self.horn = False

    def get_active_strength(self, board):
        return self.strength

    def place_card(self, board, player, opponent, opponent_board):
        pass

    def get_row(self):
        return [self.row]

    def get_targets(self, player):
        return None

    def destroy(self, board, player, decoy=False):
        # Remove from row in board (board attribute)
        board.rows[self.row].remove(self)

        # add to graveyard if not a decoy card (player attribute)
        if not decoy:
            player.graveyard.append(self)

    def get_name(self):
        return self.name
