import json
import pandas as pd

team_colors_df = pd.read_csv('./data/nba_team_colors.csv')

def get_opponent(row):
  team_short = team_colors_df.loc[team_colors_df['Full'] == row['TEAM_NAME'], 'NBA_Abbr'].squeeze()
  if (row['HTM'] == team_short):
    opp = row['VTM']
  elif (row['VTM'] == team_short):
    opp = row['HTM']
  else:
    print(team_short)
    print(row['VTM'])
    print(row['HTM'])
    return ''
  opponent_full = team_colors_df.loc[team_colors_df['NBA_Abbr'] == opp, 'Full'].squeeze()
  return opponent_full

files = [
  './data/team_shot_data/76ers_shots.json',
  './data/team_shot_data/blazers_shots.json',
  './data/team_shot_data/bucks_shots.json',
  './data/team_shot_data/bulls_shots.json',
  './data/team_shot_data/cavs_shots.json',
  './data/team_shot_data/celtics_shots.json',
  './data/team_shot_data/clippers_shots.json',
  './data/team_shot_data/grizzlies_shots.json',
  './data/team_shot_data/hawks_shots.json',
  './data/team_shot_data/heat_shots.json',
  './data/team_shot_data/hornets_shots.json',
  './data/team_shot_data/jazz_shots.json',
  './data/team_shot_data/kings_shots.json',
  './data/team_shot_data/knicks_shots.json',
  './data/team_shot_data/lakers_shots.json',
  './data/team_shot_data/magic_shots.json',
  './data/team_shot_data/mavericks_shots.json',
  './data/team_shot_data/nets_shots.json',
  './data/team_shot_data/nuggets_shots.json',
  './data/team_shot_data/pacers_shots.json',
  './data/team_shot_data/pelicans_shots.json',
  './data/team_shot_data/pistons_shots.json',
  './data/team_shot_data/raptors_shots.json',
  './data/team_shot_data/rockets_shots.json',
  './data/team_shot_data/suns_shots.json',
  './data/team_shot_data/spurs_shots.json',
  './data/team_shot_data/thunder_shots.json',
  './data/team_shot_data/timberwolves_shots.json',
  './data/team_shot_data/warriors_shots.json',
  './data/team_shot_data/wizards_shots.json',
]
all_shots_df = None
for file in files:
  with open(file) as jsonFile:
    data = json.load(jsonFile)
    headers = data['resultSets'][0]['headers']
    shots = data['resultSets'][0]['rowSet']
    team_shot_df = pd.DataFrame(shots, columns=headers)
    if (all_shots_df is None):
      all_shots_df = pd.DataFrame(team_shot_df)
    else:
      all_shots_df = all_shots_df.append(team_shot_df)
teams_shot_type_df = pd.DataFrame([])
teams_shot_zone_df = pd.DataFrame([])
team_opps_shot_type_df = pd.DataFrame([])
team_opps_shot_zone_df = pd.DataFrame([])
all_shots_df['OPPONENT'] = all_shots_df.apply(get_opponent, axis=1)
all_shots_df.to_csv('./data/all_shots.csv', index=False)

for val in all_shots_df['SHOT_TYPE'].unique():
  grouped = all_shots_df.loc[all_shots_df['SHOT_TYPE'] == val].groupby('TEAM_NAME').sum()
  teams_shot_type_df[f'{val} Made'] = grouped['SHOT_MADE_FLAG']
  teams_shot_type_df[f'{val} Attempted'] = grouped['SHOT_ATTEMPTED_FLAG']
  teams_shot_type_df[f'{val}%'] = teams_shot_type_df[f'{val} Made'] / teams_shot_type_df[f'{val} Attempted']
  opponent_grouped = all_shots_df.loc[all_shots_df['SHOT_TYPE'] == val].groupby('OPPONENT').sum()
  team_opps_shot_type_df[f'Opponent {val} Made'] = opponent_grouped['SHOT_MADE_FLAG']
  team_opps_shot_type_df[f'Opponent {val} Attempted'] = opponent_grouped['SHOT_ATTEMPTED_FLAG']
  team_opps_shot_type_df[f'Opponent {val}%'] = team_opps_shot_type_df[f'Opponent {val} Made'] / team_opps_shot_type_df[f'Opponent {val} Attempted']

for val in all_shots_df['SHOT_ZONE_BASIC'].unique():
  grouped = all_shots_df.loc[all_shots_df['SHOT_ZONE_BASIC'] == val].groupby('TEAM_NAME').sum()
  teams_shot_zone_df[f'{val} Made'] = grouped['SHOT_MADE_FLAG']
  teams_shot_zone_df[f'{val} Attempted'] = grouped['SHOT_ATTEMPTED_FLAG']
  teams_shot_zone_df[f'{val}%'] = teams_shot_zone_df[f'{val} Made'] / teams_shot_zone_df[f'{val} Attempted']
  opponent_grouped = all_shots_df.loc[all_shots_df['SHOT_ZONE_BASIC'] == val].groupby('OPPONENT').sum()
  team_opps_shot_zone_df[f'Opponent {val} Made'] = opponent_grouped['SHOT_MADE_FLAG']
  team_opps_shot_zone_df[f'Opponent {val} Attempted'] = opponent_grouped['SHOT_ATTEMPTED_FLAG']
  team_opps_shot_zone_df[f'Opponent {val}%'] = team_opps_shot_zone_df[f'Opponent {val} Made'] / team_opps_shot_zone_df[f'Opponent {val} Attempted']
team_shots_df = teams_shot_zone_df.join(teams_shot_type_df)
opponent_shots_df = team_opps_shot_zone_df.join(team_opps_shot_type_df)
teams_df = team_shots_df.join(opponent_shots_df)
teams_df.to_csv('./data/team_stats_from_shot_data.csv')