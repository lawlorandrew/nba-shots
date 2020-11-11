from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.pyplot as plt
import numpy as np

def player_scatter(df, xcol, ycol, xlabel, ylabel, title):
  fig, ax = plt.subplots(dpi=500, figsize=(10,10))
  ax.set_ylabel(ylabel)
  ax.set_xlabel(xlabel)
  ax.set_title(title)
  # ax.set_xlim(0,35)
  # ax.set_ylim(0.7,1.2)
  avg_rate = df.sum()[ycol] / df.sum()[xcol]
  ax.scatter(df[xcol], df[ycol], color=df['Primary'], alpha=0)
  for index, row in df.iterrows():
    # if (row['Name'] == 'Kris Dunn'):
    ax.text(s=row['PLAYER_NAME'], x=row[xcol], y=row[ycol], horizontalalignment='center', bbox=dict(facecolor=row['Primary'], alpha=0.5))
    # else:
    #   ax.text(s=row['Name'].split(' ')[1], x=row[xcol], y=row[ycol], horizontalalignment='center', bbox=dict(facecolor=row['Primary'], alpha=0.2))
    # ax.text(s=row['label'], x=row[xcol], y=row[ycol], horizontalalignment='center', bbox=dict(facecolor=row['Primary'], alpha=0.5))
  x_vals = np.array(ax.get_xlim())
  y_vals = x_vals*avg_rate
  ax.plot(x_vals, y_vals)
  fig.text(x=0.02,y=0.05,s='By Andrew Lawlor, Twitter: @lawlorpalooza', fontsize=8)
  fig.text(x=0.02,y=0.03,s='Data from Basketball Reference', fontsize=8)
  #fig.text(x=0.02,y=0.01,s='Updated through 8/29/20', fontsize=8)
  plt.savefig(f'output/{title}.png')