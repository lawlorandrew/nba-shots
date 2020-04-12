import matplotlib.pyplot as plt
from radar_plot import radar_plot

def plot_per_poss_radar(player_name, totals_df, team_colors_df, fig, gs=111):
  radar_plot(
    totals_df=totals_df,
    player_name=player_name,
    teams_df=team_colors_df,
    cols=[
      '3PA',
      '3P%',
      'FTA',
      'FT%',
      '2PA',
      '2P%',
      'TRB',
      'BLK',
      'PF',
      'STL',
      'TOV',
      'AST',
    ],
    pct_cols=['2P%', '3P%', 'FT%'],
    inverse_cols=['TOV', 'PF'],
    fig=fig,
    gs=gs,
  )
  plt.savefig(f'output/{player_name} Per Poss Radar 2019-20.png')