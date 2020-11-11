import matplotlib.pyplot as plt
import pandas as pd
import math
from radar_plot import radar_plot
from shot_chart import shot_chart
from utils import get_team_info, format_dataframe
from draw_court import draw_court
from dist_plot import dist_plot

def plot_player_profile(player_name, team, season):
  stats_df = pd.read_csv('./data/nba_per_poss.csv')
  teams_df = pd.read_csv('./data/nba_team_colors.csv')
  advanced_stats_df = pd.read_csv('./data/nba_advanced.csv')
  radar_df = advanced_stats_df[['player', 'team_id', 'season', 'mp', 'per', 'obpm', 'dbpm', 'ast_pct', 'fg3a_per_fga_pct', 'ts_pct', 'fta_per_fga_pct', 'trb_pct', 'blk_pct', 'stl_pct', 'tov_pct', 'usg_pct']]
  dists_df = stats_df[['player', 'team_id', 'season', 'fga_per_poss', 'fg2a_per_poss', 'fg3a_per_poss', 'fta_per_poss', 'fg2_pct', 'fg3_pct', 'ft_pct', 'pf_per_poss']]
  shot_df = pd.read_csv('./data/all_shots.csv')

  merged_df = radar_df.merge(dists_df, on=['player','team_id','season'])
  merged_df.rename(columns={'pf_per_poss': 'PF/100', 'fga_per_poss': 'FGA/100', 'fta_per_poss': 'FTA/100', 'fg3a_per_poss': '3PA/100', 'fg2a_per_poss': '2PA/100' }, inplace=True)

  cols = [
    'mp',
    'per',
    'obpm',
    'dbpm',
    'ast_pct',
    'fg3a_per_fga_pct',
    'ts_pct',
    'fta_per_fga_pct',
    'trb_pct',
    'blk_pct',
    'stl_pct',
    'tov_pct',
    'usg_pct',
    '3PA/100',
    '2PA/100',
    'FTA/100',
    'fg2_pct',
    'fg3_pct',
    'ft_pct',
    'PF/100',
  ]
  pct_cols = [
    'fg2_pct',
    'fg3_pct',
    'ft_pct',
    'fg3a_per_fga_pct',
    'ts_pct',
    'fta_per_fga_pct',
  ]

  team_info = get_team_info(stats_df=stats_df, teams_df=teams_df, team=team)
  df_to_graph, player_stats_df, sub_title = format_dataframe(
    stats_df=merged_df,
    player_name=player_name,
    team=team,
    season=season,
    cols=cols,
  )
  N = len(cols) + 1
  fig = plt.figure(figsize=(50,N*2), constrained_layout=True)
  gs = fig.add_gridspec(N, 6)
  chart_title = player_name
  fig.suptitle(
      chart_title,
      fontsize=120,
      fontweight='bold',
      y=1.02,
      x=0,
      horizontalalignment='left',
      verticalalignment='bottom'
  )
  fig.text(
      x=1,
      y=1.02,
      s=sub_title,
      horizontalalignment='right',
      verticalalignment='top',
      fontsize=60,
      style='italic'
  )
  fig.text(
      x=0,
      y=1.02,
      s=f'{team_info["Full"]}, 2019-20',
      horizontalalignment='left',
      verticalalignment='top',
      fontsize=60,
      style='italic'
  )
  ax1 = fig.add_subplot(gs[9:,:5])
  ax1 = draw_court(ax=ax1, outer_lines=False)
  player_shot_df = shot_df[shot_df['PLAYER_NAME'] == player_name]
  shot_chart(shot_df=player_shot_df, ax=ax1, ylim=(-47.5, 300))
  player_stats = merged_df[
    (merged_df['player'] == player_name) &
    (merged_df['season'] == season) &
    (merged_df['team_id'] == team)
  ].squeeze()
  radar_plot(
    totals_df=merged_df,
    stats_to_graph=player_stats,
    player_name=player_name,
    team_info=team_info,
    season=2020,
    cols=[
      'fta_per_fga_pct',
      'ts_pct',
      'fg3a_per_fga_pct',
      'ast_pct',
      'usg_pct',
      'tov_pct',
      'PF/100',
      'stl_pct',
      'blk_pct',
      'trb_pct',
    ],
    pct_cols=[
      'ts_pct',
      'fg3a_per_fga_pct',
      'fta_per_fga_pct',
    ],
    inverse_cols=[
      'tov_pct',
      'PF/100',
    ],
    fig=fig,
    gs=gs[1:9, :5],
    label_font_size=48,
    tick_font_size=32,
    label_padding=60,
  )
  for index, col in enumerate(cols):
    ax = fig.add_subplot(gs[index + 1,5])
    is_pct_col = col in pct_cols
    dist_plot(
        totals=df_to_graph,
        stats_to_graph=player_stats_df,
        col=col,
        team=team_info,
        ax=ax,
        is_pct_col=is_pct_col
    )
  plt.savefig(f'output/{player_name} 2019-20 Profile.png', bbox_inches='tight', pad_inches=2)

plot_player_profile('Giannis Antetokounmpo', 'MIL', 2020)
