import json
import pandas as pd  

with open(f'./data/tracking/post_ups.json') as jsonFile:
  data = json.load(jsonFile)
  headers = data['resultSets'][0]['headers']
  stats = data['resultSets'][0]['rowSet']
  stats_df = pd.DataFrame(stats, columns=headers)
  stats_df.to_csv(f'./data/tracking/post_ups.csv')