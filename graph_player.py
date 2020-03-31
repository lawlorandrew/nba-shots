import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#graph settings
# player - the player to graph
# filter_by_position (default False) whether or not the distributions should use only players of the same position, or all players
# position_to_use (default None) the position the player should be treated as (if None, just use default position from data)
# team - team info to use
# cols - statistics to graph
# pct_cols - the statistics that should be rendered as percentages

def graph_player(stats_df, player, team, cols, pct_cols, filter_by_position = False, position_to_use = None):
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
  fig, axs = plt.subplots(len(cols), 1, figsize=(8,len(cols)*4))
  sns.despine(left=True)
  chart_title = player
  fig.suptitle(
      chart_title,
      fontsize=30,
      fontweight='bold',
      y=.9,
      x=0,
      horizontalalignment='left',
      verticalalignment='bottom'
  )
  fig.text(
      1,
      .9,
      sub_title,
      horizontalalignment='right',
      verticalalignment='top',
      fontsize=16,
      style='italic'
  )
  fig.text(
      0,
      .9,
      team['Full'],
      horizontalalignment='left',
      verticalalignment='top',
      fontsize=16,
      style='italic'
  )
  for index, col in enumerate(cols):
    sns.distplot(
      df_to_graph[col],
      ax=axs[index],
      hist=False,
      kde_kws={"shade": True},
      color=team['Primary'],
    )
    axs[index].axvline(playerStats[col], color=team['Secondary'])
    axs[index].yaxis.set_visible(False)
    axs[index].set_xlabel('')
    if (col in pct_cols):
      value = '{:.1%}'.format(playerStats[col])
    else:
      value = '{:.1f}'.format(playerStats[col])
    percentile = playerStats[f'{col}_pct']
    percentile_text = 'Percentile: ' + '{:.0%}'.format(playerStats[f'{col}_pct'])
    value_text = value + '\n' + percentile_text
    if (percentile > .8):
      text_color = 'g'
    elif (percentile > .4):
      text_color = 'y'
    else:
      text_color = 'r'
    axs[index].text(
        1.1,
        0.5,
        value_text,
        transform=axs[index].transAxes,
        horizontalalignment='right',
        verticalalignment='center',
        fontsize=16,
        color=text_color
    )
    axs[index].text(
        -.1,
        0.5,
        col,
        transform=axs[index].transAxes,
        horizontalalignment='left',
        verticalalignment='center',
        fontsize=16,
    )
  plt.savefig(f'output/{player} 2019-20 Shooting.png', bbox_inches='tight', pad_inches=2)
