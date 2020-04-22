import pandas as pd
import matplotlib.pyplot as plt
from dist_plot import dist_plot
from draw_court import draw_court
from shot_chart import shot_chart, shot_hex_chart

def graph_team_distributions(team_name, stats_df, teams_df, pct_cols):
  team_info = teams_df.loc[teams_df['Full'] == team_name].squeeze()  # team colors to use
  df_to_graph = pd.DataFrame(stats_df)
  cols = ['2P%', '2PA', '3P%', '3PA', 'FT%',
        'FTA', 'FT Rate']  # statistics to graph
  for col in cols:
    df_to_graph[f'{col}_pct'] = df_to_graph[col].rank(pct=True)
  team_stats = df_to_graph.loc[stats_df['Team'] == team_name].squeeze()
  fig = plt.figure(figsize=(8,len(cols)*4), constrained_layout=True)
  gs = fig.add_gridspec(len(cols), 1)
  chart_title = team_name
  sub_title = '2019-20 Season'
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
      x=-.05,
      y=1.02,
      s=sub_title,
      horizontalalignment='left',
      verticalalignment='top',
      fontsize=24,
      style='italic',
  )
  for index, col in enumerate(cols):
    ax = fig.add_subplot(gs[index,0])
    is_pct_col = col in pct_cols
    dist_plot(
        totals=df_to_graph,
        stats_to_graph=team_stats,
        col=col,
        team=team_info,
        ax=ax,
        is_pct_col=is_pct_col
    )
  plt.savefig(f'output/{team_name} 2019-20 Shooting Distribution.png', bbox_inches='tight', pad_inches=2)
  plt.close()

def graph_team_with_shot_chart(team_name, stats_df, teams_df, shots_df, pct_cols, is_hex=False, is_defense=False, use_stats_from_shot_data=False):
  offense_defense_title = 'Defensive' if is_defense else 'Offensive'
  team_info = teams_df.loc[teams_df['Full'] == team_name].squeeze()  # team colors to use
  if (use_stats_from_shot_data):
    df_to_graph = pd.read_csv('./data/team_stats_from_shot_data.csv')
    if (is_defense):
      cols = ['Opponent 2PT Field Goal Attempted', 'Opponent 3PT Field Goal Attempted', 'Opponent 2PT Field Goal%', 'Opponent 3PT Field Goal%'] # statistics to graph
    else:
      cols = ['2PT Field Goal Attempted', '3PT Field Goal Attempted', '2PT Field Goal%', '3PT Field Goal%']  # statistics to graph
  else:
    df_to_graph = pd.DataFrame(stats_df)
    cols = ['2P%', '2PA', '3P%', '3PA', 'FT%',
          'FTA', 'FT Rate']  # statistics to graph
  for col in cols:
    df_to_graph[f'{col}_pct'] = df_to_graph[col].rank(pct=True)
  team_stats = df_to_graph.loc[stats_df['Team'] == team_name].squeeze()
  fig = plt.figure(figsize=(40,28), constrained_layout=True)
  gs = fig.add_gridspec(len(cols), 6)
  chart_title = team_name
  sub_title = f'2019-20 {offense_defense_title}'
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
      x=0,
      y=1.02,
      s=sub_title,
      horizontalalignment='left',
      verticalalignment='top',
      fontsize=40,
      style='italic',
  )
  ax1 = fig.add_subplot(gs[:,:5])
  ax1 = draw_court(ax=ax1, outer_lines=False)
  if (is_defense):
    team_shot_df = shots_df[shots_df['OPPONENT'] == team_name]
  else:
    team_shot_df = shots_df[shots_df['TEAM_NAME'] == team_name]
  if (is_hex):
    shot_hex_chart(shot_df=team_shot_df, ax=ax1)
  else:
    shot_chart(shot_df=team_shot_df, ax=ax1)
  for index, col in enumerate(cols):
    ax = fig.add_subplot(gs[index,5])
    is_pct_col = col in pct_cols
    dist_plot(
        totals=df_to_graph,
        stats_to_graph=team_stats,
        col=col,
        team=team_info,
        ax=ax,
        is_pct_col=is_pct_col,
        show_colors=False,
        fontsize=32
    )
  hex_title = 'Hex' if is_hex else 'Regular'
  plt.savefig(f'output/{team_name} 2019-20 {hex_title} {offense_defense_title} Shot Chart.png', bbox_inches='tight', pad_inches=2)
  plt.close()