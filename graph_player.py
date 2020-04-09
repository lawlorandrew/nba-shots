import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from draw_court import draw_court

#graph settings
# player - the player to graph
# filter_by_position (default False) whether or not the distributions should use only players of the same position, or all players
# position_to_use (default None) the position the player should be treated as (if None, just use default position from data)
# team - team info to use
# cols - statistics to graph
# pct_cols - the statistics that should be rendered as percentages
# shot_df - the shot tracking df to plot

def graph_player(stats_df, player, team, cols, pct_cols, shot_df, filter_by_position = False, position_to_use = None):
  totals_df_copy = pd.DataFrame(stats_df)
  if (position_to_use is not None):
    totals_df_copy.loc[totals_df_copy['Name'] == player, ['Pos']] = position_to_use
  if (filter_by_position is True):
    position = totals_df_copy.loc[totals_df_copy['Name']==player, ['Pos']].squeeze()
    df_to_graph = totals_df_copy.loc[totals_df_copy['Pos'] == position]
    sub_title = 'Compared with ' + position + 's'
  else:
    df_to_graph = pd.DataFrame(totals_df_copy)
    sub_title = 'Compared with all players'
  for col in cols:
    df_to_graph[f'{col}_pct'] = df_to_graph[col].rank(pct=True)
  playerStats = df_to_graph.loc[df_to_graph['Name']==player].squeeze()
  # fig, axs = plt.subplots(len(cols), 1, figsize=(8,len(cols)*4))
  fig = plt.figure(figsize=(30,len(cols)*3), constrained_layout=True)
  gs = fig.add_gridspec(len(cols), 6)
  chart_title = player
  fig.suptitle(
      chart_title,
      fontsize=30,
      fontweight='bold',
      y=1,
      x=0,
      horizontalalignment='left',
      verticalalignment='bottom'
  )
  fig.text(
      1,
      1,
      sub_title,
      horizontalalignment='right',
      verticalalignment='bottom',
      fontsize=16,
      style='italic'
  )
  fig.text(
      0,
      1,
      team['Full'],
      horizontalalignment='left',
      verticalalignment='top',
      fontsize=16,
      style='italic'
  )
  ax1 = fig.add_subplot(gs[:,:5])
  ax1 = draw_court(ax=ax1, outer_lines=True)
  ax1.set_xlim(250,-250)
  ax1.set_ylim(-50,430)
  ax1.axis('off')
  made_shots = shot_df[shot_df['EVENT_TYPE'] == 'Made Shot']
  missed_shots = shot_df[shot_df['EVENT_TYPE'] == 'Missed Shot']
  ax1.scatter(made_shots.LOC_X, made_shots.LOC_Y, c='#000080', label='Makes', s=50, zorder=15)
  ax1.scatter(missed_shots.LOC_X, missed_shots.LOC_Y, c='#DC143C', label='Misses', s=50, zorder=10)
  ax1.legend(loc='upper left', bbox_to_anchor=(0.02,0.98), fontsize=20)
  for index, col in enumerate(cols):
    ax = fig.add_subplot(gs[index,5])
    sns.distplot(
      df_to_graph[col],
      ax=ax,
      hist=False,
      kde_kws={"shade": True},
      color=team['Primary'],
    )
    ax.axvline(playerStats[col], color=team['Secondary'])
    sns.despine(left=True)
    ax.set_xlabel('')
    ax.yaxis.set_visible(False)
    if (col in pct_cols):
      value = '{:.1%}'.format(playerStats[col])
    else:
      value = '{:.1f}'.format(playerStats[col])
    percentile = playerStats[f'{col}_pct']
    percentile_text = 'P: ' + '{:.0f}'.format(playerStats[f'{col}_pct']*100)
    value_text = value + '\n' + percentile_text
    if (percentile > .8):
      text_color = 'g'
    elif (percentile > .4):
      text_color = 'y'
    else:
      text_color = 'r'
    ax.text(
        1.1,
        0.5,
        value_text,
        transform=ax.transAxes,
        horizontalalignment='right',
        verticalalignment='center',
        fontsize=16,
        color=text_color
    )
    ax.text(
        -.1,
        0.5,
        col,
        transform=ax.transAxes,
        horizontalalignment='left',
        verticalalignment='center',
        fontsize=16,
    )
  plt.savefig(f'output/{player} 2019-20 Shooting.png', bbox_inches='tight', pad_inches=2)
