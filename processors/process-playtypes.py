import json
import pandas as pd  

playtypes = ['pnr_bh', 'pnr_roll', 'transition', 'post_up', 'isolation', 'spot_up', 'handoff', 'cut', 'off_screen', 'misc']
labels = ['P&R Ball-Handler', 'P&R Roller', 'Transition', 'Post Up', 'Iso', 'Spot Up', 'Handoff', 'Cut', 'Off Screen']
colors = ['blue', 'red', 'green', 'yellow', 'orange', 'white', 'purple', 'navy', 'brown', 'cyan']
folder = 'team_playtypes'
subfolder = 'offense'
total_df = pd.DataFrame()
for (playtype,color,label) in zip(playtypes, colors, labels):
  with open(f'./data/lakers_heat/{folder}/{subfolder}/{playtype}.json') as jsonFile:
    data = json.load(jsonFile)
    headers = data['resultSets'][0]['headers']
    stats = data['resultSets'][0]['rowSet']
    stats_df = pd.DataFrame(stats, columns=headers)
    stats_df['PLAY_TYPE'] = playtype
    stats_df['Primary'] = color
    stats_df['label'] = label
    total_df = total_df.append(stats_df)
total_df.to_csv(f'./data/lakers_heat/{folder}/{subfolder}/total.csv')