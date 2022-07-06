from unittest import TestCase
from gwent import *
from gwent.cards import *
from agent import *
from gwent.data.card_db import CardDB


class TestGameState(TestCase):

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
        self.game = GameState(self.board1, self.board2)

    def test_get_all_children_complete(self):
        self.player1.lives = 0
        self.assertIsNone(self.game.get_all_children())

    def test_get_all_children_incomplete(self):
        self.game.starter = 0
        self.player1.hand.clear()
        medic = MedicCard("2", "medic", "Monster", 0, 6, False, False)
        card = UnitCard("1", "random1", "Monster", 0, 5, False, True)
        self.player1.hand.append(medic)
        self.player1.hand.append(card)

        unit1 = UnitCard("3", "random2", "Monster", 0, 3, False, False)
        unit4 = UnitCard("3", "random3", "Monster", 0, 3, False, False)
        self.player1.graveyard.append(unit1)
        self.player1.graveyard.append(unit4)

        children = self.game.get_all_children()
        self.assertEqual(len(children), 5)
        self.assertTrue(children[0].player1.passed)

        self.assertTrue(children[1].board1.rows[0][0].name == "medic")
        self.assertTrue(children[1].board1.rows[0][1].name == "random2")

        self.assertTrue(children[2].board1.rows[0][0].name == "medic")
        self.assertTrue(children[2].board1.rows[0][1].name == "random3")

        self.assertTrue(children[3].board1.rows[0][0].name == "random1")

        self.assertTrue(children[4].board1.rows[1][0].name == "random1")

    def test_generate_options(self):
        self.game.starter = 0
        self.player1.hand.clear()

        medic = MedicCard("2", "medic", "Monster", 0, 6, False, False)
        card = UnitCard("1", "random", "Monster", 0, 5, False, True)
        self.player1.hand.append(medic)
        self.player1.hand.append(card)

        # add two standard unit cards to graveyard
        unit1 = UnitCard("3", "random", "Monster", 0, 3, False, False)
        unit4 = UnitCard("3", "random", "Monster", 0, 3, False, False)
        self.player1.graveyard.append(unit1)
        self.player1.graveyard.append(unit4)

        # check the options
        options = self.game.generate_options()
        self.assertEqual(len(options), 5)
        self.assertEqual(options, [[0, None, None], [1, 0, 0], [1, 0, 1], [2, 0, None], [2, 1, None]])

    def test_get_placement_permutations(self):
        self.game.starter = 0
        self.player1.hand.clear()

        medic = MedicCard("2", "medic", "Monster", 0, 6, False, True)
        self.player1.hand.append(medic)

        unit1 = UnitCard("3", "random", "Monster", 0, 3, False, False)
        unit4 = UnitCard("3", "random", "Monster", 0, 3, False, False)
        self.player1.graveyard.append(unit1)
        self.player1.graveyard.append(unit4)

        perm = self.game.get_placement_permutations(0, medic.get_row(self.board1), medic.get_targets(self.board1))
        self.assertEqual(len(perm), 4)
        self.assertEqual(perm, [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1]])

    def test_make_play_pass(self):
        # test pass
        self.game.starter = 0
        passed_game = self.game.make_play(0, 0, 0)
        self.assertTrue(passed_game.player1.passed)

    def test_make_play_card(self):
        # test card being played
        self.game.starter = 0
        self.player1.hand.clear()
        card = UnitCard("1", "random", "Monster", 0, 5, False, False)
        self.player1.hand.append(card)
        updated_game = self.game.make_play(1, 0, None)

        self.assertFalse(self.player1.passed)
        self.assertEqual(len(updated_game.board1.rows[0]), 1)
        self.assertTrue(updated_game.board1.rows[0][0].name == "random")

    def test_make_random_play(self):
        self.game.starter = 0
        self.player1.hand.clear()
        card = UnitCard("1", "random", "Monster", 0, 5, False, False)
        self.player1.hand.append(card)

        self.game.make_random_play()

        # check either passed or card played
        self.assertTrue(self.player1.passed or self.game.board1.rows[0][0].name == "random")

    def test_round_over(self):
        self.assertFalse(self.game.round_over())
        self.player1.passed = True
        self.player2.passed = True
        self.assertTrue(self.game.round_over())

    def test_alternate_player(self):
        initial_turn = self.game.starter
        self.game.alternate_player()
        updated_turn = (initial_turn + 1) % 2
        self.assertEqual(self.game.starter, updated_turn)

        self.player1.passed = True
        self.game.alternate_player()
        self.assertEqual(self.game.starter, 1)

    def test_check_game_complete(self):
        self.assertFalse(self.game.check_game_complete())
        self.player1.lives = 0
        self.assertTrue(self.game.check_game_complete())

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

    def test_set_scores(self):
        self.game.set_scores()
        self.assertEqual(self.game.scores, [0, 0])

    def test_update_lives(self):
        self.game.set_scores()
        self.game.update_lives()

        self.assertEqual(self.player1.lives, 1)
        self.assertEqual(self.player2.lives, 1)

        self.game.scores.append(1)
        self.game.scores.append(3)
        self.game.update_lives()

        self.assertEqual(self.player1.lives, 0)
        self.assertEqual(self.player2.lives, 1)

    def test_get_result(self):
        self.player1.lives = 0
        self.player2.lives = 0
        self.assertIsNone(self.game.get_result())

        self.player1.lives = 1
        self.player2.lives = 0
        self.assertEqual(self.game.get_result(), 0)

        self.player1.lives = 0
        self.player2.lives = 1
        self.assertEqual(self.game.get_result(), 1)

    def test_get_game_data(self):
        game_dict = self.game.get_game_data()
        self.assertEqual(len(game_dict), 3)
        self.assertEqual(game_dict.get('score'), [])

        self.game.scores.append(7)
        self.game.scores.append(3)

        game_dict = self.game.get_game_data()
        self.assertEqual(len(game_dict), 3)
        self.assertEqual(game_dict.get('score'), [7, 3])
