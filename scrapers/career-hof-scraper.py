from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import time

letters = [
  'a',
  # 'b',
  # 'c',
  # 'd',
  # 'e',
  # 'f',
  # 'g',
  # 'h',
  # 'i',
  # 'j',
  # 'k',
  # 'l',
  # 'm',
  # 'n',
  # 'o',
  # 'p',
  # 'q',
  # 'r',
  # 's',
  # 't',
  # 'u',
  # 'v',
  # 'w',
  # 'x',
  # 'y',
  # 'z'
]
awards = [
  'All Star',
  'Scoring Champ',
  'TRB Champ',
  'BLK Champ',
  'NBA Champ',
  'All-NBA',
  'All-Defensive',
  'All-Rookie',
  'Finals MVP',
  'MVP',
  'ROY'
]
players_df = pd.DataFrame()
for letter in letters:
  url = (f"https://www.basketball-reference.com/players/{letter}")
  req = requests.get(url)
  soup = BeautifulSoup(req.content, "html.parser")
  links = soup.find_all('a', href=lambda value: value and value.startswith(f"/players/{letter}"))
  links = [links[2]]
  for link in links:
    boxurl = "https://www.basketball-reference.com" + link['href']
    print(boxurl)
    player_req = requests.get(boxurl)
    player_soup = BeautifulSoup(player_req.content, 'html.parser')
    # all_stars = player_soup.find_all('span', class_='sr_star')
    # print(len(all_stars))
    bling = player_soup.find('ul', id='bling')
    bling_items = bling.find_all('li')
    for bling_item in bling_items:
      bling_text = bling_item.get_text()
      if (bling_text != 'Hall of Fame'):
        split_item = bling_text.split(' ', 1)
        award = split_item[1]
        qualifier = split_item[0]
        quantity = 0
        if ('x' in qualifier):
          quantity = qualifier.split('x')[0]
        else:
          quantity = 1
        awards.append(award)
        print(quantity)
      else:
        print('Hall of Famer')
print(awards)
      

    
