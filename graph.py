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
from logo_scatter import logo_scatter
from shot_chart import shot_chart
from draw_court import draw_court
import json
import unidecode
from player_scatter import player_scatter
from big_men_passing import big_men_passing

totals_df = pd.read_csv('./data/nba_per_poss.csv')
totals_df['Name_Raw'] = totals_df['player'].str.split('\\').str[0]
totals_df['Name'] = totals_df['Name_Raw'].apply(lambda x: unidecode.unidecode(x))
team_colors_df = pd.read_csv('./data/nba_team_colors.csv')
team_per_poss_df = pd.read_csv('./data/nba_team_per_poss.csv')
opponent_per_poss_df = pd.read_csv('./data/nba_opponent_per_poss.csv')
advanced_stats_df = pd.read_csv('./data/nba_advanced.csv')
team_advanced_stats_df = pd.read_csv('./data/nba_team_advanced.csv')
advanced_stats_df['Name_Raw'] = advanced_stats_df['player'].str.split('\\').str[0]
advanced_stats_df['Name'] = advanced_stats_df['Name_Raw'].apply(lambda x: unidecode.unidecode(x))
shot_df = pd.read_csv('./data/all_shots.csv')
bubble_stats_df = pd.read_csv('./data/bubble_advanced_team_stats.csv')

totals_df['FT Rate'] = totals_df['fta_per_poss'] / totals_df['fga_per_poss']
team_per_poss_df['FT Rate'] = team_per_poss_df['FTA'] / team_per_poss_df['FGA']

player = 'Anthony Davis'  # the player to graph
# whether or not the distributions should use only players of the same position, or all players
filter_by_position = False
# the position the player should be treated as (if None, just use default position from data)
position_to_use = None
cols = ['fg2_pct', 'fg2a_per_poss', 'fg3_pct', 'fg3a_per_poss', 'ft_pct',
        'fta_per_poss', 'FT Rate']  # statistics to graph
# the statistics that should be rendered as percentages
pct_cols = ['fg2_pct', 'fg3_pct', 'ft_pct', 'FT Rate']

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

# graph_player_with_shot_chart(
#     stats_df=totals_df,
#     player_name=player,
#     teams_df=team_colors_df,
#     cols=cols,
#     pct_cols=pct_cols,
#     shot_df=shot_df,
#     filter_by_position=filter_by_position,
#     position_to_use=position_to_use,
# )

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

teams = [
]
# teams = team_per_poss_df['Team'].unique()
for team in teams:
  print(team)
  # graph_team_with_shot_chart(
  #   team_name=team,
  #   stats_df=team_per_poss_df,
  #   teams_df=team_colors_df,
  #   shots_df=shot_df,
  #   pct_cols=pct_cols,
  # )

  # graph_team_with_shot_chart(
  #   team_name=team,
  #   stats_df=team_per_poss_df,
  #   teams_df=team_colors_df,
  #   shots_df=shot_df,
  #   pct_cols=pct_cols,
  #   is_defense=True
  # )

  # graph_team_with_shot_chart(
  #   team_name=team,
  #   stats_df=team_per_poss_df,
  #   teams_df=team_colors_df,
  #   shots_df=shot_df,
  #   pct_cols=pct_cols,
  #   is_hex=True,
  #   use_stats_from_shot_data=False,
  # )

  # graph_team_with_shot_chart(
  #   team_name=team,
  #   stats_df=team_per_poss_df,
  #   teams_df=team_colors_df,
  #   shots_df=shot_df,
  #   pct_cols=pct_cols,
  #   is_hex=True,
  #   is_defense=True,
  #   use_stats_from_shot_data=True,
  # )

#fig = plt.figure()
#plot_per_poss_radar(
#  player_name='Kyrie Irving',
#  totals_df=totals_df,
#  team_colors_df=team_colors_df,
#  fig=fig
#)

players = [
  # ('Montrezl Harrell', 'LAC', 2020),
  # ('Lauri Markkanen', 'CHI', 2019)
  # ('John Wall', 'WAS', 2017),
  # ('Bradley Beal', 'WAS', 2020),
]
players_without_teams = advanced_stats_df[
  advanced_stats_df['team_id'] == 'TOT'
]
# players = advanced_stats_df['player'].unique()
# players = [players[0]]
# for i, player in players_without_teams.iterrows():
for player in players:
  # print(player['player'])
  print(player)
  fig = plt.figure()
  plot_advanced_stats_radar(
    # player_name=player['player'],
    # team=player['team_id'],
    # season=player['season'],
    player_name=player[0],
    team=player[1],
    season=player[2],
    totals_df=totals_df,
    advanced_stats_df=advanced_stats_df,
    team_colors_df=team_colors_df,
    fig=fig,
  )
  # graph_player_with_shot_chart(
  #   stats_df=totals_df,
  #   player_name=player[0],
  #   team=player[1],
  #   season=player[2],
  #   # team=player['team_id'],
  #   teams_df=team_colors_df,
  #   cols=cols,
  #   pct_cols=pct_cols,
  #   shot_df=shot_df,
  #   filter_by_position=filter_by_position,
  #   position_to_use=position_to_use,
  # )
# player_name = 'Bradley Beal'
# shot_df['DISTANCE'] = np.round(np.sqrt(np.square(shot_df['LOC_X']) + np.square(shot_df['LOC_Y'])))
# player_shots = shot_df[(shot_df['PLAYER_NAME'] == player_name)]
# sums = player_shots[player_shots['SHOT_ZONE_BASIC'] == 'Mid-Range'].sum()
# pct = sums['SHOT_MADE_FLAG'] / sums['SHOT_ATTEMPTED_FLAG']
# grouped_by_distance = player_shots.groupby(['DISTANCE']).sum()
# all_shots_grouped_by_distance = shot_df.groupby(['DISTANCE']).sum()
# #grouped_by_distance['FG_PCT'] = grouped_by_distance['SHOT_MADE_FLAG'] / grouped_by_distance['SHOT_ATTEMPTED_FLAG']
# grouped_by_distance = grouped_by_distance.reset_index()
# all_shots_grouped_by_distance = all_shots_grouped_by_distance.reset_index()
# grouped_by_distance['DISTANCE'] = grouped_by_distance['DISTANCE'] / 10
# all_shots_grouped_by_distance['DISTANCE'] = all_shots_grouped_by_distance['DISTANCE'] / 10
# fig, ax = plt.subplots()
# #smoothed = savgol_filter(grouped_by_distance['FG_PCT'], 51, 3)
# smoothed = pd.DataFrame(columns=['DISTANCE', 'FG_PCT'])
# width = 2
# for distance in grouped_by_distance['DISTANCE'].unique():
#   grouped_with_margin = grouped_by_distance.loc[(grouped_by_distance['DISTANCE'] >= distance - width) & (grouped_by_distance['DISTANCE'] <= distance + width)]
#   grouped_sum = grouped_with_margin.sum()
#   fg_pct = grouped_sum['SHOT_MADE_FLAG'] / grouped_sum['SHOT_ATTEMPTED_FLAG']
#   smoothed = smoothed.append({ 'DISTANCE': distance, 'FG_PCT': fg_pct }, ignore_index=True)
# width = 2
# all_shots_smoothed = pd.DataFrame(columns=['DISTANCE', 'FG_PCT'])
# for distance in all_shots_grouped_by_distance['DISTANCE'].unique():
#   all_shots_grouped_with_margin = all_shots_grouped_by_distance.loc[(all_shots_grouped_by_distance['DISTANCE'] >= distance - width) & (all_shots_grouped_by_distance['DISTANCE'] <= distance + width)]
#   all_shots_grouped_sum = all_shots_grouped_with_margin.sum()
#   fg_pct = all_shots_grouped_sum['SHOT_MADE_FLAG'] / all_shots_grouped_sum['SHOT_ATTEMPTED_FLAG']
#   all_shots_smoothed = all_shots_smoothed.append({ 'DISTANCE': distance, 'FG_PCT': fg_pct }, ignore_index=True)
# ax.plot(smoothed['DISTANCE'], smoothed['FG_PCT'], c='#002b5c', label=player_name)
# ax.plot(all_shots_smoothed['DISTANCE'], all_shots_smoothed['FG_PCT'], c='#E31837', label='NBA Average')
# ax.axvline(23.75, c='#000000')
# ax.axvline(22, c='#000000')
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)
# ax.set_xlabel('Distance (Feet)')
# ax.set_ylabel('FG Percentage')
# ax.set_ylim(0,1)
# ax.set_xlim(-1,40)
# ax.set_title(f'{player_name} FG Percentage by Distance')
# ax.text(x=24, y=1, s='Above the Break 3', verticalalignment='top', rotation=90)
# ax.text(x=22.25, y=1, s='Corner 3', verticalalignment='top', rotation=90)
# ax.legend()
# fig.text(
#   x=.02,
#   y=.02,
#   s='Data from stats.nba.com',
#   horizontalalignment='left',
#   verticalalignment='top',
#   fontsize=8,
#   style='italic'
# )
# plt.savefig(f'./output/{player_name} Pct by Distance.png')
# print(player_shots.loc[player_shots['SHOT_MADE_FLAG'] == True, 'DISTANCE'].max())
# print(player_shots.loc[player_shots['SHOT_MADE_FLAG'] == True, ['DISTANCE', 'LOC_X', 'LOC_Y']].sort_values(by='DISTANCE', ascending=False).head())
# print(pct)

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

# logo_scatter(
#   df=team_advanced_stats_df,
#   xcol='3PAr',
#   ycol='ORtg',
#   xlabel='Three-Point Attempt Rate',
#   ylabel='Offensive Rating',
#   title='More Three-Pointers Leads to Better Offense',
# )

# print(shot_df['GAME_DATE'])
# lillard_post_bubble = shot_df[
#   (shot_df['PLAYER_NAME'] == 'Damian Lillard') &
#   (shot_df['GAME_DATE'] > 20200701)
# ]
# print(lillard_post_bubble['GAME_DATE'])
# fig, ax = plt.subplots(figsize=(20,15))
# ax = draw_court(ax=ax, outer_lines=False)
# shot_chart(
#   shot_df=lillard_post_bubble,
#   ax=ax
# )
# plt.savefig('./output/lillard_post_bubble_shots.png')

# isolations_df = pd.read_csv('./data/playoff_isolations_defense.csv')
# isolations_df = isolations_df.nlargest(20, 'POSS')
# isolations_df = isolations_df.merge(team_colors_df, left_on='TEAM_ABBREVIATION', right_on='Team')
# player_scatter(
#   df=isolations_df,
#   xcol='POSS',
#   ycol='PPP',
#   xlabel='Isolations per Game',
#   ylabel='Points per Possession Allowed',
#   title='Top 20 Most Frequent Isolation Defenders in the Playoffs'
# )
# isolations_df = pd.read_csv('./data/playoff_isolations.csv')
# isolations_df = isolations_df.nlargest(20, 'PTS')
# isolations_df = isolations_df.merge(team_colors_df, left_on='TEAM_ABBREVIATION', right_on='Team')
# player_scatter(
#   df=isolations_df,
#   xcol='POSS',
#   ycol='PPP',
#   xlabel='Isolations per Game',
#   ylabel='Points per Possession',
#   title='Top 20 Isolation Scorers in the Playoffs'
# )

# team_isolations_df = pd.read_csv('./data/team_playoff_isolations.csv')
# team_isolations_df['TOTAL_POSS'] = team_isolations_df['POSS'] * team_isolations_df['GP']
# team_isolations_df['TOTAL_PTS'] = team_isolations_df['PTS'] * team_isolations_df['GP']
# team_isolations_grouped_df = team_isolations_df.loc[:,['YEAR', 'TOTAL_POSS', 'TOTAL_PTS', 'GP']].groupby('YEAR').sum()
# team_isolations_grouped_df['POSS'] = team_isolations_grouped_df['TOTAL_POSS']/team_isolations_grouped_df['GP']
# team_isolations_grouped_df['PPP'] = team_isolations_grouped_df['TOTAL_PTS'] / team_isolations_grouped_df['TOTAL_POSS']
# print(team_isolations_grouped_df['POSS'])
# fig, ax = plt.subplots()
# color='#17408B'
# ax.plot(team_isolations_grouped_df.index, team_isolations_grouped_df['POSS'], color=color)
# ax.set_ylabel('Possessions', color=color)
# ax.tick_params(axis='y', labelcolor=color)
# ax.set_xticks([2016,2017,2018,2019,2020])
# ax.set_xticklabels([2016,2017,2018,2019,2020])
# ax.set_title('Total Isolations in the Playoffs')
# ax2 = ax.twinx()
# color='#C9082A'
# ax2.plot(team_isolations_grouped_df.index, team_isolations_grouped_df['PPP'], color=color)
# ax2.set_ylabel('Points per Possession', color=color)
# ax2.tick_params(axis='y', labelcolor=color)
# fig.tight_layout()
# plt.savefig('./output/Playoff Isolations Over Time.png')


# playtypes_df = pd.read_csv('./data/playtypes.csv')
# playtypes_df.loc[playtypes_df['PLAY_TYPE'].isin(['pnr_roll', 'pnr_bh']),'PLAY_TYPE'] = 'PNR'
# playtypes_df = playtypes_df.groupby(['PLAY_TYPE', 'SEASON_TYPE', 'TEAM_ABBREVIATION']).sum()
# playtypes_df = playtypes_df.reset_index()
# playtypes_df['ALL_POSS'] = (playtypes_df['POSS'] / playtypes_df['POSS_PCT']) * playtypes_df['GP']
# playtypes_df['PLAYTYPE_POSS'] = playtypes_df['POSS'] * playtypes_df['GP']
# playtypes_grouped_df = playtypes_df.loc[:,['ALL_POSS', 'PLAYTYPE_POSS', 'GP', 'PLAY_TYPE', 'SEASON_TYPE']].groupby(['PLAY_TYPE', 'SEASON_TYPE']).sum()
# playtypes_grouped_df = playtypes_grouped_df.reset_index()
# playtypes_totals_df = playtypes_grouped_df.groupby(['PLAY_TYPE']).sum()
# playtypes_totals_df = playtypes_totals_df.reset_index()
# playtypes_totals_df['TOTAL_FREQ'] = playtypes_totals_df['PLAYTYPE_POSS'] / playtypes_totals_df['ALL_POSS']
# total_grouped_df = playtypes_df.groupby(['SEASON_TYPE', 'PLAY_TYPE']).sum()
# total_grouped_df['POSS_PER_GAME'] = total_grouped_df['PLAYTYPE_POSS'] / total_grouped_df['GP']
# print(total_grouped_df['POSS_PER_GAME'])
# playtypes_grouped_df['FREQ'] = playtypes_grouped_df['PLAYTYPE_POSS'] / playtypes_grouped_df['ALL_POSS']
# playtypes_grouped_df = playtypes_grouped_df.merge(playtypes_totals_df.loc[:,['PLAY_TYPE', 'TOTAL_FREQ']], left_on='PLAY_TYPE', right_on='PLAY_TYPE')
# playtypes_grouped_df = playtypes_grouped_df.sort_values(by=['TOTAL_FREQ', 'SEASON_TYPE'], ascending=False)
# N = len(playtypes_grouped_df['PLAY_TYPE'].unique())
# ind = np.arange(N)
# width = 0.35
# fig, ax = plt.subplots(figsize=(10,6))
# ax.bar(ind, playtypes_grouped_df[playtypes_grouped_df['SEASON_TYPE'] == 'reg']['FREQ'], width, label='Regular Season', color='#17408B')
# ax.bar(ind + width, playtypes_grouped_df[playtypes_grouped_df['SEASON_TYPE'] == 'playoff']['FREQ'], width, label='Playoffs', color='#C9082A')
# ax.set_xticks(ind + width / 2)
# ax.set_xticklabels(['PNR', 'Spot-Up', 'Transition', 'Cut', 'Isolation', 'Handoff', 'Offscreen', 'Post-Up'])
# ax.set_title('How Teams Finish Plays')
# ax.set_ylabel('Frequency')
# ax.set_xlabel('Play Type')
# ax.legend()
# fig.text(x=0.02,y=0.05,s='By Andrew Lawlor, Twitter: @lawlorpalooza', fontsize=6)
# fig.text(x=0.02,y=0.03,s='Data from stats.nba.com', fontsize=6)
# fig.text(x=0.02,y=0.01,s='Updated 8/28/20', fontsize=6)
# fig.savefig('./output/Playtypes.png')

# isolations_df = pd.read_csv('./data/playoff_team_isolations.csv')
# print(isolations_df.columns)
# isolations_df['TOTAL_POSS'] = isolations_df['POSS'] * isolations_df['GP']
# total_df = isolations_df.sum()
# total_df['POSS_PER_GAME'] = total_df['TOTAL_POSS'] / total_df['GP']
# print(total_df['POSS_PER_GAME'])


# df = pd.read_csv('./data/nba_shooting_by_range.csv')
# df['5Ft_Pts'] = df['Less Than 5 ft._FGM']*2
# df = df.merge(team_colors_df, left_on='TEAM_ABBREVIATION', right_on='Team')
# df = df[
#     (df['Team'].isin(['OKC', 'LAL'])) &
#     (df['PLAYER_NAME'].isin(
#       [
#         'LeBron James',
#         'Anthony Davis',
#         'JaVale McGee',
#         'Dwight Howard',
#         'Danny Green',
#         'Kentavious Caldwell-Pope',
#         'Kyle Kuzma',
#         'Alex Caruso',
#         'Markieff Morris',
#         'JR Smith',
#         'Dion Waiters',
#         'Quinn Cook',
#         'Jared Dudley',
#         'Steven Adams',
#         'Nerlens Noel',
#         'Dennis Schroder',
#         'Shai Gilgeous-Alexander',
#         'Chris Paul',
#         'Darius Bazley',
#         'Luguentz Dort',
#         'Danilo Gallinari',
#         'Terrance Ferguson',
#         'Mike Muscala',
#         'Abdel Nader',
#         'Hamidou Diallo',
#         'Andre Roberson',
#         'Deonte Burton'
#       ]
#     ))
#   ]
# print(shot_df.columns)
# deep_shot_df = shot_df[shot_df['SHOT_DISTANCE'] > 28]
# deep_shot_df_grouped = deep_shot_df.groupby(['PLAYER_NAME', 'PLAYER_ID', 'TEAM_ID', 'TEAM_NAME']).sum()
# # catch_shoot_df = pd.read_csv('./data/catch_shoot.csv')
# deep_shot_df_grouped = deep_shot_df_grouped.reset_index()
# deep_shot_df_grouped = deep_shot_df_grouped[deep_shot_df_grouped['SHOT_ATTEMPTED_FLAG'] >= 10]
# print(deep_shot_df_grouped[deep_shot_df_grouped['PLAYER_NAME'] == 'Davis Bertans'])
# deep_shot_df_grouped = pd.merge(deep_shot_df_grouped, team_colors_df, left_on='TEAM_NAME', right_on='Full')
# print(deep_shot_df_grouped.columns)
# # catch_shoot_df = catch_shoot_df[catch_shoot_df['CATCH_SHOOT_FG3A'] >= 100]
df = pd.read_csv('./data/tracking/post_ups.csv')
df = pd.merge(df, team_colors_df, left_on='TEAM_ABBREVIATION', right_on='NBA_Abbr')
# print(df.columns)
# df['MP'] = df['MIN'] * df['GP']
# df = df[df['MP'] >= 25]
# df['PIE'] = df['PIE']*100
# df = df[df['PASSES_MADE'] >= 10]
print(df.columns)
df = df[df['POST_TOUCHES'] >= 4]
player_scatter(
  df=df,
  xcol='POST_TOUCHES',
  ycol='POST_TOUCH_AST',
  xlabel='Post-Ups Per Game',
  ylabel='Post-Up Assists Per Game',
  title='Post-Up Passing',
  subtitle='2020-21 Regular Season, Min. 4 Post-Ups Per Game, Through 1-1'
)

# draft_df = pd.read_csv('./data/2020_draft.csv')
# draft_df['Name_Raw'] = draft_df['Player'].str.split('\\').str[0]
# draft_df['Name'] = draft_df['Name_Raw'].apply(lambda x: unidecode.unidecode(x))
# df = pd.merge(df, draft_df, left_on='PLAYER_NAME', right_on='Name')
# df = df.sort_values(by='Pk',ascending=True)
# print(df['PLAYER_NAME'])
# df['Name Abbr'] = df['PLAYER_NAME'].str.split(" ").str[1]
# fig, ax = plt.subplots(dpi=500, figsize=(10,4))
# df = df[df['MIN'] >= 10]
# N = df.shape[0]
# X = np.arange(N)
# width = 0.5
# ax.bar(X, df['PIE'], width, color=df['Primary'])
# ax.set_xticks(X)
# ax.set_xticklabels(df['Name Abbr'], rotation=90, fontsize=6)
# ax.set_ylabel('Player Impact Estimate')
# ax.set_xlabel('Player')
# fig.tight_layout(rect=[0, 0.03, 1, 0.95], w_pad=1.5, h_pad=3.5)
# fig.suptitle('Preseason Player Impact', y=1, fontsize=20)
# ax.set_title('Draft Year = 2019, Season = 2020, Min. 10 Minutes Played')
# plt.savefig('./output/Preseason Rookie Impact.png')
# print(df['Name'])
# player_scatter(
#   df=df,
#   xcol='Pk',
#   ycol='PIE',
#   xlabel='Pick',
#   ylabel='Player Impact Estimate',
#   title='Preseason Rookie Efficiency',
#   subtitle='Draft Year = 2020, Season = 2020'
# )

# logo_scatter(
#   df=team_advanced_stats_df,
#   xcol='ORB%',
#   ycol='DRB%',
#   xlabel='Offensive Rebounding Rate',
#   ylabel='Defensive Rebounding Rate',
#   title='Rebounding in the 2019-20 Regular Season',
# )

# playoff_pg_df = pd.read_csv('./data/playoff_pergame.csv')
# playoff_pg_df = playoff_pg_df.merge(team_colors_df,left_on='Tm', right_on='Team')
# playoff_pg_df['Bin'] = pd.cut(playoff_pg_df['MP'], [0,10,20,30,40,50], labels=['< 10', '10-20', '20-30', '30-40', '40+'])
# playoff_pg_df = playoff_pg_df.sort_values(by=['Tm'])
# print(playoff_pg_df.columns)

# row = 0
# col = 0
# fig, axs = plt.subplots(4,4, sharey=True, dpi=250)
# for team in playoff_pg_df['Tm'].unique():
#   team_df = playoff_pg_df[playoff_pg_df['Tm'] == team]
#   color=team_df['Primary'].unique()[0]
#   # axs[row,col].hist(team_df['MP'], bins=[0,5,10,15,20,25,30,35,40,45], color=team_df['Primary'].unique())
#   sns.distplot(
#     team_df['MP'],
#     ax=axs[row,col],
#     kde_kws={"shade": True},
#     color=color,
#     bins=[0,10,20,30,40,50],
#   )
#   axs[row,col].set_xlim(-5,45)
#   axs[row,col].set_xlabel(team_df['Tm'].unique().squeeze())
#   axs[row,col].set_xticks([])
#   axs[row,col].set_yticks([])
#   if col < 3:
#     col += 1
#   else:
#     col = 0
#     row += 1
# fig.tight_layout(rect=[0, 0.03, 1, 0.95])
# fig.suptitle('Playoff Minute Distributions')
# fig.text(
#   x=.5,
#   y=0.94,
#   s='X Axis: Minutes Played, Y Axis: # of Players',
#   horizontalalignment='center',
#   verticalalignment='top',
#   fontsize=8,
#   style='italic'
# )
# fig.text(
#   x=.02,
#   y=0.04,
#   s='Data from Basketball Reference',
#   horizontalalignment='left',
#   verticalalignment='top',
#   fontsize=8,
#   style='italic'
# )
# fig.text(
#   x=.98,
#   y=0.04,
#   s='By Andrew Lawlor, Twitter: @lawlorpalooza',
#   horizontalalignment='right',
#   verticalalignment='top',
#   fontsize=8,
#   style='italic'
# )
# plt.savefig('./output/Playoff MP Histogram.png')