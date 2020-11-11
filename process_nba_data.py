import json
import pandas as pd  

# playtypes = ['pnr_bh', 'pnr_roll', 'transition', 'postup', 'isolation', 'spotup', 'handoff', 'cut', 'offscreen']
# seasontypes = ['reg', 'playoff']
# total_df = pd.DataFrame()
# for seasontype in seasontypes:
#   for playtype in playtypes:
#     with open(f'./data/playtypes/{playtype}_{seasontype}_2020.json') as jsonFile:
#       data = json.load(jsonFile)
#       headers = data['resultSets'][0]['headers']
#       stats = data['resultSets'][0]['rowSet']
#       stats_df = pd.DataFrame(stats, columns=headers)
#       stats_df['SEASON_TYPE'] = seasontype
#       stats_df['PLAY_TYPE'] = playtype
#       total_df = total_df.append(stats_df)
# total_df.to_csv('./data/playtypes.csv')

with open(f'data/nba_shooting_by_range.json') as jsonFile:
  data = json.load(jsonFile)
  headers = data['resultSets']['headers']
  ranges = headers[0]['columnNames']
  print(headers[1]['columnNames'][5:])
  stats = data['resultSets']['rowSet']
  columns = headers[1]['columnNames'][:5]
  print(columns)
  for shot_range in ranges:
    for stat in ['FGM', 'FGA', 'FG_PCT']:
      columns.append(f'{shot_range}_{stat}')

  stats_df = pd.DataFrame(stats, columns=columns)
  stats_df.to_csv('./data/nba_shooting_by_range.csv')