import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

mock_drafts_df = pd.read_csv('./data/draft/draft_projections.csv')
team_colors_df = pd.read_csv('./data/nba_team_colors.csv')
mock_drafts_df = pd.merge(mock_drafts_df, team_colors_df, left_on='Team', right_on='Team')
drafts = ['Ringer-KOC', 'Vecenie-The Athletic', 'Peek-Yahoo',
       'Woo-SI', 'O’Donnell-SB Nation', 'Parrish-CBS Sports', 'Givony-ESPN',
       'Wasserman-Bleacher Report', 'Tankathon', 'Netscouts']

fig, axs = plt.subplots(6, 5, sharey=True, figsize=(8,8))
fig.tight_layout(rect=[0, 0.03, 1, 0.95], w_pad=1.5, h_pad=3.5)
fig.suptitle('NBA Composite Mock Draft 10/15 | @lawlorpalooza')
for index, row in mock_drafts_df.iterrows():
  labels, values = zip(*Counter(row.loc[drafts].values.tolist()).most_common())
  labels = [f'{label.split(" ")[1]}' for label in labels]
  indexes = np.arange(len(labels))
  figrow = (row['Pick'] - 1) // 5
  figcol = (row['Pick'] - 1) % 5
  # print(row['Pick'])
  # print(figrow)
  # print(figcol)
  width = 0.5
  axs[figrow, figcol].bar(indexes, values, width, color=row["Primary"])
  axs[figrow, figcol].set_title(f'{row["Pick"]} - {row["Team"]}', fontsize=12)
  axs[figrow, figcol].set_xticks(indexes)
  axs[figrow, figcol].set_yticks([])
  axs[figrow, figcol].xaxis.labelpad = 0
  axs[figrow, figcol].set_xticklabels(labels, rotation=60, fontdict={'fontsize': 6})
# fig.text(
#   x=0.5,
#   y=0.95,
#   s='@lawlorpalooza',
#   horizontalalignment='center',
#   verticalalignment='bottom',
#   fontsize=6,
#   style='italic'
# )
fig.text(
  x=0.01,
  y=0.01,
  s='Mock Drafts by Kevin O\'Connor, Sam Vecenie, Krysten Peek, Jeremy Woo, Ricky O\'Donnell, Gary Parrish, Jonathan Givony, Jonathan Wasserman, Tankathon, Netscouts',
  horizontalalignment='left',
  verticalalignment='bottom',
  fontsize=6,
  style='italic'
)
plt.savefig('./output/Mock Drafts 2020.png')