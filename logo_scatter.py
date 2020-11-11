from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.pyplot as plt
import numpy as np

def logo_scatter(df, xcol, ycol, xlabel, ylabel, title):
  fig, ax = plt.subplots(dpi=500)
  ax = plt.gca()
  x, y, z = np.atleast_1d(df[xcol], df[ycol], df['Team'])
  artists = []
  for x0, y0, z0 in zip(x, y, z):
    image = plt.imread(f'./logos/{z0}.png')
    zoom = .05
    im = OffsetImage(image, zoom=zoom)
    ab = AnnotationBbox(im, (x0, y0), xycoords='data', frameon=False)
    artists.append(ax.add_artist(ab))
  ax.update_datalim(np.column_stack([x, y]))
  ax.autoscale()
  ax.set_ylabel(ylabel)
  ax.set_xlabel(xlabel)
  ax.set_title(title)
  # m, b = np.polyfit(df[xcol], df[ycol], 1)
  # print(m)
  # print(b)
  ax.axvline(df[xcol].median(), ls='dotted', color='#000000')
  ax.axhline(df[ycol].median(), ls='dotted', color='#000000')
  ax.annotate('MIA\n#4 OFF\n#7 DEF\n#2 OVR', (109.4,115.5), horizontalalignment='center', verticalalignment='bottom', fontsize=6, color='#98002e')
  ax.annotate('LAL\n#2 OFF\n#4 DEF\n#1 OVR', (106.9,115.6), horizontalalignment='center', verticalalignment='center', fontsize=6, color='#552583')
  ax.set_xlim(122.5,102.5)
  ax.set_ylim(100,125)
  x = np.linspace(100,122.5)
  y = x
  ax.plot(x, y, ls='dotted', color='black')
  ax.annotate("Bad Offense, Good Defense", (103.5,101), horizontalalignment='right', verticalalignment='bottom', fontsize=8)
  ax.annotate("Good Offense, Good Defense", (103.5,124.5), horizontalalignment='right', verticalalignment='top', fontsize=8)
  ax.annotate("Bad Offense, Bad Defense", (121.5,101), horizontalalignment='left', verticalalignment='bottom', fontsize=8)
  ax.annotate("Good Offense, Bad Defense", (121.5,124.5), horizontalalignment='left', verticalalignment='top', fontsize=8)
  fig.text(x=0.02,y=0.05,s='By Andrew Lawlor, Twitter: @lawlorpalooza', fontsize=6)
  fig.text(x=0.02,y=0.03,s='Data from Basketball Reference', fontsize=6)
  # fig.text(x=0.02,y=0.01,s='Updated 8/15/20', fontsize=6)
  plt.savefig(f'output/{title}.png')