import json
import os
import shutil
import pandas as pd
import numpy as np


class JsonReader:

    def __init__(self, json_file, card_file, destination):
        with open(json_file) as f:
            self.data_list = json.load(f)
        self.card_file = card_file
        self.destination = destination

    def run_balance(self, iteration, faction_path, card_path):
        faction_stats = self.get_faction_overview_stats(iteration)
        card_stats = self.get_card_stats(iteration)

        faction_stats.to_csv(faction_path, mode='a', header=not os.path.exists(faction_path), index_label="faction")
        card_stats.to_csv(card_path, mode='a', header=not os.path.exists(card_path), index_label="card_id")

        self.create_new_card_data_file(card_stats)

    def get_faction_overview_stats(self, iteration):
        df = pd.DataFrame(0,
                          columns=["iteration", "games", "wins", "win_rate", "avg_game_len"],
                          index=["nilfgaardian", "monster", "northern", "scoiatael"])

        df["iteration"] = iteration

        for game in self.data_list:
            winner = game.get("result")
            factions = [game.get("p1_faction"), game.get("p2_faction")]
            df.loc[factions[0], "games"] += 1
            df.loc[factions[1], "games"] += 1
            df.loc[factions[0], "avg_game_len"] += len(game.get("score")) / 2 + game.get("player1").get(
                "graveyard size")
            df.loc[factions[1], "avg_game_len"] += len(game.get("score")) / 2 + game.get("player2").get(
                "graveyard size")
            if winner is not None:
                df.loc[factions[int(winner)], "wins"] += 1

        df["avg_game_len"] *= (1 / df["games"])
        df["win_rate"] = df["wins"] / df["games"]
        return df

    def get_faction_v_faction_stats(self, iteration):
        # TODO implement
        # create df for fact v fact, normal index,
        # each row shows ["faction1", "faction2", "games", "wins", "win_rate", "avg_game_len"]
        # add rows with empty stats
        # loop through json, update df based on each game
        # calc win rate and return df
        pass

    def get_card_stats(self, iteration):
        card_list = self.get_unique_card_list()
        df = pd.DataFrame(0,
                          index=card_list,
                          columns=["iteration", "games", "wins", "win_rate", "avg_game_len", "adjustment"])

        df["iteration"] = iteration

        for game in self.data_list:
            winner = game.get("result")
            players = [game.get("player1"), game.get("player2")]
            self.update_card_stats_for_player(df, players[0], len(game.get('score')), 0 == winner)
            self.update_card_stats_for_player(df, players[1], len(game.get('score')), 1 == winner)

        df["avg_game_len"] *= (1 / df["games"])
        df["win_rate"] = df["wins"] / df["games"]
        df["adjustment"] = np.where((df["win_rate"] >= 0.75), -2,
                                    np.where(((df["win_rate"] > 0.6) & (df["win_rate"] < 0.75)), -1,
                                    np.where(((df["win_rate"] > 0.25) & (df["win_rate"] < 0.4)), 1,
                                    np.where((df["win_rate"] <= 0.25), 2, 0))))

        return df

    def update_card_stats_for_player(self, df, player_dict, score_length, winner):
        # need to run through both hand and graveyard
        hand = player_dict.get("hand")
        graveyard = player_dict.get("graveyard")
        score_length = score_length / 2 + player_dict.get("hand size") + player_dict.get("graveyard size")

        self.parse_card_container(df, hand, score_length, winner)
        self.parse_card_container(df, graveyard, score_length, winner)

    def parse_card_container(self, df, container, score_length, winner):
        for card in container:
            df.loc[card, "games"] += 1
            df.loc[card, "avg_game_len"] += score_length
            if winner:
                df.loc[card, "wins"] += 1

    def get_unique_card_list(self):
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
        for card in card_dict:
            if card not in card_list:
                card_list.append(card)

    def create_new_card_data_file(self, card_stats):
        if not os.path.exists(self.destination):
            shutil.copyfile(self.card_file, self.destination)

        card_df = pd.read_csv(self.destination).set_index('card_id')
        card_df = pd.concat([card_df, card_stats], axis=1)
        card_df['power'] += card_df['adjustment']
        card_df.drop(["iteration", "games", "wins", "win_rate", "avg_game_len", "adjustment"], axis=1, inplace=True)

        card_df.to_csv(self.destination, index_label="card_id")
