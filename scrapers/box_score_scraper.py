from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import time

months = [
  # 'october',
  # 'november',
  # 'december',
  # 'january',
  # 'february',
  # 'march',
  # 'july',
  'august'
]
for month in months:
  stats = ['fg', 'fga', 'fg3', 'fg3a', 'ft', 'fta', 'tov', 'pts', 'orb', 'drb', 'pf']
  all_stats_df = pd.DataFrame(columns=stats)
  url = (f"https://www.basketball-reference.com/leagues/NBA_2020_games-{month}.html")
  req = requests.get(url)
  soup = BeautifulSoup(req.content, "html.parser")
  links = soup.find_all('a', href=lambda value: value and value.startswith("/boxscores/20"))
  # links = [links[0]]
  for link in links:
    boxurl = "https://www.basketball-reference.com" + link['href']
    print(boxurl)
    boxreq = requests.get(boxurl)
    boxsoup = BeautifulSoup(boxreq.content, 'html.parser')
    game_date = link['href'][11:19]
    regex = re.compile("box-(.*?)-game-basic")
    boxscores = boxsoup.find_all("table", id=regex)
    stats_df = pd.DataFrame(columns=stats)
    teams = []
    togpattern = re.compile(r'Time of Game:(.*?)')
    tog_header = boxsoup.find('strong', string=togpattern)
    tog = ''
    if tog_header:
      tog_raw = boxsoup.find('strong', string=togpattern).parent.get_text()
      if tog_raw:
        tog = tog_raw[14:]
    for boxscore in boxscores:
      stats_series = pd.Series(index=stats)
      teams.append(boxscore.get('id')[4:7])
      footer = boxscore.find('tfoot')
      for stat in stats:
        stats_series[stat] = footer.find('td', { 'data-stat': stat }).get_text()
      stats_df = stats_df.append(stats_series, ignore_index=True)
    for index in [0,1]:
      stats_df.loc[index,'Team'] = teams[index]
      stats_df.loc[index,'Opponent'] = teams[1-index]
      stats_df['Date'] = game_date
      stats_df['Time of Game'] = tog
      for stat in stats:
        stats_df.loc[index, f'Opponent {stat}'] = stats_df.loc[1-index, stat].squeeze()
    all_stats_df = all_stats_df.append(stats_df)
    time.sleep(1)
  print(all_stats_df)
  all_stats_df.to_csv(f'./data/box_score_totals-{month}.csv')
