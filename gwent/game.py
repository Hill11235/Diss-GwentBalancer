class GameState:

    # TODO complete game completion check
    # TODO complete game loop check and create basic options check for each player
    # TODO create logic flow for each available option and matching method
    # TODO create basic CLI so that a game can be played

    def __init__(self, board1, board2):
        self.board1 = board1
        self.board2 = board2
        self.player1 = board1.player
        self.player2 = board2.player

    def game_loop(self, verbose=False):
        # nest turn loop within game completion look
        # have a player go first and then alternate at the end of turn
        # give options to pass or play
        while not self.check_game_complete():
            while not self.player1.passed and not self.player2.passed:
                # get play choice
                pass
            self.player1.reset_round()
            self.player2.reset_round()
        pass

    def check_game_complete(self):
        return self.player1.lives <= 0 or self.player2.lives <= 0

    # options each turn
    # - pass (set player as passed, check if both players passed)
    # - play a card (if hand not empty)
    #     - choose a card to play
    #     - choose row (if there are options)
    #     - choose target (if there are options)

    def get_options(self, player):
        num_options = 1 + len(player.hand)
        return num_options

    def get_game_data(self):
        # get final game data
        pass
