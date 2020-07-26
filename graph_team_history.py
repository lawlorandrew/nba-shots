import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

def graph_team_history():
  history_df = pd.read_csv('./data/pistons_history.csv')
  fig, ax = plt.subplots()
  ax.plot(history_df['Season'], history_df['Rel ORtg'], c='#C8102E', label='Relative Offensive Rating')
  ax.plot(history_df['Season'], history_df['Rel DRtg']*-1, c='#1d428a', label='Relative Defensive Rating')
  ax.plot(history_df['Season'], history_df['SRS'], c='#bec0c2', label='Overall SRS')
  ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
  ax.set_xlim('1969-70', '2019-20')
  ax.spines['top'].set_visible(False)
  ax.spines['right'].set_visible(False)
  ax.set_title('Detroit Pistons Team History')
  ax.axhline(0, color='#000000', ls='dotted')
  ax.legend()
  plt.savefig(f'output/Detroit Pistons Team History.png')
  plt.close()

graph_team_history()