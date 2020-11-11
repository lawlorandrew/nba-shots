import matplotlib.pyplot as plt
from radar_plot import radar_plot
from utils import get_team_info
import pandas as pd

def plot_advanced_stats_radar(player_name, team, season, totals_df, advanced_stats_df, team_colors_df, fig):
    fouls_df = totals_df[['Name_Raw', 'team_id', 'season', 'pf_per_poss', 'fg3_pct', 'fg2_pct', 'ft_pct']]
    # fouls_df = totals_df[['Name_Raw', 'PF', '3P%']]
    merged_df = advanced_stats_df.merge(
      fouls_df, on=['Name_Raw', 'team_id', 'season'])
    merged_df.rename(columns={
        'pf_per_poss': 'PF/100',
        'ast_pct': 'AST%',
        'blk_pct': 'BLK%',
        'trb_pct': 'TRB%',
        'orb_pct': 'ORB%',
        'drb_pct': 'DRB%',
        'usg_pct': 'USG%',
        'tov_pct': 'TOV%',
        'fg3a_per_fga_pct': '3PAr',
        'ts_pct': 'TS%',
        'fta_per_fga_pct': 'FTr',
        'stl_pct': 'STL%',
        'fg3_pct': '3P%',
        'fg2_pct': '2P%',
        'ft_pct': 'FT%'
    }, inplace=True)
    merged_df.rename(columns={
        'PF': 'PF/100',
    }, inplace=True)
    # POSITIONAL FILTER
    print(merged_df['pos'].unique())
    merged_df = merged_df[merged_df['pos'].isin(['PG', 'SG', 'PG-SG', 'SG-PG'])]
    stats_to_graph = merged_df[
        (merged_df['Name'] == player_name) &
        (merged_df['team_id'] == team) &
        (merged_df['season'] == season)
    ].squeeze()
    # stats_to_graph = merged_df[
    #     (merged_df['Name_Raw'] == player_name)
    # ].squeeze()
    merged_df = merged_df.drop_duplicates(
        subset=['player', 'season'], keep='first')
    team_info = get_team_info(
        stats_df=totals_df, teams_df=team_colors_df, team=team)
    radar_plot(
        totals_df=merged_df,
        stats_to_graph=stats_to_graph,
        player_name=player_name,
        team_info=team_info,
        season=season,
        cols=[
            'BLK%',
            'DRB%',
            'ORB%',
            'AST%',
            'USG%',
            'TOV%',
            '3PAr',
            '3P%',
            '2P%',
            'FT%',
            'FTr',
            'PF/100',
            'STL%',
        ],
        pct_cols=[
            'TS%',
            '3PAr',
            'FTr',
            '3P%',
            '2P%',
            'FT%',
        ],
        inverse_cols=[
            'TOV%',
            'PF/100',
        ],
        fig=fig,
    )
    # fig.suptitle(
    #     player_name,
    #     fontsize=20,
    #     fontweight='bold',
    #     y=.92,
    #     x=.02,
    #     horizontalalignment='left',
    #     verticalalignment='bottom'
    # )
    # fig.text(
    #     x=.02,
    #     y=.92,
    #     s=f'{team_info["Full"]}, {season} Playoffs',
    #     horizontalalignment='left',
    #     verticalalignment='top',
    #     fontsize=12,
    #     style='italic'
    # )
    # fig.text(
    #     x=.02,
    #     y=.03,
    #     s='By Andrew Lawlor, Twitter: @lawlorpalooza',
    #     horizontalalignment='left',
    #     verticalalignment='top',
    #     fontsize=8,
    #     style='italic'
    # )
    # fig.text(
    #     x=.02,
    #     y=.06,
    #     s='Data from Basketball Reference',
    #     horizontalalignment='left',
    #     verticalalignment='top',
    #     fontsize=8,
    #     style='italic'
    # )
    plt.savefig(
        f'output/player-radars/{player_name} {team} Advanced Radar {season}.png')
    plt.close('all')
