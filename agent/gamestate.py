import random
from copy import deepcopy
from itertools import product


# search and node based game class.
class GameState:

    def __init__(self, board1, board2):
        self.board1 = board1
        self.board2 = board2
        self.player1 = board1.player
        self.player2 = board2.player
        self.player_list = [self.player1, self.player2]
        self.board_list = [self.board1, self.board2]
        self.starter = random.randint(0, 1)
        self.scores = []

    def get_all_children(self):
        # return a list of all gamestates that can be reached from this one with one action.

        if self.check_game_complete():
            return None
        children = []
        options = self.generate_options()

        for option in options:
            children.append(self.make_play(option[0], option[1], option[2]))

        return children

    def generate_options(self):
        # get all options for plays, including index of card in hand, row number, and target number.

        active_player = self.player_list[self.starter]
        active_board = self.board_list[self.starter]
        options = [[0, None, None]]

        for i in range(len(active_player.hand)):
            active_card = active_player.hand[i]
            rows = active_card.get_row(active_board)
            targets = active_card.get_targets(active_board)
            options.extend(self.get_placement_permutations(i + 1, rows, targets))

        return options

    def get_placement_permutations(self, num, rows, targets):
        # get list of different placement permutations for a given card.
        permutations = []

        if targets is None:
            if len(rows) == 1:
                permutations.append([num, rows[0], None])
            elif len(rows) < 0:
                permutations.append([num, -1, None])
            else:
                for row in rows:
                    permutations.append([num, row, None])
        else:
            target_idx = range(len(targets))
            for perm in product(rows, target_idx):
                permutations.append([num, perm[0], perm[1]])

        return permutations

    def make_play(self, index, row, target):
        # make play, either passing or playing a card, and return a new game state.

        new_gamestate = deepcopy(self)
        active_player = new_gamestate.player_list[new_gamestate.starter]
        active_board = new_gamestate.board_list[new_gamestate.starter]

        if index == 0:
            active_player.pass_round()
        else:
            card = active_player.hand[index - 1]
            if target is not None:
                targets = card.get_targets(active_board)
                target = targets[target]
            card.place_card(new_gamestate.board_list[new_gamestate.starter],
                            new_gamestate.board_list[(new_gamestate.starter + 1) % 2],
                            row,
                            target)

        new_gamestate.alternate_player()

        if new_gamestate.round_over():
            new_gamestate.end_of_round()

        return new_gamestate

    def make_random_play(self):
        # make a random play, and return a new game state.

        active_player = self.player_list[self.starter]
        active_board = self.board_list[self.starter]
        index = random.randint(0, len(active_player.hand))

        if index == 0:
            active_player.pass_round()
        else:
            active_card = active_player.hand[index - 1]
            rows = active_card.get_row(active_board)
            targets = active_card.get_targets(active_board)
            if targets is not None and targets != []:
                targets = random.choice(targets)
            else:
                targets = None
            if len(rows) > 0:
                row = random.choice(rows)
            else:
                row = -1
            active_card.place_card(self.board_list[self.starter],
                                   self.board_list[(self.starter + 1) % 2],
                                   row,
                                   targets)

        self.alternate_player()
        if self.round_over():
            self.end_of_round()

    def round_over(self):
        # return boolean indicating whether the round over or not.

        return self.player1.passed and self.player2.passed

    def end_of_round(self):
        # update gamestate at the end of each round.

        self.set_scores()
        self.update_lives()
        self.set_player_turn()
        self.board1.clear_board()
        self.board2.clear_board()
        self.player1.reset_round()
        self.player2.reset_round()

    def alternate_player(self):
        # change the active player index based on who has passed.

        if not self.player1.passed and not self.player2.passed:
            self.starter = (self.starter + 1) % 2
        elif self.player1.passed and not self.player2.passed:
            self.starter = 1
        elif self.player2.passed and not self.player1.passed:
            self.starter = 0

    def check_game_complete(self):
        # check whether the game is complete or not.

        return self.player1.lives <= 0 or self.player2.lives <= 0

    def set_player_turn(self):
        # sets the player who starts the next round based on who won the previous round.

        index = len(self.scores) - 1
        if self.scores[index - 1] == self.scores[index]:
            self.starter = random.randint(0, 1)
        elif self.scores[index - 1] < self.scores[index]:
            self.starter = 1
        else:
            self.starter = 0

    def set_scores(self):
        # set the scores based on the player's boards.

        self.scores.append(sum(self.board1.score()))
        self.scores.append(sum(self.board2.score()))

    def update_lives(self):
        # update each player's lives at the end of the round.

        p1_score = self.scores[len(self.scores) - 2]
        p2_score = self.scores[len(self.scores) - 1]

        if p1_score == p2_score:
            self.player1.lose_round()
            self.player2.lose_round()
        elif p1_score > p2_score:
            self.player2.lose_round()
        else:
            self.player1.lose_round()

    def get_result(self):
        # return the index of the winning player or none for a draw.

        if self.player1.lives == 0 and self.player2.lives == 0:
            return None
        elif self.player1.lives > self.player2.lives:
            return 0
        else:
            return 1

    def get_winning_faction(self):
        # return the faction of the winner if there is one.

        result = self.get_result()
        if result is None:
            winner = "draw"
        elif result == 0:
            winner = self.player1.faction
        else:
            winner = self.player2.faction
        return winner

    def get_game_data(self):
        # return the game data as a dictionary.

        game_dict = {
            "score": self.scores,
            "result": self.get_result(),
            "p1_faction": self.player1.faction,
            "p2_faction": self.player2.faction,
            "player1": self.player1.get_player_data(),
            "player2": self.player2.get_player_data()
        }

        return game_dict
