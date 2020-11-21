import pandas as pd
from radar_plot import radar_plot
import matplotlib.pyplot as plt

def safe_divide(a, b):
  if (b == 0):
    return 0
  else:
    return a/b

torvik_df = pd.read_csv('./data/torvik.csv')
# torvik_df = torvik_df[torvik_df['Min%'] >= 40]
# torvik_df['Assist%_percentile'] = torvik_df['Assist%'].rank(pct=True)
# torvik_df = torvik_df[torvik_df['Role'].isin(['PF/C', 'C'])]
# nba_df = pd.read_csv('./data/draft/ncaa-totals-2006-07.csv')
# nba_df = nba_df[nba_df['NBA_g'] > 0]
# merged_df = pd.merge(torvik_df, nba_df, left_on=['Name', 'Season'], right_on=['player', 'year_max'])
# merged_df = merged_df[merged_df['NBA_g'].notnull()]
# merged_df['NBA_min'] = merged_df['NBA_mp_per_g'] * merged_df['NBA_g']
# merged_df = merged_df[merged_df['NBA_min'] >= 100]
# merged_df['Name'].to_csv('./data/centers.csv')
# draft_rankings_df = pd.read_csv('./data/draft/draft_rankings.csv')
# early_entrants_df = pd.read_csv('./data/draft/early-entrants.csv')
# df_2020 = torvik_df[torvik_df['Season'] == 2020]
# draft_class = pd.merge(df_2020, draft_rankings_df, how='inner', left_on='Name', right_on='Name')
# print(draft_class.nlargest(30, 'Assist%_percentile').loc[:,['Name', 'Assist%', 'Assist%_percentile']])
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
player_name = 'Patrick Williams'
college_df = pd.read_csv('./data/college_team_colors.csv')
team_info = college_df[college_df['Team'] == 'FSU'].squeeze()
fig = plt.figure(dpi=250)
# advanced_stats_df = pd.read_csv('./data/nba_advanced.csv')
# totals_df = pd.read_csv('./data/nba_per_game.csv')
# merged_df = advanced_stats_df.merge(
#     totals_df, on=['player', 'team_id', 'season'])
torvik_df.loc[torvik_df['2PA'].isnull(), '2PA'] = 0
torvik_df.loc[torvik_df['3PA'].isnull(), '3PA'] = 0
torvik_df.loc[torvik_df['FTA'].isnull(), 'FTA'] = 0
torvik_df.loc[torvik_df['Far2'].isnull(), 'Far2'] = 0
torvik_df.loc[torvik_df['Far2A'].isnull(), 'Far2A'] = 0
torvik_df.loc[torvik_df['3P'].isnull(), '3P'] = 0
torvik_df.loc[torvik_df['FT'].isnull(), 'FT'] = 0
torvik_df.loc[torvik_df['G'].isnull(), 'G'] = 0
torvik_df.loc[torvik_df['Min%'].isnull(), 'Min%'] = 0
torvik_df['Min'] = torvik_df['Min%'] / 100 * torvik_df['G'] * 40
torvik_df['FGA'] = torvik_df['2PA'] + torvik_df['3PA']
torvik_df['FG'] = torvik_df['2P'] + torvik_df['3P']
torvik_df['3PAR'] = torvik_df.apply(lambda row: safe_divide(row['3PA'], row['FGA']), axis=1)
torvik_df['3P%'] = torvik_df.apply(lambda row: safe_divide(row['3P'], row['3PA']), axis=1)
torvik_df['2P%'] = torvik_df.apply(lambda row: safe_divide(row['2P'], row['2PA']), axis=1)
torvik_df['Close2%'] = torvik_df.apply(lambda row: safe_divide(row['Close2'], row['Close2A']), axis=1)
torvik_df['Far2%'] = torvik_df.apply(lambda row: safe_divide(row['Far2'], row['Far2A']), axis=1)
torvik_df['FT%'] = torvik_df.apply(lambda row: safe_divide(row['FT'], row['FTA']), axis=1)
torvik_df['FTR'] = torvik_df.apply(lambda row: safe_divide(row['FTA'], row['FGA']), axis=1)
torvik_df['Close2A/G'] = torvik_df.apply(lambda row: safe_divide(row['Close2A'], row['G']), axis=1)
torvik_df['FTA/G'] = torvik_df.apply(lambda row: safe_divide(row['FTA'], row['G']), axis=1)
torvik_df['Far2A/G'] = torvik_df.apply(lambda row: safe_divide(row['Far2A'], row['G']), axis=1)
torvik_df['3PA/G'] = torvik_df.apply(lambda row: safe_divide(row['3PA'], row['G']), axis=1)
torvik_df['Close2A/Min'] = torvik_df.apply(lambda row: safe_divide(row['Close2A'], row['Min']), axis=1)
torvik_df['FTA/Min'] = torvik_df.apply(lambda row: safe_divide(row['FTA'], row['Min']), axis=1)
torvik_df['Far2A/Min'] = torvik_df.apply(lambda row: safe_divide(row['Far2A'], row['Min']), axis=1)
torvik_df['3PA/Min'] = torvik_df.apply(lambda row: safe_divide(row['3PA'], row['Min']), axis=1)
torvik_df['Close2A/40'] = torvik_df['Close2A/Min'] * 40
torvik_df['Far2A/40'] = torvik_df['Far2A/Min'] * 40
torvik_df['FTA/40'] = torvik_df['FTA/Min'] * 40
torvik_df['3PA/40'] = torvik_df['3PA/Min'] * 40
stats_to_graph = torvik_df[(torvik_df['Name'] == player_name) & (torvik_df['Season'] == 2020)].squeeze()
# merged_df = merged_df.drop_duplicates(
#     subset=['player', 'season'], keep='first')
torvik_df = torvik_df[torvik_df['Min%'] >= 40]
print(torvik_df['Role'].unique())
torvik_df = torvik_df[torvik_df['Role'].isin(['Stretch 4', 'Wing F', 'Wing G'])]
radar_plot(
    totals_df=torvik_df,
    stats_to_graph=stats_to_graph,
    player_name=player_name,
    team_info=team_info,
    season=2020,
    label_font_size=8,
    cols=[
        'BLK%',
        'DR%',
        'OR%',
        'Close2A/40',
        'Close2%',
        'Far2A/40',
        'Far2%',
        'FTA/40',
        'FT%',
        '3PA/40',
        '3P%',
        'TO%',
        'USG',
        'Assist%',
        'Fouls/40',
        'STL%',
    ],
    pct_cols=[
        'Far2%',
        'Close2%',
        'FT%',
        '3P%',
    ],
    inverse_cols=[
        'TO%',
        'Fouls/40',
    ],
    fig=fig,
)
plt.savefig(f'./output/draft-radars/{player_name} Draft.png')
