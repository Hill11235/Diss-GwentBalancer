import random


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

    def game_loop(self, verbose=False):
        print("Starting player is ", self.player_list[self.starter])
        round_counter = 0
        turn_count = 0

        while not self.check_game_complete():
            print("Round ",  round_counter)

            while not self.player1.passed and not self.player2.passed:
                active_player = self.player_list[self.starter]
                number_options = self.get_num_options(active_player)
                print("There are ", number_options, " choices")
                self.print_options()
                choice = int(input("Please choose one of the above options."))

                if choice == 0:
                    active_player.pass_round()
                else:
                    chosen_card = active_player.hand[choice - 1]
                    rows = chosen_card.get_row()
                    targets = chosen_card.get_targets()
                    chosen_target = 0

                    if len(rows) > 1:
                        print("Available rows: ", rows)
                        chosen_row = int(input("Please choose one of the available rows:"))
                    else:
                        chosen_row = rows[0]

                    if targets is not None:
                        print("There are ", len(targets), " targets")
                        for i in range(len(targets)):
                            print(i, ": ", targets[i])
                        chosen_target = int(input("Please choose one of the available targets:"))

                    chosen_card.place_card(self.board_list[self.starter],
                                           active_player,
                                           self.player_list[(self.starter + 1) % 2],
                                           self.board_list[(self.starter + 1) % 2],
                                           chosen_row,
                                           chosen_target)

                turn_count += 1
                self.alternate_player()

            self.end_of_round()
            round_counter += 1

        print("Winner is: ")

    def end_of_round(self):
        self.set_scores()
        self.update_lives()
        self.set_player_turn()
        self.board1.clear_board()
        self.board2.clear_board()
        self.player1.reset_round()
        self.player2.reset_round()

    def alternate_player(self):
        if not self.player1.passed and not self.player2.passed:
            self.starter = (self.starter + 1) % 2
        elif self.player1.passed and not self.player2.passed:
            self.starter = 1
        elif self.player2.passed and not self.player1.passed:
            self.starter = 0

    def check_game_complete(self):
        return self.player1.lives <= 0 or self.player2.lives <= 0

    def get_num_options(self, player):
        num_options = 1 + len(player.hand)
        return num_options

    def print_options(self):
        active_player = self.player_list[self.starter]
        options = self.get_num_options(active_player)

        print("0: pass")
        for i in range(1, options):
            print(i, ": ", active_player.hand[i - 1])

    def set_player_turn(self):
        index = len(self.scores) - 1
        if self.scores[index - 1] == self.scores[index]:
            # need to add factional logic here if to be included
            self.starter = random.randint(0, 1)
        elif self.scores[index - 1] < self.scores[index]:
            self.starter = 1
        else:
            self.starter = 0

    def set_scores(self):
        self.scores.append(sum(self.board1.score()))
        self.scores.append(sum(self.board2.score()))

    def update_lives(self):
        p1_score = self.scores[len(self.scores) - 2]
        p2_score = self.scores[len(self.scores) - 1]

        if p1_score == p2_score:
            # need to add factional logic here if to be included
            self.player1.lose_round()
            self.player2.lose_round()
        elif p1_score > p2_score:
            self.player2.lose_round()
        else:
            self.player1.lose_round()

    def get_game_data(self):
        # get final game data
        pass
