import pandas as pd
from scipy.stats import betabinom, norm, yeojohnson
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score, train_test_split

df = pd.read_csv('./data/draft/blocks.csv')
torvik_df = pd.read_csv('./data/torvik.csv')
torvik_df = torvik_df[torvik_df['Season'] > 2009]
torvik_df_player_grouped = torvik_df.groupby(['Name', 'PlayerID'])
torvik_df.loc[torvik_df['2PA'].isnull(), '2PA'] = 0
torvik_df.loc[torvik_df['3PA'].isnull(), '3PA'] = 0
torvik_df.loc[torvik_df['FTA'].isnull(), 'FTA'] = 0
torvik_df.loc[torvik_df['Far2'].isnull(), 'Far2'] = 0
torvik_df.loc[torvik_df['Far2A'].isnull(), 'Far2A'] = 0
torvik_df.loc[torvik_df['3P'].isnull(), '3P'] = 0
torvik_df.loc[torvik_df['FT'].isnull(), 'FT'] = 0
torvik_df['FGA'] = torvik_df['2PA'] + torvik_df['3PA']
torvik_df['FG'] = torvik_df['2P'] + torvik_df['3P']
torvik_df = torvik_df[torvik_df['Height'].notnull()]
torvik_df = torvik_df[torvik_df['Height'] != '-']
torvik_df = torvik_df[~torvik_df['Height'].str.contains("'")]
torvik_df = torvik_df[torvik_df['Height'].str.contains('5|6|7')]
torvik_df['Height_Split'] = torvik_df['Height'].str.split('-')
torvik_df['Feet'] = torvik_df['Height_Split'].str[0]
torvik_df['Inches'] = torvik_df['Height_Split'].str[1]
torvik_df['Height_Inches'] = torvik_df['Height_Split'].str[0].astype(int)*12 + torvik_df['Height_Split'].str[1].astype(int)
torvik_df.loc[torvik_df['Role'] == 'Pure PG', 'Role'] = 1
torvik_df.loc[torvik_df['Role'] == 'Scoring PG', 'Role'] = 1
torvik_df.loc[torvik_df['Role'] == 'Combo G', 'Role'] = 1
torvik_df.loc[torvik_df['Role'] == 'Wing G', 'Role'] = 2
torvik_df.loc[torvik_df['Role'] == 'Wing F', 'Role'] = 2
torvik_df.loc[torvik_df['Role'] == 'Stretch 4', 'Role'] = 2
torvik_df.loc[torvik_df['Role'] == 'PF/C', 'Role'] = 3
torvik_df.loc[torvik_df['Role'] == 'C', 'Role'] = 3
for col in []:
  torvik_df[f'{col}_pctile'] = torvik_df[col].rank(pct=True)
for col in ['Height_Inches', 'BLK%', 'STL%']:
  torvik_df[f'{col}_pctile'] = torvik_df.groupby('Role')[col].rank(pct=True)
# career_df_sums = torvik_df_player_grouped.sum().loc[:,['3PA', '3P', 'Far2', 'Far2A', 'FGA', 'FT', 'FTA', 'BLK']]
# career_df_min = torvik_df_player_grouped['Season'].min()
# career_df_max = torvik_df_player_grouped['Season'].max()
# career_df = career_df_sums.join(career_df_min)
last_year_only = torvik_df.sort_values('Season', ascending=False).drop_duplicates(['Name', 'PlayerID'])
merged_df = pd.merge(df, last_year_only, how='inner', left_on='player', right_on='Name')
# merged_df = merged_df[merged_df['mp'] >= 200]
merged_df.loc[merged_df['Role'] == 3,['Name', 'BLK%_pctile', 'STL%_pctile', 'Height_Inches_pctile', 'blk_pct']].to_csv('blocks_model.csv')

continuous_vs = ['BLK%','STL%', 'Height_Inches']
discrete_vs = ['Role']
model_cols = continuous_vs + discrete_vs
X = merged_df.loc[:,model_cols]
y = merged_df['blk_pct']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
draft_class = last_year_only[last_year_only['Season'] == 2020]
draft_class = draft_class[(draft_class['Role'].notnull()) & (draft_class['Min%'] >= 40)]
draft_class_X = draft_class.loc[:,model_cols]
for v in continuous_vs:
  X_train[v], l = yeojohnson(X_train[v])
  # print(v)
  # print(l)
  draft_class_X[v] = yeojohnson(draft_class_X[v], l)
  X_test[v] = yeojohnson(X_test[v], l)
  X[v] = yeojohnson(X[v], l)
reg = LinearRegression().fit(X_train,y_train)
print(reg.score(X_test,y_test))
print(reg.coef_)
shotblockers_df = draft_class[
  (draft_class['BLK%_pctile'] >= .9) & 
  (draft_class['STL%_pctile'] >= .5) & 
  # (draft_class['Height_Inches_pctile'] >= .5) &
  (draft_class['Role'] == 3)
]
draft_class['pred_blk%'] = reg.predict(draft_class_X)
print(draft_class[draft_class['Name'] == 'Udoka Azubuike'])
print(draft_class.nlargest(30, 'pred_blk%').loc[:,['Name', 'pred_blk%']])

print(shotblockers_df.shape)
shotblockers_df.loc[:, ['Name', 'BLK%_pctile', 'BLK%', 'STL%_pctile', 'STL%', 'Height_Inches']].to_csv('shotblockers.csv')
