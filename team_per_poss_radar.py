import matplotlib.pyplot as plt
from radar_plot import radar_plot

def plot_team_per_poss_radar(team_name, totals_df, team_colors_df, fig):
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
  ]
  for col in cols:
    totals_df[f'{col}_pct'] = totals_df[col].rank(pct=True)
  team_stats = totals_df.loc[totals_df['Team'] == team_name].squeeze()
  team_info = team_colors_df.loc[team_colors_df['Full'] == team_name].squeeze()  # team colors to use
  radar_plot(
    totals_df=totals_df,
    stats_to_graph=team_stats,
    player_name=team_name,
    team_info=team_info,
    cols=cols,
    pct_cols=['2P%', '3P%', 'FT%'],
    inverse_cols=['TOV', 'PF'],
    fig=fig,
  )
  fig.suptitle(
      team_name,
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
      s='2019-20 Team Radar',
      horizontalalignment='left',
      verticalalignment='top',
      fontsize=12,
      style='italic'
  )
  plt.savefig(f'output/{team_name} Per Poss Radar 2019-20.png')