import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from graph_comparison import graph_comparison

totals_df = pd.read_csv('./data/nba_per_poss.csv')
totals_df['Name'] = totals_df['Player'].str.split('\\').str[0]
team_colors_df = pd.read_csv('./data/nba_team_colors.csv')

totals_df['FT Rate'] = totals_df['FTA'] / totals_df['FGA']

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



player = 'Duncan Robinson' # the player to graph
filter_by_position= False # whether or not the distributions should use only players of the same position, or all players
position_to_use = None # the position the player should be treated as (if None, just use default position from data)
team = totals_df.loc[totals_df['Name']==player, ['Tm']].squeeze()
colors=team_colors_df.loc[team_colors_df['Team'] == team].squeeze() # team colors to use
cols = ['2P%', '2PA', '3P%', '3PA', 'FT%', 'FTA', 'FT Rate'] # statistics to graph
pct_cols = ['2P%', '3P%', 'FT%', 'FT Rate'] # the statistics that should be rendered as percentages

graph_player(
    stats_df=totals_df,
    player=player,
    team=colors,
    cols=cols,
    pct_cols=pct_cols,
    filter_by_position=filter_by_position,
    position_to_use=position_to_use,
)

def graph_team(stats_df, team, colors_df, cols, pct_cols, filter_by_position=False, position_to_use=None):
  colors=colors_df.loc[colors_df['Team'] == team].squeeze() # team colors to use
  players = stats_df.loc[stats_df['Tm'] == team]
  for index,player in players.iterrows():
    graph_player(
        stats_df=stats_df,
        player=player['Name'],
        team=colors,
        cols=cols,
        pct_cols=pct_cols,
        filter_by_position=filter_by_position,
        position_to_use=position_to_use,
    )

player = 'Jayson Tatum' # the player to graph
filter_by_position= False # whether or not the distributions should use only players of the same position, or all players
position_to_use = None # the position the player should be treated as (if None, just use default position from data)
team = totals_df.loc[totals_df['Name']==player, ['Tm']].squeeze()
colors=team_colors_df.loc[team_colors_df['Team'] == team].squeeze() # team colors to use
cols = ['2P%', '2PA', '3P%', '3PA', 'FT%', 'FTA', 'FT Rate'] # statistics to graph
pct_cols = ['2P%', '3P%', 'FT%', 'FT Rate'] # the statistics that should be rendered as percentages

graph_player(
    stats_df=totals_df,
    player=player,
    team=colors,
    cols=cols,
    pct_cols=pct_cols,
    filter_by_position=filter_by_position,
    position_to_use=position_to_use,
)

cols = ['2P%', '2PA', '3P%', '3PA', 'FT%', 'FTA', 'FT Rate'] # statistics to graph
pct_cols = ['2P%', '3P%', 'FT%', 'FT Rate'] # the statistics that should be rendered as percentages
players = pd.DataFrame([['Jayson Tatum', 'green'], ['LeBron James', 'purple']], columns=['Name', 'Color'])
graph_comparison(
    stats_df=totals_df,
    players=players,
    cols=cols,
    pct_cols=pct_cols,
    filter_by_position=False,
)