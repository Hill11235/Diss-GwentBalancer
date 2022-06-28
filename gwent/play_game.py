from gwent.game import GameState
from gwent.player import Player
from gwent.deck import Deck
from gwent.board import Board
from gwent.data.card_db import CardDB


class TestGame:

    def func(self):
        test_decks = "data/test_decks.csv"
        file_name = "card_data.csv"
        faction = "Nilfgaardian"
        size = 22
        seed = 123

        card_db = CardDB(file_name)
        deck = Deck(card_db, faction, size, seed)
        monster, nilf, northern, scoiatael = deck.create_deck_using_list(test_decks)

        player_nilf = Player("p1", "Nilfgaardian", nilf)
        player_monster = Player("p2", "Monster", monster)
        player_north = Player("p3", "Northern", northern)
        player_scoiatael = Player("p4", "Scoiatael", scoiatael)
        board1 = Board(player_nilf)
        board2 = Board(player_monster)
        board3 = Board(player_north)
        board4 = Board(player_scoiatael)

        game = GameState(board1, board4)
        game.starter = 0

        game.game_loop()


if __name__ == '__main__':
    TestGame().func()
