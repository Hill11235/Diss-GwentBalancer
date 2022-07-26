import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# TODO parse card and faction stats and create and save different graphs
class GraphicCreation:

    def __init__(self, iteration):
        self.iteration = iteration

    def create_matrix(self):
        # create faction v faction win rate and game length matrix
        # TODO need to extract faction v faction performance into a csv
        pass

    def create_line_charts(self):
        # create line charts for each faction showing win rate and avg duration with each iteration
        factions = pd.read_csv("./stats/faction_stats.csv")
        print(factions)

        for faction_name in ["monster", "nilfgaardian", "scoiatael", "northern"]:
            self.plot_faction(factions, faction_name)

        self.plot_faction(factions, None)

    def plot_faction(self, df, faction):
        sns.set_style(style="white")
        if faction is None:
            data = df
            title = "Win rate with each iteration - all factions"
            save_path = "visualisations/all_factions_win_rate_plot.png"
        else:
            data = df[df["faction"] == faction]
            print(data)
            title = "Win rate with each iteration - " + faction + " faction"
            save_path = "visualisations/" + faction + "_win_rate_plot.png"

        faction_plot = sns.lineplot(x=df['iteration'],
                                    y=df['win_rate'],
                                    data=data,
                                    hue='faction',
                                    ci=None)
        faction_plot.set(xticks=range(min(df['iteration']), max(df['iteration']) + 1),
                         title=title)
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
        plt.savefig(save_path, bbox_inches='tight')
        plt.clf()

    def create_box_charts(self):
        # need to loop over output file and get all game durations
        pass

    def get_extreme_card_summary(self):
        # show top and bottom five card summaries based on normal statistics
        pass
