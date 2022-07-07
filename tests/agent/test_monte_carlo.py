from unittest import TestCase
from gwent import *
from agent import *
from gwent.data.card_db import CardDB


class TestMCTS(TestCase):

    def setUp(self):
        test_decks = "data/test_decks.csv"
        file_name = "card_data.csv"
        faction = "Nilfgaardian"
        size = 22
        seed = 123

        self.card_db = CardDB(file_name)
        self.deck = Deck(self.card_db, faction, size, seed)
        self.monster, self.nilf, self.northern, self.scoiatael = self.deck.create_deck_using_list(test_decks)

        self.player1 = Player("p1", "Northern", self.northern)
        self.player2 = Player("p2", "Monster", self.monster)
        self.board1 = Board(self.player1)
        self.board2 = Board(self.player2)
        self.game = GameState(self.board1, self.board2)
        self.node = Node(self.game, None)
        self.mcts = MCTS()

    def test_run_search(self):
        self.fail()

    def test_get_best_play(self):
        self.fail()

    def test_selection(self):
        self.fail()

    def test_expand(self):
        self.fail()

    def test_simulate(self):
        for i in range(100):
            result = self.mcts.simulate(self.node)
            self.assertTrue(result in [None, 0, 1])

    def test_backpropagate(self):
        self.game.starter = 0
        node2 = Node(self.game, self.node)
        node3 = Node(self.game, node2)

        self.mcts.backpropagate(node3, 0)
        self.assertEqual(node3.number_visits, 1)
        self.assertEqual(node2.number_visits, 1)
        self.assertEqual(self.node.number_visits, 1)
        self.assertEqual(node3.wins, 1)
        self.assertEqual(node2.wins, 1)
        self.assertEqual(self.node.wins, 1)

    def test_get_ucb1(self):
        self.assertIsNone(self.mcts.get_ucb1(self.node))
        node2 = Node(self.game, self.node)
        self.node.number_visits = 5
        node2.number_visits = 3

        self.assertEqual(self.mcts.get_ucb1(node2), 1.03583715336408)

