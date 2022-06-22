import unittest
from gwent import *


class GameStateTest(unittest.TestCase):

    def setUp(self):
        test_decks = "data/test_decks.csv"
        file_name = "data/card_data.csv"
        faction = "Nilfgaardian"
        size = 22
        seed = 123

        self.deck = Deck(file_name, faction, size, seed)
        self.monster, self.nilf, self.northern, self.scoiatael = self.deck.create_deck_using_list(test_decks)

        self.player1 = Player("p1", "Nilfgaardian", self.nilf)
        self.player2 = Player("p2", "Monster", self.monster)
        self.board1 = Board(self.player1)
        self.board2 = Board(self.player2)
        self.game = GameState(self.board1, self.board2)

    def test_initial_setup(self):
        self.assertEqual(self.board1.score(), [0, 0, 0])
        for row in self.board1.rows:
            self.assertEqual(len(row), 0)

    def test_clear_board(self):
        pass

    def test_set_score(self):
        # test that scores can be added in GameState
        pass

    def test_lives_update(self):
        # call set scores and then check that each player's lives are decremented as expected as it's a draw
        pass

    def test_set_player_turn(self):
        # manually adjust scores in game state and then test the order for the three different scenarios
        pass

    def test_get_num_options(self):
        # test there are eleven options to begin with
        pass

    def test_check_game_complete(self):
        # check incomplete at start, manually override lives and test complete
        pass

    def test_alternate_player(self):
        # manually override passed for each player and check that the active player alternates properly
        pass
