import pandas as pd

def get_team_info(stats_df, teams_df, team):
  team_info = teams_df.loc[teams_df['Team'] == team].squeeze()  # team colors to use
  return team_info

def format_dataframe(stats_df, player_name, team, season, cols, filter_by_position = False, position_to_use = None):
  totals_df_copy = stats_df.drop_duplicates(subset=['player', 'season'], keep='first')
  if (position_to_use is not None):
    totals_df_copy.loc[totals_df_copy['player'] == player_name, ['pos']] = position_to_use
  if (filter_by_position is True):
    position = totals_df_copy.loc[totals_df_copy['player']==player_name, ['pos']].squeeze()
    df_to_graph = totals_df_copy.loc[totals_df_copy['pos'] == position]
    sub_title = 'Compared with ' + position + 's'
  else:
    df_to_graph = pd.DataFrame(totals_df_copy)
    sub_title = 'Compared with all players'
  for col in cols:
    df_to_graph[f'{col}_pct'] = df_to_graph[col].rank(pct=True)
  player_stats_df = df_to_graph.loc[
    (df_to_graph['player'] == player_name) &
    (df_to_graph['team_id'] == team) &
    (df_to_graph['season'] == season)
  ].squeeze()
  return df_to_graph, player_stats_df, sub_title