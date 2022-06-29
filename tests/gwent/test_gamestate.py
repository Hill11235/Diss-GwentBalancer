import unittest
from gwent import *
from gwent.data.card_db import CardDB


class GameStateTest(unittest.TestCase):

    def setUp(self):
        test_decks = "data/test_decks.csv"
        file_name = "card_data.csv"
        faction = "Nilfgaardian"
        size = 22
        seed = 123

        self.card_db = CardDB(file_name)
        self.deck = Deck(self.card_db, faction, size, seed)
        self.monster, self.nilf, self.northern, self.scoiatael = self.deck.create_deck_using_list(test_decks)

        self.player1 = Player("p1", "Nilfgaardian", self.nilf)
        self.player2 = Player("p2", "Monster", self.monster)
        self.board1 = Board(self.player1)
        self.board2 = Board(self.player2)
        self.game = PvpGame(self.board1, self.board2)

    def test_initial_setup(self):
        self.assertEqual(self.board1.score(), [0, 0, 0])
        for row in self.board1.rows:
            self.assertEqual(len(row), 0)

    def test_set_score(self):
        self.game.set_scores()
        self.assertEqual(self.game.scores, [0, 0])

    def test_lives_update(self):
        self.game.set_scores()
        self.game.update_lives()

        self.assertEqual(self.player1.lives, 1)
        self.assertEqual(self.player2.lives, 1)

        self.game.scores.append(1)
        self.game.scores.append(3)
        self.game.update_lives()

        self.assertEqual(self.player1.lives, 0)
        self.assertEqual(self.player2.lives, 1)

    def test_set_player_turn(self):
        self.assertIn(self.game.starter, [0, 1])
        self.game.scores.append(1)
        self.game.scores.append(3)
        self.game.set_player_turn()
        self.assertEqual(self.game.starter, 1)

        self.game.scores.append(7)
        self.game.scores.append(3)
        self.game.set_player_turn()
        self.assertEqual(self.game.starter, 0)

        self.game.scores.append(3)
        self.game.scores.append(3)
        self.game.set_player_turn()
        self.assertIn(self.game.starter, [0, 1])

    def test_get_num_options(self):
        self.assertEqual(self.game.get_num_options(self.player1), 11)
        self.assertEqual(self.game.get_num_options(self.player2), 11)

    def test_check_game_complete(self):
        self.assertFalse(self.game.check_game_complete())
        self.player1.lives = 0
        self.assertTrue(self.game.check_game_complete())

    def test_alternate_player(self):
        initial_turn = self.game.starter
        self.game.alternate_player()
        updated_turn = (initial_turn + 1) % 2
        self.assertEqual(self.game.starter, updated_turn)

        self.player1.passed = True
        self.game.alternate_player()
        self.assertEqual(self.game.starter, 1)

    def test_get_game_data(self):
        game_dict = self.game.get_game_data()
        self.assertEqual(len(game_dict), 3)
        self.assertEqual(game_dict.get('score'), [])

        self.game.scores.append(7)
        self.game.scores.append(3)

        game_dict = self.game.get_game_data()
        self.assertEqual(len(game_dict), 3)
        self.assertEqual(game_dict.get('score'), [7, 3])
