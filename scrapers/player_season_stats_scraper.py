from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import time

seasons = [
  2012,
  2013,
  2014,
  2015,
  2016,
  2017,
  2018,
  2019,
  2020
]
stat_classifications = [
  'per_poss',
  'advanced',
  'per_game'
]
for stat_classification in stat_classifications:
  total_df = pd.DataFrame()
  for season in seasons:
    print(season)
    print(stat_classification)
    url = f'https://www.basketball-reference.com/leagues/NBA_{season}_{stat_classification}.html'
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    full_rows = soup.find_all('tr', class_='full_table')
    partial_rows = soup.find_all('tr', class_='partial_table')
    rows = full_rows + partial_rows
    stats_df = pd.DataFrame()
    for row in rows:
      row_data = pd.Series()
      tds = row.find_all('td')
      for td in tds:
        row_data[td['data-stat']] = td.get_text()
      stats_df = stats_df.append(row_data, ignore_index=True)
    stats_df['season'] = season
    total_df = total_df.append(stats_df)
  total_df.to_csv(f'./data/nba_{stat_classification}.csv')
