import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import pandas as pd

playoffs_df = pd.read_csv('./data/playoff_team_isolations.csv')
reg_season_df = pd.read_csv('./data/reg_season_isolations.csv')
xcol = 'POSS'
ycol = 'PPP'
xlabel = 'Possessions'
ylabel = 'Points Per Possession'
title = 'Isolations'
fig, ax = plt.subplots(dpi=500)
ax = plt.gca()
ims = []
dfs = [reg_season_df, playoffs_df]
for index in range(2):
  df = dfs[index]
  title = 'Regular Season Isolations'
  if (index == 1):
    title = 'Playoff Isolations'
  ttl = plt.text(0.5, 1.01, title, horizontalalignment='center', verticalalignment='bottom', transform=ax.transAxes)
  x, y, z = np.atleast_1d(df[xcol], df[ycol], df['TEAM_NAME'])
  artists = []
  for x0, y0, z0 in zip(x, y, z):
      image = plt.imread(f'./logos/{z0}.png')
      zoom = .05
      im = OffsetImage(image, zoom=zoom)
      ab = AnnotationBbox(im, (x0, y0), xycoords='data', frameon=False)
      artists.append(ax.add_artist(ab))
  vline = ax.axvline(df[xcol].mean(), ls='dotted', color='#000000')
  hline = ax.axhline(df[ycol].mean(), ls='dotted', color='#000000')
  artists.append(vline)
  artists.append(hline)
  artists.append(ttl)
  ims.append(artists)
ax.set_xlim(0,25)
ax.set_ylim(0.5,1.5)
ax.set_ylabel(ylabel)
ax.set_xlabel(xlabel)
# ax.set_title(title)
fig.text(x=0.02, y=0.05, s='By Andrew Lawlor, Twitter: @lawlorpalooza', fontsize=6)
fig.text(x=0.02, y=0.03, s='Data from stats.nba.com', fontsize=6)
fig.text(x=0.02, y=0.01, s='Updated through 8/29/20', fontsize=6)

ims=ims
ani = animation.ArtistAnimation(
    fig, ims, interval=2000, blit=True)
print(animation.writers.list())
ani.save('./output/isolations.gif', writer='imagemagick')
