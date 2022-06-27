from gwent.game import GameState
from gwent.player import Player
from gwent.deck import Deck
from gwent.board import Board


class TestGame:

    def func(self):
        test_decks = "data/test_decks.csv"
        file_name = "data/card_data.csv"
        faction = "Nilfgaardian"
        size = 22
        seed = 123

        deck = Deck(file_name, faction, size, seed)
        monster, nilf, northern, scoiatael = deck.create_deck_using_list(test_decks)

        playerMonster = Player("p2", "Monster", monster)
        playerNorth = Player("p3", "Northern", northern)
        board2 = Board(playerMonster)
        board3 = Board(playerNorth)

        game = GameState(board2, board3)

        game.game_loop()


if __name__ == '__main__':
    TestGame().func()
