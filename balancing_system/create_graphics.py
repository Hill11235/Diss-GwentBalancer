import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class GraphicCreation:

    def create_matrix(self, metric, iteration=None):
        # TODO test when there are multiple iterations in the file
        df = pd.read_csv("./stats/faction_v_faction.csv", index_col=0)
        output_path = "visualisations/matrix_" + metric + ".png"
        if iteration is not None:
            df = df[df['iteration'] == iteration]
            output_path = "visualisations/matrix_" + metric + "_iteration_" + str(iteration) + ".png"

        data = df.pivot_table(index='faction1', columns='faction2', values=metric)

        matrix = sns.heatmap(data, cmap="YlGnBu", annot=True)
        matrix.set(title="Faction vs faction - " + metric)
        matrix.set_ylabel("Winning faction")
        matrix.set_xlabel("Losing faction")
        plt.savefig(output_path)
        plt.clf()

    def create_line_charts(self, metric):
        # create line charts for each faction showing win rate and avg duration with each iteration
        factions = pd.read_csv("./stats/faction_stats.csv")

        for faction_name in ["monster", "nilfgaardian", "scoiatael", "northern"]:
            self.plot_faction(factions, faction_name, metric)

        self.plot_faction(factions, None, metric)

    def plot_faction(self, df, faction, metric):
        sns.set_style(style="white")
        if faction is None:
            data = df
            title = "Win rate with each iteration - all factions"
            save_path = "visualisations/all_factions_win_rate_plot.png"
        else:
            data = df[df["faction"] == faction]
            title = "Win rate with each iteration - " + faction + " faction"
            save_path = "visualisations/" + faction + "_win_rate_plot.png"

        faction_plot = sns.lineplot(x=df['iteration'],
                                    y=df[metric],
                                    data=data,
                                    hue='faction',
                                    ci=None)
        faction_plot.set(xticks=range(min(df['iteration']), max(df['iteration']) + 1),
                         title=title)
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
        plt.savefig(save_path, bbox_inches='tight')
        plt.clf()

    def create_box_charts(self, iteration=None):
        # TODO test when there are multiple iterations in the file
        df = pd.read_csv("./stats/game_duration_data.csv", index_col=0)
        save_path = "visualisations/game_duration_box_plots.png"
        title = "Game duration box plots by faction"
        if iteration is not None:
            df = df[df['iteration'] == iteration]
            save_path = "visualisations/game_duration_box_plots_iteration" + str(iteration) + ".png"
            title += " - iteration " + str(iteration)
        box_plot = sns.boxplot(y=df['game_duration'], x=df['faction'])
        box_plot.set(title=title)
        plt.savefig(save_path, bbox_inches='tight')
        plt.clf()

    def get_extreme_card_summary(self, metric, iteration=None):
        df = pd.read_csv("./stats/card_stats.csv", index_col=0)
        save_path = "visualisations/extreme_card_summary"
        if iteration is not None:
            df = df[df['iteration'] == iteration]
            save_path = "visualisations/extreme_card_summary_iteration" + str(iteration)

        df_high = df.nlargest(10, metric)
        df_low = df.nsmallest(10, metric)
        self.save_card_summary_as_table(df_high, "high", save_path)
        self.save_card_summary_as_table(df_low, "low", save_path)

    def save_card_summary_as_table(self, df, end, save_path):
        df = self.format_df_for_table(df)
        save_path = save_path + "_" + end + ".png"
        fig, ax = plt.subplots()
        fig.patch.set_visible(False)
        ax.axis('off')
        ax.axis('tight')
        ax.table(cellText=df.values, colLabels=df.columns, loc='center')
        plt.savefig(save_path, bbox_inches='tight', dpi=400)
        plt.clf()

    def format_df_for_table(self, df):
        df['card_id'] = df.index
        cols = list(df)
        cols.insert(0, cols.pop(cols.index('card_id')))
        df = df.loc[:, cols]
        df['win_rate'] = df['win_rate'].round(decimals=2)
        df['avg_game_len'] = df['avg_game_len'].round(decimals=2)

        return df
