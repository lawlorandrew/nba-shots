from graph_player import graph_player

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