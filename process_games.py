import pandas as pd
import numpy as np

games_df = pd.read_csv('./data/games.csv')
team_ratings_df = pd.read_csv('./data/nba_team_advanced.csv')
games_df["Date"] = pd.to_datetime(games_df["Date"], format="%a %b %d %Y")
games_df["Home_Margin"] = games_df["HPTS"] - games_df["VPTS"]
games_df["Home_Win"] = games_df["Home_Margin"] > 0
games_df["Within_3"] = (np.abs(games_df["Home_Margin"]) <= 3)
games_df["Within_5"] = (np.abs(games_df["Home_Margin"]) <= 5) | (games_df['OT'].str.find('OT'))
games_df["Within_10"] = (np.abs(games_df["Home_Margin"]) <= 10) | (games_df['OT'].str.find('OT'))
games_df["Total_PTS"] = games_df["HPTS"] + games_df["VPTS"]
games_df = games_df.merge(
  team_ratings_df[['Team', 'NRtg']],
  left_on="Home/Neutral",
  right_on="Team",
  suffixes=['', '_Home']
)
games_df = games_df.merge(
  team_ratings_df[['Team', 'NRtg']],
  left_on="Visitor/Neutral",
  right_on="Team",
  suffixes=['', '_Away']
)
games_df = games_df.rename(columns={ 'NRtg': 'NRtg_Home'})
games_df = games_df.drop(columns=['Team', 'Team_Away'])
games_df['Rtg_Diff'] = games_df['NRtg_Home'] - games_df['NRtg_Away']

cutoff_date = pd.to_datetime("07/01/2020", format="%m/%d/%Y")
bubble_games_df = games_df[games_df["Date"] > cutoff_date]
bubble_teams = bubble_games_df["Home/Neutral"].unique()
print(bubble_games_df.head())
print(bubble_games_df.shape)
print(bubble_games_df['OT'].count() / bubble_games_df.shape[0])
print(bubble_games_df['Within_3'].sum() / bubble_games_df.shape[0])
print(np.abs(bubble_games_df['Home_Margin']).mean())
print(bubble_games_df['Home_Margin'].mean())
print(bubble_games_df['Home_Win'].sum() / bubble_games_df.shape[0])
print(bubble_games_df['NRtg_Home'].mean())
print(bubble_games_df['NRtg_Away'].mean())
print(bubble_games_df['Rtg_Diff'].mean())

# print(bubble_games_df['Total_PTS'].mean() / 2)

non_bubble_games_df = games_df[games_df["Date"] < cutoff_date]
print(non_bubble_games_df.shape)
print(non_bubble_games_df['OT'].count() / non_bubble_games_df.shape[0])
print(non_bubble_games_df['Within_3'].sum() / non_bubble_games_df.shape[0])
print(np.abs(non_bubble_games_df['Home_Margin']).mean())
print(non_bubble_games_df['Home_Margin'].mean())
print(non_bubble_games_df['Home_Win'].sum() / non_bubble_games_df.shape[0])
print(non_bubble_games_df['Rtg_Diff'].mean())
# print(non_bubble_games_df['Total_PTS'].mean() / 2)

non_bubble_top22_games_df = non_bubble_games_df[(non_bubble_games_df["Home/Neutral"].isin(bubble_teams)) & (non_bubble_games_df["Visitor/Neutral"].isin(bubble_teams))]
print(non_bubble_top22_games_df.shape)
print(non_bubble_top22_games_df['OT'].count() / non_bubble_top22_games_df.shape[0])
print(non_bubble_top22_games_df['Within_3'].sum() / non_bubble_top22_games_df.shape[0])
print(np.abs(non_bubble_top22_games_df['Home_Margin']).mean())
print(non_bubble_top22_games_df['Home_Margin'].mean())
print(non_bubble_top22_games_df['Home_Win'].sum() / non_bubble_top22_games_df.shape[0])
print(non_bubble_top22_games_df['Rtg_Diff'].mean())
# print(non_bubble_top22_games_df['Total_PTS'].mean() / 2)