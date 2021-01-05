from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.pyplot as plt
import numpy as np

def big_men_passing(df, xcol, ycol, xlabel, ylabel, title, subtitle):
  fig, ax = plt.subplots(dpi=500, figsize=(10,6))
  ax.set_ylabel(ylabel)
  ax.set_xlabel(xlabel)
  fig.tight_layout(rect=[0, 0.03, 1, 0.95], w_pad=0, h_pad=3.5)
  fig.suptitle(title, y=1, x=.52, fontsize=16)
  ax.set_title(subtitle)
  ax.scatter(df[xcol], df[ycol], color=df['Primary'], alpha=0)
  ax.set_xlim(0,100)
  ax.set_ylim(-1,15)
  for index, row in df.iterrows():
    ax.text(s=row['PLAYER_NAME'].split(' ')[1], x=row[xcol], y=row[ycol], horizontalalignment='center', bbox=dict(facecolor=row['Primary'], alpha=0.2, zorder=10), zorder=10)
    # else:
    #   ax.text(s=row['Name'].split(' ')[1], x=row[xcol], y=row[ycol], horizontalalignment='center', bbox=dict(facecolor=row['Primary'], alpha=0.2))
    # ax.text(s=row['label'], x=row[xcol], y=row[ycol], horizontalalignment='center', bbox=dict(facecolor=row['Primary'], alpha=0.5))
  fig.text(x=0.02,y=0.05,s='By Andrew Lawlor, Twitter: @lawlorpalooza', fontsize=8)
  fig.text(x=0.02,y=0.03,s='Data from stats.nba.com', fontsize=8)
  #fig.text(x=0.02,y=0.01,s='Updated through 8/29/20', fontsize=8)
  ax.grid(True, axis='y')
  # ax.legend()
  plt.savefig(f'output/{title} {subtitle}.png')