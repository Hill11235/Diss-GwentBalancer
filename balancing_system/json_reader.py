import json
import pandas as pd


class JsonReader:

    def __init__(self, json_file):
        with open(json_file) as f:
            self.data_list = json.load(f)

    def get_faction_stats(self, iteration):
        factions_df = pd.DataFrame(0,
                                   columns=["iteration", "games", "wins", "win_rate"],
                                   index=["nilfgaardian", "monster", "northern", "scoiatael"])

        factions_df["iteration"] = iteration

        for game in self.data_list:
            winner = game.get("result")
            factions = [game.get("p1_faction"), game.get("p2_faction")]
            factions_df.loc[factions[0], "games"] += 1
            factions_df.loc[factions[1], "games"] += 1
            if winner is not None:
                factions_df.loc[factions[int(winner)], "wins"] += 1

        factions_df["win_rate"] = factions_df["wins"] / factions_df["games"]
        return factions_df

    def get_card_stats(self):
        # parse and create dataframe for each card id, count games and wins for each. Calc win rate
        # use win rates for each card to determine buff/nerf amount (use some kind of banding??)
        pass

    def create_new_card_data_file(self):
        # copy input file for sims and rename based on iteration, adjust cards based on buff, and save
        pass

    def create_iter_visualisations(self):
        # create visualisations based on faction and card stats
        # write iteration stats to csv file
        pass
