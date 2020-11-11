import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from player_scatter import player_scatter
from advanced_stats_radar import plot_advanced_stats_radar
from logo_scatter import logo_scatter

team_playtype_df = pd.read_csv(
    './data/lakers_heat/team_playtypes/offense/total.csv')
team_opp_playtype_df = pd.read_csv(
    './data/lakers_heat/team_playtypes/defense/total.csv')
player_playtype_df = pd.read_csv(
    './data/lakers_heat/player_playtypes/offense/total.csv')
team_totals_df = pd.read_csv('./data/lakers_heat/team_totals/advanced.csv')
player_playtype_df['TOT_POSS'] = player_playtype_df['GP'] * \
    player_playtype_df['POSS']
player_playtype_df['TOT_PTS'] = player_playtype_df['TOT_POSS'] * \
    player_playtype_df['PPP']

filtered_player_playtypes_df = player_playtype_df[player_playtype_df['TEAM_ABBREVIATION'] == 'MIA']
team_colors_df = pd.read_csv('./data/nba_team_colors.csv')
totals_df = pd.read_csv('./data/lakers_heat/players/per_poss.csv')
totals_df['Name_Raw'] = totals_df['Player'].str.split('\\').str[0]
advanced_df = pd.read_csv('./data/lakers_heat/players/advanced.csv')
advanced_df['Name_Raw'] = advanced_df['Player'].str.split('\\').str[0]

filtered_team_playtype_df = team_playtype_df[team_playtype_df['TEAM_ABBREVIATION'] == 'MIA']
filtered_team_playtype_df = filtered_team_playtype_df.sort_values(by='POSS')
print(filtered_team_playtype_df.loc[:,['label', 'POSS', 'PPP']])

filtered_advanced_df = advanced_df[advanced_df['MP'] > 100]

print(filtered_advanced_df.nlargest(10, '3PAr').loc[:,['Name_Raw','3PAr','MP']])

# OVERALL RATINGS
# logo_scatter(
#   df=team_totals_df,
#   xcol='DRtg',
#   ycol='ORtg',
#   xlabel='Defensive Rating',
#   ylabel='Offensive Rating',
#   title='Playoff Efficiency',
# )

#PLAYER RADARS
fig = plt.figure()
plot_advanced_stats_radar(
    # player_name=player['player'],
    # team=player['team_id'],
    # season=player['season'],
    player_name='',
    team='MIA',
    season=2020,
    totals_df=totals_df,
    advanced_stats_df=filtered_advanced_df,
    team_colors_df=team_colors_df,
    fig=fig,
)

# TEAM PLAYTYPE DEFENSE
# filtered_team_opp_playtype_df = team_opp_playtype_df[team_opp_playtype_df['TEAM_ABBREVIATION'] == 'MIA']
# player_scatter(
#   df=filtered_team_opp_playtype_df,
#   xcol='POSS',
#   ycol='PPP',
#   xlabel='Possessions per Game',
#   ylabel='Points per Possession',
#   title='Heat on Defense'
# )

# N = len(filtered_team_opp_playtype_df['PLAY_TYPE'].unique())
# ind = np.arange(N)
# width = 0.35
# fig, ax = plt.subplots(figsize=(10,6))
# print(filtered_team_opp_playtype_df['PPP'])
# print(filtered_team_opp_playtype_df.shape)
# filtered_team_opp_playtype_df = filtered_team_opp_playtype_df.sort_values(by=['POSS'], ascending=False)
# print(filtered_team_opp_playtype_df['PLAY_TYPE'])
# ax.bar(ind, filtered_team_opp_playtype_df['PPP'], width, color='#17408B')
# ax.set_xticks(ind)
# ax.set_xticklabels(['Spot-Up', 'Transition', 'P&R Ball-Handler', 'Isolation', 'P&R Roller', 'Post-Up', 'Handoff', 'Off-Screen'])
# ax.set_title('Lakers Defense')
# ax.set_ylabel('Points Per Possession')
# ax.set_xlabel('Play Type')
# fig.text(x=0.02,y=0.05,s='By Andrew Lawlor, Twitter: @lawlorpalooza', fontsize=6)
# fig.text(x=0.02,y=0.03,s='Data from stats.nba.com', fontsize=6)
# fig.savefig('./output/Laker Defense.png')


# PLAYER PLAYTYPE OFFENSE
# top_player_playtypes_df = filtered_player_playtypes_df.nlargest(15, 'TOT_PTS')
# print(top_player_playtypes_df.head())
# player_scatter(
#   df=top_player_playtypes_df,
#   xcol='POSS',
#   ycol='PPP',
#   xlabel='Possessions per Game',
#   ylabel='Points per Possession',
#   title='Top 15 Heat Scoring Plays'
# )
