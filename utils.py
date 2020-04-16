import pandas as pd

def get_team_info(stats_df, teams_df, player_name):
  team_name = stats_df.loc[stats_df['Name'] == player_name, ['Tm']].squeeze()
  team_info = teams_df.loc[teams_df['Team'] == team_name].squeeze()  # team colors to use
  return team_info

def format_dataframe(stats_df, player_name, cols, filter_by_position = False, position_to_use = None):
  totals_df_copy = pd.DataFrame(stats_df)
  if (position_to_use is not None):
    totals_df_copy.loc[totals_df_copy['Name'] == player_name, ['Pos']] = position_to_use
  if (filter_by_position is True):
    position = totals_df_copy.loc[totals_df_copy['Name']==player_name, ['Pos']].squeeze()
    df_to_graph = totals_df_copy.loc[totals_df_copy['Pos'] == position]
    sub_title = 'Compared with ' + position + 's'
  else:
    df_to_graph = pd.DataFrame(totals_df_copy)
    sub_title = 'Compared with all players'
  for col in cols:
    df_to_graph[f'{col}_pct'] = df_to_graph[col].rank(pct=True)
  player_stats_df = df_to_graph.loc[df_to_graph['Name'] == player_name].squeeze()
  return df_to_graph, player_stats_df, sub_title