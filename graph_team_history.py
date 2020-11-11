import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import math

def graph_team_history():
  history_df = pd.read_csv('./data/pistons_history.csv')
  history_df = history_df[history_df['Season'] >= '2009-10']
  history_df.loc[history_df['Playoffs'].str.contains('Lost'), 'Playoffs'] = 'Playoffs'
  history_df.loc[history_df['Playoffs'].str.contains('Won'), 'Playoffs'] = 'Title'
  fig, ax = plt.subplots()
  # ax.plot(history_df['Season'], history_df['Rel ORtg'], c='#C8102E', label='Relative Offensive Rating')
  # ax.plot(history_df['Season'], history_df['Rel DRtg']*-1, c='#1d428a', label='Relative Defensive Rating')
  ax.plot(history_df['Season'], history_df['SRS'], c='#C8102E')
  # for index, row in history_df.iterrows():
  #   if (row['Playoffs'] == row['Playoffs']):
  #     ax.text(
  #       s=row['Playoffs'],
  #       x=row['Season'],
  #       y=row['SRS']
  #     )
  ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
  ax.set_xlim('2009-10', '2019-20')
  ax.set_ylim(-10, 10)
  ax.spines['top'].set_visible(False)
  ax.spines['right'].set_visible(False)
  ax.set_title('Detroit Pistons')
  ax.set_xlabel('Season')
  ax.set_ylabel('Net Rating')
  ax.axhline(0, color='#000000', ls='dotted')
  # ax.legend()
  plt.savefig(f'output/Detroit Pistons Team History.png')
  plt.close()

graph_team_history()