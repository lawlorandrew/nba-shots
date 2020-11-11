from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import time

offset = 0
totals_df = pd.DataFrame()
table_exists = True
cookies = { 'stathead_user': 'alawlor%3A%3Aalawlor%3A%3A3c2890b7208ed003bfacc2fac6001f04%3A%3A36190334' }

while (table_exists is True):
  try:
    url = f'https://stathead.com/basketball/psl_finder.cgi?request=1&lg_id=NBA&order_by=blk_pct&season_start=1&is_playoffs=N&as_val=0&per_poss_base=100&order_by_asc=0&as_comp=gt&year_min=2011&birth_country_is=Y&height_max=99&match=combined&per_minute_base=36&height_min=0&season_end=-1&age_min=0&age_max=99&college_id=0&positions[]=G&positions[]=GF&positions[]=F&positions[]=FG&positions[]=FC&positions[]=C&positions[]=CF&type=totals&offset={offset}'
    req = requests.get(url, cookies=cookies)
    print(offset)
    soup = BeautifulSoup(req.content, "html.parser")
    table = soup.find('table', id='stats')
    table_exists = table is not None
    if (table_exists):
      rows = soup.find('tbody').find_all('tr', class_=lambda x: x is None)
      stats_df = pd.DataFrame()
      for row in rows:
        row_data = pd.Series()
        tds = row.find_all('td')
        for td in tds:
          row_data[td['data-stat']] = td.get_text()
        stats_df = stats_df.append(row_data, ignore_index=True)
      offset += 100
      totals_df = totals_df.append(stats_df, ignore_index=True)
      time.sleep(2)
  except ConnectionError:
    print('connection error, waiting 20s and trying again')
    time.sleep(20)
totals_df.to_csv(f'./data/draft/blocks.csv')
