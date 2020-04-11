import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from math import pi
from utils import get_team_info

def get_tick_label(tick, col, pct_cols):
  if col in pct_cols:
    return '{:.0%}'.format(tick)
  else:
    return '{:.0f}'.format(tick)

def radar_plot(totals_df, player_name, teams_df, cols, pct_cols, fig, rect = None):
  stats_to_graph = totals_df[totals_df['Name'] == 'Zach LaVine'].squeeze()
  team_info = get_team_info(stats_df = totals_df, teams_df=teams_df, player_name=player_name)
  if rect is None:
    rect = [0.1, 0.1, 0.75, 0.75]
  num_ticks = 5
  N = len(cols)
  angles = np.arange(0, 360, 360.0/N)
  axes = [fig.add_axes(rect, projection="polar", label="axes%d" % i) 
                for i in range(N)]
  mainAx = axes[0]
  mainAx.set_thetagrids(angles, labels=cols, fontsize=12, zorder=0)
  mainAx.tick_params(pad=20)
  for ax in axes:
    ax.patch.set_visible(False)
    ax.grid("off")
    ax.xaxis.set_visible(False)

  limits = []
  for ax, angle, col in zip(axes, angles, cols):
    limit = totals_df[col].max()
    limits.append(limit)
    ticks = [(limit/num_ticks)*i for i in range(num_ticks + 1)]
    tick_labels = [get_tick_label(tick, col, pct_cols) for tick in ticks]
    ax.set_rgrids(
      ticks,
      angle=angle,
      labels=tick_labels,
      horizontalalignment='center',
      verticalalignment='center',
      fontsize=8,
      zorder=0,
    )
    ax.spines["polar"].set_visible(False)
    ax.set_ylim(0, limit)
  
  radii = []
  for col in cols:
    radii.append(stats_to_graph[col])
  thetas = np.deg2rad(np.r_[angles, angles[0]])
  values = np.r_[radii, radii[0]]
  limits = np.r_[limits, limits[0]]
  # scaling all values by first limit so they graph properly
  values[1:] = (values[1:]/limits[1:]) * limits[0]
  mainAx.xaxis.set_visible(True)
  mainAx.plot(thetas, values)
  mainAx.fill(thetas, values, zorder=100, color=team_info['Primary'])
  plt.savefig(f'output/{player_name} Radar 2019-20.png')

test_series = pd.Series(
  data=[10, 20, 10, 30],
  index=['stat1', 'stat2', 'stat3', 'stat4'],
)
test_totals = pd.DataFrame(
  data=[[10, 20, 10, 30],[100, 50, 75, 80]],
  columns=['stat1', 'stat2', 'stat3', 'stat4']
)

#fig = plt.figure()
#radar_plot(totals_df=test_totals,stats_to_graph=test_series, cols=['stat1', 'stat2', 'stat3', 'stat4'], fig=fig)