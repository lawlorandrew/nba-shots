from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import time

offset = 0
totals_df = pd.DataFrame()
table_exists = True

while (table_exists is True):
  try:
    # url = f"https://www.sports-reference.com/cbb/play-index/psl_finder.cgi?request=1&match=single&year_min=2007&year_max=&conf_id=&school_id=&class_is_fr=Y&class_is_so=Y&class_is_jr=Y&class_is_sr=Y&pos_is_g=Y&pos_is_f=Y&pos_is_c=Y&games_type=A&qual=&c1stat=&c1comp=&c1val=&c2stat=&c2comp=&c2val=&c3stat=&c3comp=&c3val=&c4stat=&c4comp=&c4val=&order_by=pts&order_by_asc=&offset={offset}"
    url = f"https://www.sports-reference.com/cbb/play-index/psl_finder.cgi?request=1&match=single&year_min=2020&year_max=2020&conf_id=&school_id=&class_is_fr=&class_is_so=&class_is_jr=&class_is_sr=Y&pos_is_g=Y&pos_is_f=Y&pos_is_c=Y&games_type=A&qual=&c1stat=&c1comp=&c1val=&c2stat=&c2comp=&c2val=&c3stat=&c3comp=&c3val=&c4stat=&c4comp=&c4val=&order_by=pts&order_by_asc=&offset={offset}"
    req = requests.get(url)
    print(offset)
    soup = BeautifulSoup(req.content, "html.parser")
    table = soup.find('table', id='stats')
    table_exists = table is not None
    if (table_exists):
      rows = soup.find('tbody').find_all('tr', class_=lambda x: x is None)
      stats_df = pd.DataFrame()
      for row in rows:
        row_data = pd.Series()
        name = row.find('td', {"data-stat":"player"}).get_text()
        row_data['Name'] = name
        stats_df = stats_df.append(row_data, ignore_index=True)
      offset += 100
      totals_df = totals_df.append(stats_df, ignore_index=True)
      time.sleep(2)
  except ConnectionError:
    print('connection error, waiting 20s and trying again')
    time.sleep(20)
totals_df.to_csv(f'./data/draft/seniors.csv')
