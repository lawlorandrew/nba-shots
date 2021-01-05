from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import time

years = [
  '2021',
  # '2020',
  # '2019',
  # '2018',
  # '2017',
  # '2016',
  # '2015',
  # '2014',
  # '2013',
  # '2012',
  # '2011',
  # '2010'
]
months = [
  # 'october',
  # 'november',
  'december',
  'january',
  'february',
  'march',
  # 'april',
  # 'may',
  # 'june',
  # 'july',
  # 'august',
  # 'september'
]
for year in years:
  totals_df = pd.DataFrame()
  for month in months:
    url = (f"https://www.basketball-reference.com/leagues/NBA_{year}_games-{month}.html")
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    body = soup.find('tbody')
    if (body):
      rows = body.find_all('tr', class_=lambda x: x is None)
      for row in rows:
        row_data = pd.Series()
        tds = row.find_all('td')
        for td in tds:
          row_data[td['data-stat']] = td.get_text()
        date_el = row.find('th')
        row_data['game_date'] = date_el.get_text()
        totals_df = totals_df.append(row_data, ignore_index=True)
      # links = soup.find_all('a', href=lambda value: value and value.startswith("/boxscores/20"))
      # # links = [links[0]]
      # for link in links:
      #   boxurl = "https://www.basketball-reference.com" + link['href']
      #   print(boxurl)
      #   boxreq = requests.get(boxurl)
      #   boxsoup = BeautifulSoup(boxreq.content, 'html.parser')
      #   game_date = link['href'][11:19]
      #   regex = re.compile("box-(.*?)-game-basic")
      #   boxscores = boxsoup.find_all("table", id=regex)
      #   stats_df = pd.DataFrame(columns=stats)
      #   teams = []
      #   togpattern = re.compile(r'Time of Game:(.*?)')
      #   tog_header = boxsoup.find('strong', string=togpattern)
      #   tog = ''
      #   if tog_header:
      #     tog_raw = boxsoup.find('strong', string=togpattern).parent.get_text()
      #     if tog_raw:
      #       tog = tog_raw[14:]
      #   for boxscore in boxscores:
      #     stats_series = pd.Series(index=stats)
      #     teams.append(boxscore.get('id')[4:7])
      #     footer = boxscore.find('tfoot')
      #     for stat in stats:
      #       stats_series[stat] = footer.find('td', { 'data-stat': stat }).get_text()
      #     stats_df = stats_df.append(stats_series, ignore_index=True)
      #   for index in [0,1]:
      #     stats_df.loc[index,'Team'] = teams[index]
      #     stats_df.loc[index,'Opponent'] = teams[1-index]
      #     stats_df['Date'] = game_date
      #     stats_df['Time of Game'] = tog
      #     for stat in stats:
      #       stats_df.loc[index, f'Opponent {stat}'] = stats_df.loc[1-index, stat].squeeze()
      #   all_stats_df = all_stats_df.append(stats_df)
      time.sleep(1)
  # totals_df = totals_df[(totals_df['visitor_pts'].notnull()) & (totals_df['visitor_pts'] != '')]
  totals_df = totals_df.reset_index()
  totals_df = totals_df.drop(['index'], axis=1)
  if (year == '2020'):
    totals_df['playoffs'] = 'N'
    totals_df.loc[totals_df.index > 1063, 'playoffs'] = 'Y'
  else:
    totals_df['playoffs'] = 'N'
    totals_df.loc[totals_df.index > 1230, 'playoffs'] = 'Y'
  totals_df.to_csv(f'./data/scores_{year}.csv')
