import pandas as pd
import matplotlib.pyplot as plt
from draw_court import draw_court
from dist_plot import dist_plot
from shot_chart import shot_chart
from utils import get_team_info, format_dataframe

#graph settings
# player - the player to graph
# filter_by_position (default False) whether or not the distributions should use only players of the same position, or all players
# position_to_use (default None) the position the player should be treated as (if None, just use default position from data)
# teams_df - dataframe of team info
# cols - statistics to graph
# pct_cols - the statistics that should be rendered as percentages
# shot_df - the shot tracking df to plot

def graph_player_with_shot_chart(stats_df, player_name, teams_df, cols, pct_cols, shot_df, filter_by_position = False, position_to_use = None):
  team_info = get_team_info(stats_df=stats_df, teams_df=teams_df, player_name=player_name)
  df_to_graph, player_stats_df, sub_title = format_dataframe(
    stats_df=stats_df,
    player_name=player_name,
    cols=cols,
    filter_by_position=filter_by_position,
    position_to_use=position_to_use
  )
  fig = plt.figure(figsize=(40,len(cols)*4), constrained_layout=True)
  gs = fig.add_gridspec(len(cols), 6)
  chart_title = player_name
  fig.suptitle(
      chart_title,
      fontsize=80,
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
      fontsize=40,
      style='italic'
  )
  fig.text(
      x=0,
      y=1.02,
      s=f'{team_info["Full"]}, 2019-20',
      horizontalalignment='left',
      verticalalignment='top',
      fontsize=40,
      style='italic'
  )
  ax1 = fig.add_subplot(gs[:,:5])
  ax1 = draw_court(ax=ax1, outer_lines=False)
  player_shot_df = shot_df[shot_df['PLAYER_NAME'] == player_name]
  shot_chart(shot_df=player_shot_df, ax=ax1)
  for index, col in enumerate(cols):
    ax = fig.add_subplot(gs[index,5])
    is_pct_col = col in pct_cols
    dist_plot(
        totals=df_to_graph,
        stats_to_graph=player_stats_df,
        col=col,
        team=team_info,
        ax=ax,
        is_pct_col=is_pct_col,
        show_colors=False,
        fontsize=32
    )
  plt.savefig(f'output/{player_name} 2019-20 Shot Chart.png', bbox_inches='tight', pad_inches=2)
  plt.close()

#graph settings
# player_name - the player to graph
# filter_by_position (default False) whether or not the distributions should use only players of the same position, or all players
# position_to_use (default None) the position the player should be treated as (if None, just use default position from data)
# teams_df - dataframe of team info
# cols - statistics to graph
# pct_cols - the statistics that should be rendered as percentages

def graph_player_distributions(stats_df, player_name, teams_df, cols, pct_cols, filter_by_position = False, position_to_use = None):
  team_info = get_team_info(stats_df=stats_df, teams_df=teams_df, player_name=player_name)
  df_to_graph, player_stats_df, sub_title = format_dataframe(
    stats_df=stats_df,
    player_name=player_name,
    cols=cols,
    filter_by_position=filter_by_position,
    position_to_use=position_to_use
  )
  fig = plt.figure(figsize=(8,len(cols)*4), constrained_layout=True)
  gs = fig.add_gridspec(len(cols), 1)
  chart_title = player_name
  fig.suptitle(
      chart_title,
      fontsize=30,
      fontweight='bold',
      y=1.02,
      x=-.05,
      horizontalalignment='left',
      verticalalignment='bottom'
  )
  fig.text(
      x=1.05,
      y=1.02,
      s=sub_title,
      horizontalalignment='right',
      verticalalignment='top',
      fontsize=24,
      style='italic'
  )
  fig.text(
      x=-.05,
      y=1.02,
      s=f'{team_info["Full"]}, 2019-20',
      horizontalalignment='left',
      verticalalignment='top',
      fontsize=24,
      style='italic'
  )
  for index, col in enumerate(cols):
    ax = fig.add_subplot(gs[index,0])
    is_pct_col = col in pct_cols
    dist_plot(
        totals=df_to_graph,
        stats_to_graph=player_stats_df,
        col=col,
        team=team_info,
        ax=ax,
        is_pct_col=is_pct_col
    )
  plt.savefig(f'output/{player_name} 2019-20 Shooting Distribution.png', bbox_inches='tight', pad_inches=2)
  plt.close()