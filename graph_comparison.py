import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def graph_comparison(stats_df, players, cols, pct_cols, filter_by_position = False, position_to_use = None):
  totals_df_copy = pd.DataFrame(stats_df)
  if (position_to_use is not None and filter_by_position is True):
    totals_df_copy.loc[totals_df_copy['Name'].isin(players.Name), ['Pos']] = position_to_use
    df_to_graph = totals_df_copy.loc[totals_df_copy['Pos'] == position_to_use]
    template_label = f'Compared with {position_to_use}s' 
  else:
    df_to_graph = pd.DataFrame(totals_df_copy)
    template_label = 'Compared with all players'
  for col in cols:
    df_to_graph[f'{col}_pct'] = df_to_graph[col].rank(pct=True)
  playerStats = df_to_graph.loc[df_to_graph['Name'].isin(players.Name)].squeeze()
  fig, axs = plt.subplots(len(cols), 1, figsize=(8,len(cols)*4))
  sns.despine(left=True)
  chart_title = 'Player Comparison'
  fig.suptitle(
      chart_title,
      fontsize=30,
      y=.9,
      x=-.1,
      horizontalalignment='left',
      verticalalignment='bottom',
  )
  for index, col in enumerate(cols):
    sns.distplot(
      df_to_graph[col],
      ax=axs[index],
      hist=False,
      kde_kws={"shade": True},
      color='blue',
    )
    count = 0
    legend_labels = []
    for i, stat in playerStats.iterrows():
      if (count == 0):
        sub_title = stat['Name']
      else:
        sub_title = sub_title + ', ' + stat['Name']
      axs[index].axvline(stat[col], color=players.loc[players['Name'] == stat['Name'], 'Color'].squeeze(), label=stat['Name'])
      count = count + 1
      if (col in pct_cols):
        label = stat['Name'] + ': ' + '{:.0%}'.format(stat[col]) + ', P' + '{:.0f}'.format(stat[f'{col}_pct']*100)
      else:
        label = stat['Name'] + ': ' + '{:.0f}'.format(stat[col]) + ', P' + '{:.0f}'.format(stat[f'{col}_pct']*100)
      legend_labels.append(label)
      #axs[index].text(
      #    stat[col] + axs[index].get_xlim()[1] * 0.01,
      #    axs[index].get_ylim()[1]*0.7,
      #    stat['Name'],
      #    rotation=90
      #)
    axs[index].yaxis.set_visible(False)
    axs[index].set_xlabel('')
    axs[index].legend(
        loc='right',
        bbox_to_anchor=(1.2,0.5),
        labels=legend_labels
    )
    axs[index].text(
        -.2,
        0.5,
        col,
        transform=axs[index].transAxes,
        horizontalalignment='left',
        verticalalignment='center',
        fontsize=16,
    )
  fig.text(
      -.1,
      .9,
      sub_title,
      verticalalignment='top',
      horizontalalignment='left',
      fontsize=16,
      style='italic'
  )
  fig.text(
      1.1,
      .9,
      template_label,
      verticalalignment='top',
      horizontalalignment='right',
      fontsize=16,
      style='italic'
  )
  plt.savefig(f'output/Comparison 2019-20 Shooting.png', bbox_inches='tight', pad_inches=2)