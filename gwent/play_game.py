import pyfiglet
from gwent.pvp_game import PvpGame
from gwent.player import Player
from gwent.deck import Deck
from gwent.board import Board
from gwent.data.card_db import CardDB


# Allows users to play the game via the command line.
class TestGame:

    def play_game(self):
        # create decks and initiates game.
        file_name = "card_data.csv"
        print(pyfiglet.figlet_format("GWENT"))
        print("\nWelcome to Gwent\n")
        seed = int(input("Please enter a positive integer to be used as a random seed: "))
        faction1 = input("Please choose the faction for player 1 by typing one of the below: "
                         "\nmonster\nnilfgaardian\nnorthern\nscoiatael\n\n")
        faction2 = input("\nPlease choose the faction for player 2by typing one of the below: "
                         "\nmonster\nnilfgaardian\nnorthern\nscoiatael\n\n")
        print("")
        size = 22

        card_db = CardDB(file_name)
        deck1 = Deck(card_db, faction1, size, seed)
        deck2 = Deck(card_db, faction2, size, seed)

        player1 = Player("p1", faction1, deck1.deck)
        player2 = Player("p2", faction2, deck2.deck)
        board1 = Board(player1)
        board2 = Board(player2)

        game = PvpGame(board1, board2)
        game.starter = 0

        game.game_loop()


if __name__ == '__main__':
    TestGame().play_game()
