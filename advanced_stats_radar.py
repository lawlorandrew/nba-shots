import matplotlib.pyplot as plt
from radar_plot import radar_plot
from utils import get_team_info


def plot_advanced_stats_radar(player_name, totals_df, advanced_stats_df, team_colors_df, fig):
    fouls_df = totals_df[['Name', 'PF']]
    merged_df = advanced_stats_df.merge(fouls_df, on='Name')
    merged_df.rename(columns={'PF': 'PF/100'}, inplace=True)
    stats_to_graph = merged_df[merged_df['Name'] == player_name].squeeze()
    team_info = get_team_info(
        stats_df=totals_df, teams_df=team_colors_df, player_name=player_name)
    radar_plot(
        totals_df=merged_df,
        stats_to_graph=stats_to_graph,
        player_name=player_name,
        team_info=team_info,
        cols=[
            'BLK%',
            'TRB%',
            'AST%',
            'USG%',
            'TOV%',
            '3PAr',
            'TS%',
            'FTr',
            'PF/100',
            'STL%',
        ],
        pct_cols=[
            'TS%',
            '3PAr',
            'FTr',
        ],
        inverse_cols=[
            'TOV%',
            'PF/100',
        ],
        fig=fig,
    )
    fig.suptitle(
        player_name,
        fontsize=20,
        fontweight='bold',
        y=.92,
        x=.02,
        horizontalalignment='left',
        verticalalignment='bottom'
    )
    fig.text(
        x=.02,
        y=.92,
        s=f'{team_info["Full"]}, 2019-20',
        horizontalalignment='left',
        verticalalignment='top',
        fontsize=12,
        style='italic'
    )
    fig.text(
        x=.02,
        y=.05,
        s='Data from Basketball Reference',
        horizontalalignment='left',
        verticalalignment='top',
        fontsize=8,
        style='italic'
    )
    plt.savefig(f'output/{player_name} Advanced Radar 2019-20.png')
