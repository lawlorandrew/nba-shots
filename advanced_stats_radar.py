import matplotlib.pyplot as plt
from radar_plot import radar_plot

def plot_advanced_stats_radar(player_name, totals_df, advanced_stats_df, team_colors_df, fig, gs = 111):
  fouls_df = totals_df[['Name', 'PF']]
  merged_df = advanced_stats_df.merge(fouls_df, on='Name')
  merged_df.rename(columns={'PF': 'PF/100'}, inplace=True)
  radar_plot(
    totals_df=merged_df,
    player_name=player_name,
    teams_df=team_colors_df,
    cols=[
      'FTr',
      'TS%',
      '3PAr',
      'AST%',
      'USG%',
      'TOV%',
      'PF/100',
      'STL%',
      'BLK%',
      'TRB%',
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
    gs=gs
  )
  plt.savefig(f'output/{player_name} Advanced Radar 2019-20.png')
