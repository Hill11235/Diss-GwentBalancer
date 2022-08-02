import json
import os
import shutil
import pandas as pd
import numpy as np


# parse simulation data and saved summary information as csv files.
class JsonReader:

    def __init__(self, json_file, card_file, destination):
        with open(json_file) as f:
            self.data_list = json.load(f)
        self.card_file = card_file
        self.destination = destination

    def run_balance(self, iteration):
        # create summary tables, update source card file based on statistics, and save for use in next iteration.

        parent_dir = os.path.dirname(__file__)
        faction_stats = self.get_faction_overview_stats(iteration)
        card_stats = self.get_card_stats(iteration)
        game_duration_stats = self.get_game_duration_stats(iteration)
        f_v_f_stats = self.get_faction_v_faction_stats(iteration)

        faction_stats.to_csv(os.path.join(parent_dir, "stats/faction_stats.csv"),
                             mode='a', header=not os.path.exists(os.path.join(parent_dir, "stats/faction_stats.csv")),
                             index_label="faction")
        card_stats.to_csv(os.path.join(parent_dir, "stats/card_stats.csv"), mode='a',
                          header=not os.path.exists(os.path.join(parent_dir, "stats/card_stats.csv")),
                          index_label="card_id")
        game_duration_stats.to_csv(os.path.join(parent_dir, "stats/game_duration_data.csv"),
                                   mode='a',
                                   header=not os.path.exists(os.path.join(parent_dir, "stats/game_duration_data.csv")))
        f_v_f_stats.to_csv(os.path.join(parent_dir, "stats/faction_v_faction.csv"),
                           mode='a',
                           header=not os.path.exists(os.path.join(parent_dir, "stats/faction_v_faction.csv")))

        self.create_new_card_data_file(card_stats)

    def get_faction_overview_stats(self, iteration):
        # parse game data and create dataframe showing faction level performance.

        df = pd.DataFrame(0,
                          columns=["iteration", "games", "wins", "win_rate", "avg_game_len"],
                          index=["nilfgaardian", "monster", "northern", "scoiatael"])

        df["iteration"] = iteration

        for game in self.data_list:
            winner = game.get("result")
            factions = [game.get("p1_faction"), game.get("p2_faction")]
            df.loc[factions[0], "games"] += 1
            df.loc[factions[1], "games"] += 1
            game_len = len(game.get("score")) / 2 + game.get("player1").get("graveyard size") + game.get("player2").get(
                "graveyard size")
            df.loc[factions[0], "avg_game_len"] += game_len
            df.loc[factions[1], "avg_game_len"] += game_len
            if winner is not None:
                df.loc[factions[int(winner)], "wins"] += 1

        df["avg_game_len"] *= (1 / df["games"])
        df["win_rate"] = df["wins"] / df["games"]
        return df

    def get_faction_v_faction_stats(self, iteration):
        # parse game data and create dataframe showing faction vs faction performance.

        cols = ["iteration", "faction1", "faction2", "games", "wins", "win_rate", "avg_game_len"]
        df = pd.DataFrame(columns=cols)
        df = self.add_f_v_f_initial_rows(df, iteration)

        for game in self.data_list:
            f1 = game.get("p1_faction")
            f2 = game.get("p2_faction")
            factions = [f1, f2]
            result = game.get("result")
            df.loc[(df['faction1'] == f1) & (df['faction2'] == f2), "games"] += 1
            df.loc[(df['faction1'] == f2) & (df['faction2'] == f1), "games"] += 1
            if result is not None:
                df.loc[
                    (df['faction1'] == factions[result]) & (df['faction2'] == factions[(result + 1) % 2]), "wins"] += 1
            game_len = len(game.get("score")) / 2 + game.get("player1").get("graveyard size") + game.get("player2").get(
                "graveyard size")
            df.loc[(df['faction1'] == f1) & (df['faction2'] == f2), "avg_game_len"] += game_len
            df.loc[(df['faction1'] == f2) & (df['faction2'] == f1), "avg_game_len"] += game_len

        df['iteration'] = iteration
        df["avg_game_len"] *= (1 / df["games"])
        df["win_rate"] = df["wins"] / df["games"]

        return df

    def add_f_v_f_initial_rows(self, df, iteration):
        # create initial format for faction vs faction table.

        d1 = [iteration, "monster", 'nilfgaardian', 0, 0, 0, 0]
        d2 = [iteration, "monster", 'northern', 0, 0, 0, 0]
        d3 = [iteration, "monster", 'scoiatael', 0, 0, 0, 0]
        d4 = [iteration, "nilfgaardian", 'monster', 0, 0, 0, 0]
        d5 = [iteration, "nilfgaardian", 'northern', 0, 0, 0, 0]
        d6 = [iteration, "nilfgaardian", 'scoiatael', 0, 0, 0, 0]
        d7 = [iteration, "northern", 'monster', 0, 0, 0, 0]
        d8 = [iteration, "northern", 'nilfgaardian', 0, 0, 0, 0]
        d9 = [iteration, "northern", 'scoiatael', 0, 0, 0, 0]
        d10 = [iteration, "scoiatael", 'monster', 0, 0, 0, 0]
        d11 = [iteration, "scoiatael", 'nilfgaardian', 0, 0, 0, 0]
        d12 = [iteration, "scoiatael", 'northern', 0, 0, 0, 0]

        for dicto in [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12]:
            df.loc[len(df)] = dicto
        return df

    def get_game_duration_stats(self, iteration):
        # create a dataframe listing all game durations in a given iteration.
        df = pd.DataFrame(columns=["iteration", "faction", "game_duration"])

        for game in self.data_list:
            df = df.append(self.get_game_duration_info(iteration, game, 1), ignore_index=True)
            df = df.append(self.get_game_duration_info(iteration, game, 2), ignore_index=True)

        return df

    def get_game_duration_info(self, iteration, game, player_number):
        # given a game dictionary, return a dictionary of game length.

        faction = game.get("p" + str(player_number) + "_faction")
        game_len = len(game.get("score")) / 2 + game.get("player1").get("graveyard size") + game.get("player2").get(
            "graveyard size")
        return {"iteration": iteration, "faction": faction, "game_duration": game_len}

    def get_card_stats(self, iteration):
        # parse game data and create dataframe of summary card information.

        card_list = self.get_unique_card_list()
        df = pd.DataFrame(0,
                          index=card_list,
                          columns=["iteration", "games", "wins", "win_rate", "avg_game_len", "adjustment"])

        df["iteration"] = iteration

        for game in self.data_list:
            winner = game.get("result")
            players = [game.get("player1"), game.get("player2")]
            game_len = len(game.get("score")) / 2 + game.get("player1").get("graveyard size") + game.get("player2").get(
                "graveyard size")
            self.update_card_stats_for_player(df, players[0], game_len, 0 == winner)
            self.update_card_stats_for_player(df, players[1], game_len, 1 == winner)

        df["avg_game_len"] *= (1 / df["games"])
        df["win_rate"] = df["wins"] / df["games"]
        df["adjustment"] = np.where((df["win_rate"] >= 0.75), -2,
                                    np.where(((df["win_rate"] > 0.6) & (df["win_rate"] < 0.75)), -1,
                                             np.where(((df["win_rate"] > 0.25) & (df["win_rate"] < 0.4)), 1,
                                                      np.where((df["win_rate"] <= 0.25), 2, 0))))

        return df

    def update_card_stats_for_player(self, df, player_dict, score_length, winner):
        # for a given player, parse their card information and update the card stats dataframe.

        # need to run through both hand and graveyard
        hand = player_dict.get("hand")
        graveyard = player_dict.get("graveyard")

        self.parse_card_container(df, hand, score_length, winner)
        self.parse_card_container(df, graveyard, score_length, winner)

    def parse_card_container(self, df, container, score_length, winner):
        # parse hand or graveyard and update card stats dataframe.

        for card in container:
            df.loc[card, "games"] += 1
            df.loc[card, "avg_game_len"] += score_length
            if winner:
                df.loc[card, "wins"] += 1

    def get_unique_card_list(self):
        # return unique list of cards present in simulations.
        output = []

        for game in self.data_list:
            p1 = game.get("player1")
            p2 = game.get("player2")

            p1_hand = p1.get("hand")
            p1_graveyard = p1.get("graveyard")
            p2_hand = p2.get("hand")
            p2_graveyard = p2.get("graveyard")

            self.add_cards_to_list(output, p1_hand)
            self.add_cards_to_list(output, p1_graveyard)
            self.add_cards_to_list(output, p2_hand)
            self.add_cards_to_list(output, p2_graveyard)

        return output

    def add_cards_to_list(self, card_list, card_dict):
        # parse dictionary and add card to list if not present.

        for card in card_dict:
            if card not in card_list:
                card_list.append(card)

    def create_new_card_data_file(self, card_stats):
        # create new card data csv that can be used as final result or for future iterations.

        if not os.path.exists(self.destination):
            shutil.copyfile(self.card_file, self.destination)

        card_df = pd.read_csv(self.destination).set_index('card_id')
        card_df = pd.concat([card_df, card_stats], axis=1)
        card_df['adjustment'] = card_df['adjustment'].fillna(0).astype(int)
        card_df['power'] += card_df['adjustment']
        card_df.drop(["iteration", "games", "wins", "win_rate", "avg_game_len", "adjustment"], axis=1, inplace=True)

        card_df.to_csv(self.destination, index_label="card_id")
