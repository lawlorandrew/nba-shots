import matplotlib.pyplot as plt
import pandas as pd
import math
from radar_plot import radar_plot
from shot_chart import shot_chart
from utils import get_team_info, format_dataframe
from draw_court import draw_court
from dist_plot import dist_plot

def plot_player_profile(player_name):
  stats_df = pd.read_csv('./data/nba_per_poss.csv')
  stats_df['Name'] = stats_df['Player'].str.split('\\').str[0]
  teams_df = pd.read_csv('./data/nba_team_colors.csv')
  advanced_stats_df = pd.read_csv('./data/nba_advanced.csv')
  advanced_stats_df['Name'] = advanced_stats_df['Player'].str.split('\\').str[0]
  radar_df = advanced_stats_df[['Name', 'Tm', 'MP', 'PER', 'OBPM', 'DBPM', 'AST%', '3PAr', 'TS%', 'FTr', 'TRB%', 'BLK%', 'STL%', 'TOV%', 'USG%']]
  dists_df = stats_df[['Name', 'FGA', '3PA', '2PA', 'FTA', '2P%', '3P%', 'FT%', 'PF']]
  shot_df = pd.read_csv('./data/all_shots.csv')

  merged_df = radar_df.merge(dists_df, on='Name')
  merged_df.rename(columns={'PF': 'PF/100', 'FGA': 'FGA/100', 'FTA': 'FTA/100', '3PA': '3PA/100', '2PA': '2PA/100' }, inplace=True)

  cols = [
    'MP',
    'PER',
    'OBPM',
    'DBPM',
    'AST%',
    '3PAr',
    'TS%',
    'FTr',
    'TRB%',
    'BLK%',
    'STL%',
    'TOV%',
    'USG%',
    '3PA/100',
    '2PA/100',
    'FTA/100',
    '2P%',
    '3P%',
    'FT%',
    'PF/100',
  ]
  pct_cols = [
    '2P%',
    '3P%',
    'FT%',
    '3PAr',
    'TS%',
    'FTr',
  ]

  team_info = get_team_info(stats_df=stats_df, teams_df=teams_df, player_name=player_name)
  df_to_graph, player_stats_df, sub_title = format_dataframe(
    stats_df=merged_df,
    player_name=player_name,
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
  player_stats = merged_df[merged_df['Name'] == player_name].squeeze()
  radar_plot(
    totals_df=merged_df,
    stats_to_graph=player_stats,
    player_name=player_name,
    team_info=team_info,
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

plot_player_profile('Giannis Antetokounmpo')
