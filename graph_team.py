from graph_player import graph_player

def graph_team(stats_df, team, teamInfo, cols, pct_cols, filter_by_position=False):
  players = stats_df.loc[stats_df['Tm'] == team]
  for index,player in players.iterrows():
    graph_player(
        stats_df=stats_df,
        player=player['Name'],
        team=teamInfo,
        cols=cols,
        pct_cols=pct_cols,
        filter_by_position=filter_by_position,
    )