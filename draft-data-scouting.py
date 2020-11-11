import pandas as pd
from radar_plot import radar_plot
import matplotlib.pyplot as plt

torvik_df = pd.read_csv('./data/torvik.csv')
torvik_df = torvik_df[torvik_df['Min%'] >= 40]
torvik_df['Assist%_percentile'] = torvik_df['Assist%'].rank(pct=True)
torvik_df = torvik_df[torvik_df['Role'].isin(['PF/C', 'C'])]
nba_df = pd.read_csv('./data/draft/ncaa-totals-2006-07.csv')
nba_df = nba_df[nba_df['NBA_g'] > 0]
merged_df = pd.merge(torvik_df, nba_df, left_on=['Name', 'Season'], right_on=['player', 'year_max'])
merged_df = merged_df[merged_df['NBA_g'].notnull()]
merged_df['NBA_min'] = merged_df['NBA_mp_per_g'] * merged_df['NBA_g']
merged_df = merged_df[merged_df['NBA_min'] >= 100]
merged_df['Name'].to_csv('./data/centers.csv')
draft_rankings_df = pd.read_csv('./data/draft/draft_rankings.csv')
early_entrants_df = pd.read_csv('./data/draft/early-entrants.csv')
df_2020 = torvik_df[torvik_df['Season'] == 2020]
draft_class = pd.merge(df_2020, draft_rankings_df, how='inner', left_on='Name', right_on='Name')
print(draft_class.nlargest(30, 'Assist%_percentile').loc[:,['Name', 'Assist%', 'Assist%_percentile']])
# print(merged_df.nlargest(50, 'NBA_blk_per_g').loc[:,['Name', 'BLK%', 'NBA_blk_per_g', 'NBA_mp_per_g']])
# print(draft_class.nlargest(30, 'BLK%').loc[:,['Name', 'BLK%', 'Draft Ranking']])
# print(merged_df.nlargest(40, 'STL%').loc[:,['Name', 'STL%', 'NBA_blk_per_g', 'NBA_mp_per_g']])
# print(draft_class.nlargest(30, 'STL%').loc[:,['Name', 'STL%', 'Draft Ranking']])
# print(draft_class.nlargest(30, 'BLK%').loc[:,['Name', 'BLK%', 'Draft Ranking']])
# print(draft_class.nsmallest(30, 'Fouls/40').loc[:,['Name', 'Fouls/40', 'Draft Ranking']])



# wings_df = pd.read_csv('./data/draft/draft-3-d-wings.csv')
# early_entrants_df = pd.read_csv('./data/draft/early-entrants.csv')
# wings_df['Name'] = wings_df['Player'].str.split('\\').str[0]
# wings_df = wings_df[
#     (wings_df['MP'] > 500) &
#     ((wings_df['Class'] == 'SR') | wings_df['Name'].isin(early_entrants_df['Player'])) &
#     (wings_df['3PA'] >= 1)
# ]
# wings_df.loc[:, ['Name', 'STL%', 'BLK%', 'FT%', '3PA',
#                  '3P%', 'DRtg']].to_csv('./output/draft-3-d-wings.csv')

# wings_df.rename(columns={
#     'PF': 'PF/G',
#     '3PA': '3PA/G',
#     'FTA': 'FTA/G',
#     '2PA': '2PA/G'
# }, inplace=True)
# player_name = 'CJ Elleby'
# stats_to_graph = wings_df[wings_df['Name'] == player_name].squeeze()
# college_df = pd.read_csv('./data/college_team_colors.csv')
# team_info = college_df[college_df['Team'] == 'WSU'].squeeze()
# fig = plt.figure(dpi=250)
# advanced_stats_df = pd.read_csv('./data/nba_advanced.csv')
# totals_df = pd.read_csv('./data/nba_per_game.csv')
# merged_df = advanced_stats_df.merge(
#     totals_df, on=['player', 'team_id', 'season'])
# merged_df.rename(columns={
#     'pf_per_g': 'PF/G',
#     'fg3a_per_g': '3PA/G',
#     'fta_per_g': 'FTA/G',
#     'fg2a_per_g': '2PA/G',
#     'ast_pct': 'AST%',
#     'blk_pct': 'BLK%',
#     'drb_pct': 'DRB%',
#     'orb_pct': 'ORB%',
#     'usg_pct': 'USG%',
#     'tov_pct': 'TOV%',
#     'fg3_pct': '3P%',
#     'fg2_pct': '2P%',
#     'ts_pct': 'TS%',
#     'ft_pct': 'FT%',
#     'stl_pct': 'STL%',
# }, inplace=True)
# merged_df = merged_df.drop_duplicates(
#     subset=['player', 'season'], keep='first')
# radar_plot(
#     totals_df=merged_df,
#     stats_to_graph=stats_to_graph,
#     player_name=player_name,
#     team_info=team_info,
#     season=2020,
#     cols=[
#         'BLK%',
#         'DRB%',
#         'ORB%',
#         '2PA/G',
#         '2P%',
#         'FTA/G',
#         'FT%',
#         '3PA/G',
#         '3P%',
#         'TOV%',
#         'USG%',
#         'AST%',
#         'PF/G',
#         'STL%',
#     ],
#     pct_cols=[
#         'TS%',
#         '3PAr',
#         'FTr',
#     ],
#     inverse_cols=[
#         'TOV%',
#         'PF/G',
#     ],
#     fig=fig,
# )
# plt.savefig(f'./output/draft-radars/{player_name} Draft.png')
