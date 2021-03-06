import matplotlib.pyplot as plt
from radar_plot import radar_plot
from utils import get_team_info

def plot_per_poss_radar(player_name, team, season, totals_df, team_colors_df, fig, gs=111):
  stats_to_graph = totals_df[totals_df['Name'] == player_name].squeeze()
  team_info = get_team_info(stats_df = totals_df, teams_df=team_colors_df, team=team)
  radar_plot(
    totals_df=totals_df,
    player_name=player_name,
    stats_to_graph=stats_to_graph,
    team_info=team_info,
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