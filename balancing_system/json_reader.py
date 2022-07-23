import json


class JsonReader:

    def __init__(self, json_file):
        with open(json_file) as f:
            self.data_list = json.load(f)

    def get_faction_stats(self):
        # parse file and get the number of wins for each faction, use to derive win rate for each faction
        # NEED BOTH PARTICIPATING FACTIONS
        pass

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
