import os
from unittest import TestCase
from gwent import *
from agent import *
from gwent.data.card_db import CardDB


class TestNode(TestCase):

    def setUp(self):
        test_decks = "data/test_decks.csv"
        parent_dir = os.path.dirname(__file__)
        file_name = "./../../gwent/data/card_data.csv"
        faction = "Nilfgaardian"
        size = 22
        seed = 123

        self.card_db = CardDB(os.path.join(parent_dir, file_name))
        self.deck = Deck(self.card_db, faction, size, seed)
        self.monster, self.nilf, self.northern, self.scoiatael = self.deck.create_deck_using_list(test_decks)

        self.player1 = Player("p1", "Nilfgaardian", self.nilf)
        self.player2 = Player("p2", "Monster", self.monster)
        self.board1 = Board(self.player1)
        self.board2 = Board(self.player2)
        self.game = GameState(self.board1, self.board2)

        self.node1 = Node(self.game, None)

    def test_is_leaf(self):
        self.assertTrue(self.node1.is_leaf())
        self.node1.get_all_children()
        self.assertFalse(self.node1.is_leaf())

    def test_is_terminal(self):
        self.assertFalse(self.node1.is_terminal())
        self.player1.lives = 0
        self.assertTrue(self.node1.is_terminal())

    def test_get_all_children(self):
        self.game.starter = 0
        children = self.node1.get_all_children()
        self.assertEqual(len(children), 11)

    def test_get_random_child(self):
        self.assertIsNone(self.node1.get_random_child())
        children = self.node1.get_all_children()
        self.assertTrue(children.__contains__(self.node1.get_random_child()))
