class GameState:

    # TODO complete constructor
    # TODO complete game completion check
    # TODO complete game loop check and create basic options check for each player
    # TODO create logic flow for each available option and matching method
    # TODO create basic CLI so that a game can be played

    def __init__(self):
        # set up players, decks, board (using card db)
        pass

    def game_loop(self):
        # need to set up some kind of loop which runs through each round
        while (not self.check_game_complete()):
            pass
        pass

    def check_game_complete(self):
        # check if either players lives are at zero
        return True

    # options each turn
    # - pass
    # - play a card
    #
