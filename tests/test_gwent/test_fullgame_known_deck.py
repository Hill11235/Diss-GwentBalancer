import unittest
from unittest import mock
from gwent import *
from gwent.data.card_db import CardDB


class FullGameKnownDeckTest(unittest.TestCase):

    def setUp(self):
        test_decks = "data/test_decks.csv"
        file_name = "card_data.csv"
        faction = "Nilfgaardian"
        size = 22
        seed = 123

        self.card_db = CardDB(file_name)
        self.deck = Deck(self.card_db, faction, size, seed)
        self.monster, self.nilf, self.northern, self.scoiatael = self.deck.create_deck_using_list(test_decks)

        self.playerNilf = Player("p1", "Nilfgaardian", self.nilf)
        self.playerMonster = Player("p2", "Monster", self.monster)
        self.playerNorth = Player("p3", "Northern", self.northern)
        self.playerScoi = Player("p4", "Scoiatael", self.scoiatael)
        self.board1 = Board(self.playerNilf)
        self.board2 = Board(self.playerMonster)
        self.board3 = Board(self.playerNorth)
        self.board4 = Board(self.playerScoi)

    @mock.patch('builtins.input')
    def test_monster_vs_northern(self, mocked_input):
        monster_hand, northern_hand = self.mons_v_north_sort_hand()

        self.playerNorth.hand = northern_hand
        self.playerMonster.hand = monster_hand

        mocked_input.side_effect = ['4', '5', '3', '6', '0', '1', '0', '0',
                                    '4', '5', '2', '2', '0', '0',
                                    '1', '1', '5', '2', '1', '1', '0', '1', '1', '4', '0', '1', '2', '0', '1', '0']
        game = PvpGame(self.board2, self.board3)
        game.starter = 0
        game.game_loop()

        dicto = game.get_game_data()
        self.assertEqual(dicto.get('score'), [10, 0, 15, 17, 17, 101])

    def mons_v_north_sort_hand(self):
        monster_order = ["frightener", "arachas2", "earth_elemental", "arachas1", "arachas3",
                         "werewolf", "griffin", "kayran", "leshen", "harpy"]
        northern_order = ["blue_stripes_commando", "dandelion", "dun_banner_medic", "biting_frost",
                          "villentretenmerth", "ciri", "decoy", "clear_weather", "commanders_horn",
                          "blue_stripes_commando"]
        monster_hand = []
        northern_hand = []

        for name in monster_order:
            for card in self.playerMonster.hand:
                if card.card_id == name:
                    monster_hand.append(card)

        for name in northern_order:
            for card in self.playerNorth.hand:
                if card.card_id == name:
                    northern_hand.append(card)
                    break

        print(len(northern_hand))

        return monster_hand, northern_hand
