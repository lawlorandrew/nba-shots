import pandas as pd
import matplotlib.pyplot as plt

months = [
  'october',
  'november',
  'december',
  'january',
  'february',
  'march',
  'july',
  'august'
]
df = None
for month in months:
  if (df is None):
    df = pd.read_csv(f'./data/box_score_totals-{month}.csv')
  else:
    month_df = pd.read_csv(f'./data/box_score_totals-{month}.csv')
    df = df.append(month_df)
df['possessions'] = 0.5*((df['fga'] + 0.4*df['fta'] - 1.07*(df['orb']/(df['orb'] + df['Opponent drb'])) * (df['fga'] - df['fg']) + df['tov']) + df['Opponent fga'] + 0.4*df['Opponent fta'] - 1.07*(df['Opponent orb'] / (df['Opponent orb'] + df['drb'])) * (df['Opponent fga'] - df['Opponent fg']) + df['Opponent tov'])
df["Date"] = pd.to_datetime(df["Date"], format="%Y%m%d")
df['Minutes'] = pd.to_numeric(df['Time of Game'].str[0:1])*60 + pd.to_numeric(df['Time of Game'].str[2:])
print(df['Minutes'])
cutoff_date = pd.to_datetime("07/01/2020", format="%m/%d/%Y")
bubble_df = df[df["Date"] > cutoff_date]
bubble_teams = bubble_df['Team'].unique()
non_bubble_df = df[df["Date"] < cutoff_date]
non_bubble_top22_df = non_bubble_df[(non_bubble_df["Team"].isin(bubble_teams)) & (non_bubble_df["Opponent"].isin(bubble_teams))]
# df['off_rtg'] = (df['pts'] / df['possessions']) * 100
# df['eFG%'] = (df['fg'] + 0.5*df['fg3'])/df['fga']
for df_to_use in [bubble_df, non_bubble_df, non_bubble_top22_df]:
  print('GAMES')
  print(df_to_use.shape[0])
  print('PTS PER GAME')
  print(df_to_use['pts'].sum() / df_to_use.shape[0])
  print('OFF RTG')
  print((df_to_use['pts'].sum() / df_to_use['possessions'].sum())*100)
  print('eFG')
  print((df_to_use['fg'].sum() + 0.5*df_to_use['fg3'].sum())/df_to_use['fga'].sum())
  print('3P%')
  print(df_to_use['fg3'].sum()/df_to_use['fg3a'].sum())
  print('FG%')
  print(df_to_use['fg'].sum()/df_to_use['fga'].sum())
  print('FT%')
  print(df_to_use['ft'].sum()/df_to_use['fta'].sum())
  print('Fouls Per Game')
  print(df_to_use['pf'].sum()/df_to_use.shape[0])
  print('FTA Per Game')
  print(df_to_use['fta'].sum()/df_to_use.shape[0])
  print('3Pr')
  print(df_to_use['fg3a'].sum()/df_to_use['fga'].sum())
  print('FGA Per Game')
  print(df_to_use['fga'].sum()/df_to_use.shape[0])
  print('Turnovers Per Game')
  print(df_to_use['tov'].sum()/df_to_use.shape[0])
  print('Time of Game')
  print(df_to_use['Minutes'].sum()/df_to_use.shape[0])
  print('--------')

start_date = df['Date'].min()
# print(start_date)
df['Week'] = (((df['Date'] - start_date).dt.days)//7) + 1
# print(df['Week'].unique())
pre_shutdown = df[df['Week'] < 30]
post_shutdown = df[df['Week'] > 30]
grouped_by_week = df.groupby(['Week']).mean()
grouped_by_week = grouped_by_week.reset_index()
pre_shutdown = grouped_by_week[grouped_by_week['Week'] < 30]
post_shutdown = grouped_by_week[grouped_by_week['Week'] > 30]
post_shutdown['Week'] = post_shutdown['Week'] - 18
# print(grouped_by_week)
fig, ax = plt.subplots()
ax.plot(pre_shutdown['Week'], pre_shutdown['pf'])
# ax.plot(post_shutdown['Week'], post_shutdown['pf'], color='blue')
ax.set_xlabel('Week')
ax.set_ylabel('Fouls Per Game')
ax.set_title('Fouls Per Game (Pre-Bubble)')
plt.savefig('output/Fouls vs Time.png')