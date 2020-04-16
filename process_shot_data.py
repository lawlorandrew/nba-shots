import json
import pandas as pd

files = [
  './data/team_shot_data/bucks_shots.json',
  './data/team_shot_data/bulls_shots.json',
  './data/team_shot_data/celtics_shots.json',
  './data/team_shot_data/heat_shots.json',
  './data/team_shot_data/jazz_shots.json',
  './data/team_shot_data/lakers_shots.json',
  './data/team_shot_data/magic_shots.json',
  './data/team_shot_data/mavericks_shots.json',
  './data/team_shot_data/pacers_shots.json',
  './data/team_shot_data/pistons_shots.json',
  './data/team_shot_data/raptors_shots.json',
  './data/team_shot_data/rockets_shots.json',
  './data/team_shot_data/warriors_shots.json',
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
  all_shots_df.to_csv('./data/all_shots.csv', index=False)
