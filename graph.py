import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from graph_comparison import graph_comparison
from graph_player import graph_player_distributions, graph_player_with_shot_chart
from graph_team import graph_team_distributions, graph_team_with_shot_chart
from advanced_stats_radar import plot_advanced_stats_radar
from per_poss_radar import plot_per_poss_radar
from player_profile import plot_player_profile
from team_per_poss_radar import plot_team_per_poss_radar
from scipy.signal import savgol_filter
import json

totals_df = pd.read_csv('./data/nba_per_poss.csv')
totals_df['Name'] = totals_df['Player'].str.split('\\').str[0]
team_colors_df = pd.read_csv('./data/nba_team_colors.csv')
team_per_poss_df = pd.read_csv('./data/nba_team_per_poss.csv')
advanced_stats_df = pd.read_csv('./data/nba_advanced.csv')
advanced_stats_df['Name'] = advanced_stats_df['Player'].str.split('\\').str[0]
shot_df = pd.read_csv('./data/all_shots.csv')

totals_df['FT Rate'] = totals_df['FTA'] / totals_df['FGA']
team_per_poss_df['FT Rate'] = team_per_poss_df['FTA'] / team_per_poss_df['FGA']

player = 'Anthony Davis'  # the player to graph
# whether or not the distributions should use only players of the same position, or all players
filter_by_position = False
# the position the player should be treated as (if None, just use default position from data)
position_to_use = None
cols = ['2P%', '2PA', '3P%', '3PA', 'FT%',
        'FTA', 'FT Rate']  # statistics to graph
# the statistics that should be rendered as percentages
pct_cols = ['2P%', '3P%', 'FT%', 'FT Rate']

#graph_player_distributions(
#    stats_df=totals_df,
#    player_name=player,
#    teams_df=team_colors_df,
#    cols=cols,
#    pct_cols=pct_cols,
#    filter_by_position=filter_by_position,
#    position_to_use=position_to_use,
#)

#shot_chart_player = 'Duncan Robinson'

graph_player_with_shot_chart(
    stats_df=totals_df,
    player_name=player,
    teams_df=team_colors_df,
    cols=cols,
    pct_cols=pct_cols,
    shot_df=shot_df,
    filter_by_position=filter_by_position,
    position_to_use=position_to_use,
)

#players = pd.DataFrame([['Jayson Tatum', '#00a55c'], [
#                       'Jaylen Brown', '#bb9753']], columns=['Name', 'Color'])
#graph_comparison(
#    stats_df=totals_df,
#    players=players,
#    cols=cols,
#    pct_cols=pct_cols,
#    filter_by_position=False,
#)

# the statistics that should be rendered as percentages
#pct_cols = ['2P%', '3P%', 'FT%', 'FT Rate']

#graph_team_distributions(
#  team_name='Chicago Bulls',
#  stats_df=team_per_poss_df,
#  teams_df=team_colors_df,
#  pct_cols=pct_cols,
#)

#graph_team_distributions(
#  team_name='Chicago Bulls',
#  stats_df=team_per_poss_df,
#  teams_df=team_colors_df,
#  pct_cols=pct_cols,
#)

fig =plt.figure()
plot_team_per_poss_radar(
  team_name='Milwaukee Bucks',
  totals_df=team_per_poss_df,
  team_colors_df=team_colors_df,
  fig=fig
)
plt.close()

teams = [
  'Philadelphia 76ers',
  #'Chicago Bulls',
  #'San Antonio Spurs'
]
for team in teams:
  graph_team_with_shot_chart(
    team_name=team,
    stats_df=team_per_poss_df,
    teams_df=team_colors_df,
    shots_df=shot_df,
    pct_cols=pct_cols,
  )

  graph_team_with_shot_chart(
    team_name=team,
    stats_df=team_per_poss_df,
    teams_df=team_colors_df,
    shots_df=shot_df,
    pct_cols=pct_cols,
    is_defense=True
  )

  graph_team_with_shot_chart(
    team_name=team,
    stats_df=team_per_poss_df,
    teams_df=team_colors_df,
    shots_df=shot_df,
    pct_cols=pct_cols,
    is_hex=True,
    use_stats_from_shot_data=False,
  )

  graph_team_with_shot_chart(
    team_name=team,
    stats_df=team_per_poss_df,
    teams_df=team_colors_df,
    shots_df=shot_df,
    pct_cols=pct_cols,
    is_hex=True,
    is_defense=True,
    use_stats_from_shot_data=True,
  )

#fig = plt.figure()
#plot_per_poss_radar(
#  player_name='Kyrie Irving',
#  totals_df=totals_df,
#  team_colors_df=team_colors_df,
#  fig=fig
#)

fig = plt.figure()
plot_advanced_stats_radar(
  player_name=player,
  totals_df=totals_df,
  advanced_stats_df=advanced_stats_df,
  team_colors_df=team_colors_df,
  fig=fig,
)
plt.close()

players = [
  # 'Zion Williamson',
  # 'Duncan Robinson',
  # 'Jayson Tatum',
  # 'Lonzo Ball',
  # 'Shai Gilgeous-Alexander',
  # 'Khris Middleton',
  # 'Bradley Beal',
  # 'Christian Wood',
  # 'Blake Griffin',
  # 'Derrick Rose',
  # 'Sekou Doumbouya',
  # 'Bruce Brown',
  # 'Luke Kennard',
  # 'Sviatoslav Mykhailiuk',
  # 'Thon Maker',
  # 'Tony Snell',
  'Markelle Fultz',
  'Jonathan Isaac',
  'Shake Milton',
  'Al Horford'
]
for player_name in players:
  fig = plt.figure()
  plot_advanced_stats_radar(
    player_name=player_name,
    totals_df=totals_df,
    advanced_stats_df=advanced_stats_df,
    team_colors_df=team_colors_df,
    fig=fig,
  )
  graph_player_with_shot_chart(
    stats_df=totals_df,
    player_name=player_name,
    teams_df=team_colors_df,
    cols=cols,
    pct_cols=pct_cols,
    shot_df=shot_df,
    filter_by_position=filter_by_position,
    position_to_use=position_to_use,
  )
player_name = 'Bradley Beal'
shot_df['DISTANCE'] = np.round(np.sqrt(np.square(shot_df['LOC_X']) + np.square(shot_df['LOC_Y'])))
player_shots = shot_df[(shot_df['PLAYER_NAME'] == player_name)]
sums = player_shots[player_shots['SHOT_ZONE_BASIC'] == 'Mid-Range'].sum()
pct = sums['SHOT_MADE_FLAG'] / sums['SHOT_ATTEMPTED_FLAG']
grouped_by_distance = player_shots.groupby(['DISTANCE']).sum()
all_shots_grouped_by_distance = shot_df.groupby(['DISTANCE']).sum()
#grouped_by_distance['FG_PCT'] = grouped_by_distance['SHOT_MADE_FLAG'] / grouped_by_distance['SHOT_ATTEMPTED_FLAG']
grouped_by_distance = grouped_by_distance.reset_index()
all_shots_grouped_by_distance = all_shots_grouped_by_distance.reset_index()
grouped_by_distance['DISTANCE'] = grouped_by_distance['DISTANCE'] / 10
all_shots_grouped_by_distance['DISTANCE'] = all_shots_grouped_by_distance['DISTANCE'] / 10
fig, ax = plt.subplots()
#smoothed = savgol_filter(grouped_by_distance['FG_PCT'], 51, 3)
smoothed = pd.DataFrame(columns=['DISTANCE', 'FG_PCT'])
width = 2
for distance in grouped_by_distance['DISTANCE'].unique():
  grouped_with_margin = grouped_by_distance.loc[(grouped_by_distance['DISTANCE'] >= distance - width) & (grouped_by_distance['DISTANCE'] <= distance + width)]
  grouped_sum = grouped_with_margin.sum()
  fg_pct = grouped_sum['SHOT_MADE_FLAG'] / grouped_sum['SHOT_ATTEMPTED_FLAG']
  smoothed = smoothed.append({ 'DISTANCE': distance, 'FG_PCT': fg_pct }, ignore_index=True)
width = 2
all_shots_smoothed = pd.DataFrame(columns=['DISTANCE', 'FG_PCT'])
for distance in all_shots_grouped_by_distance['DISTANCE'].unique():
  all_shots_grouped_with_margin = all_shots_grouped_by_distance.loc[(all_shots_grouped_by_distance['DISTANCE'] >= distance - width) & (all_shots_grouped_by_distance['DISTANCE'] <= distance + width)]
  all_shots_grouped_sum = all_shots_grouped_with_margin.sum()
  fg_pct = all_shots_grouped_sum['SHOT_MADE_FLAG'] / all_shots_grouped_sum['SHOT_ATTEMPTED_FLAG']
  all_shots_smoothed = all_shots_smoothed.append({ 'DISTANCE': distance, 'FG_PCT': fg_pct }, ignore_index=True)
ax.plot(smoothed['DISTANCE'], smoothed['FG_PCT'], c='#002b5c', label=player_name)
ax.plot(all_shots_smoothed['DISTANCE'], all_shots_smoothed['FG_PCT'], c='#E31837', label='NBA Average')
ax.axvline(23.75, c='#000000')
ax.axvline(22, c='#000000')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlabel('Distance (Feet)')
ax.set_ylabel('FG Percentage')
ax.set_ylim(0,1)
ax.set_xlim(-1,40)
ax.set_title(f'{player_name} FG Percentage by Distance')
ax.text(x=24, y=1, s='Above the Break 3', verticalalignment='top', rotation=90)
ax.text(x=22.25, y=1, s='Corner 3', verticalalignment='top', rotation=90)
ax.legend()
fig.text(
  x=.02,
  y=.02,
  s='Data from stats.nba.com',
  horizontalalignment='left',
  verticalalignment='top',
  fontsize=8,
  style='italic'
)
plt.savefig(f'./output/{player_name} Pct by Distance.png')
print(player_shots.loc[player_shots['SHOT_MADE_FLAG'] == True, 'DISTANCE'].max())
print(player_shots.loc[player_shots['SHOT_MADE_FLAG'] == True, ['DISTANCE', 'LOC_X', 'LOC_Y']].sort_values(by='DISTANCE', ascending=False).head())
print(pct)

# print(player_shots['GAME_DATE'])
# pre_all_star = player_shots[(player_shots['GAME_DATE'] < 20200216) & (player_shots['SHOT_ZONE_BASIC'] != 'Backcourt')]
# post_all_star = player_shots[(player_shots['GAME_DATE'] > 20200216) & (player_shots['SHOT_ZONE_BASIC'] != 'Backcourt')]
# pre_grouped = pre_all_star.groupby(['SHOT_ZONE_BASIC']).sum()
# pre_grouped = pre_grouped.reset_index()
# pre_total = pre_all_star.sum()
# pre_total['SHOT_ZONE_BASIC'] = 'Total'
# pre_grouped = pre_grouped.append(pre_total, ignore_index=True)
# post_grouped = post_all_star.groupby(['SHOT_ZONE_BASIC']).sum()
# post_grouped = post_grouped.reset_index()
# post_total = post_all_star.sum()
# print(post_total['SHOT_ATTEMPTED_FLAG'])
# post_total['SHOT_ZONE_BASIC'] = 'Total'
# post_grouped = post_grouped.append(post_total, ignore_index=True)
# print(pre_grouped.shape[0])
# print(post_grouped.shape[0])
# print(pre_grouped)
# print(post_grouped['SHOT_ATTEMPTED_FLAG'])
# fig, ax = plt.subplots()
# x = np.arange(pre_grouped.shape[0])
# width = 0.35
# ax.bar(x - width / 2, pre_grouped['SHOT_ATTEMPTED_FLAG'] / 55, width, label='Pre All-Star', color='#bb9753')
# ax.bar(x + width / 2, post_grouped['SHOT_ATTEMPTED_FLAG'] / 9, width, label='Post All-Star', color='#00a55c')
# ax.set_xticks(x)
# ax.set_xticklabels(pre_grouped['SHOT_ZONE_BASIC'])
# ax.set_ylabel('Shots per game')
# ax.set_xlabel('Shot Zone')
# ax.set_title('Jayson Tatum Pre vs. Post All-Star Game')
# ax.legend()
# plt.show()


#plot_player_profile('Giannis Antetokounmpo')

sixers_df = pd.read_csv('./data/sixers_advanced.csv')
sixers_df['Name'] = sixers_df['Player'].str.split('\\').str[0]
fig, ax = plt.subplots()
ax.scatter(sixers_df['MP'], sixers_df['3PAr'], c='#006bb6', s=5)
ax.set_ylabel('3-Point Rate')
ax.set_xlabel('Minutes Played')
ax.set_title('2019-20 Philadelphia 76ers')
ax.set_xlim(-50,2950)
fig.text(x=0.02,y=0.02,s='Data from Basketball Reference')
labels = sixers_df[sixers_df['Name'].isin(
  [
    'Shake Milton',
    'Joel Embiid',
    'Ben Simmons',
    'Tobias Harris',
    'Furkan Korkmaz',
    'Al Horford',
    'Josh Richardson',
    'Matisse Thybulle',
    'Mike Scott',
    'Alec Burks',
    'Glenn Robinson',
  ]
)]
for i, row in labels.iterrows():
  ax.annotate(row['Name'], (row['MP'] + 10, row['3PAr'] + 0.01))
plt.savefig('output/Philadelphia MP vs 3PAr.png')