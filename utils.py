def get_team_info(stats_df, teams_df, player_name):
  team_name = stats_df.loc[stats_df['Name'] == player_name, ['Tm']].squeeze()
  team_info = teams_df.loc[teams_df['Team'] == team_name].squeeze()  # team colors to use
  return team_info