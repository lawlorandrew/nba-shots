import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from math import pi
from utils import get_team_info

def get_tick_label(tick, index, col, pct_cols):
  if index == 0:
    return ''
  if col in pct_cols:
    return '{:.0%}'.format(tick)
  else:
    return '{:.1f}'.format(tick)

def radar_plot(totals_df, player_name, teams_df, cols, pct_cols, fig, inverse_cols=[], gs=111):
  stats_to_graph = totals_df[totals_df['Name'] == player_name].squeeze()
  team_info = get_team_info(stats_df = totals_df, teams_df=teams_df, player_name=player_name)
  num_ticks = 5
  N = len(cols)
  angles = np.arange(0, 360, 360.0/N)
  axes = [fig.add_subplot(gs, projection="polar", label="axes%d" % i)
                for i in range(N)]
  mainAx = axes[0]
  mainAx.set_thetagrids(angles, labels=cols, fontsize=12)
  mainAx.tick_params(pad=20)
  for ax in axes[1:]:
    ax.grid(False)
    ax.xaxis.set_visible(False)
    ax.patch.set_visible(False)

  scales = []
  min_limits = []
  for ax, angle, col in zip(axes, angles, cols):
    min_limit = totals_df[col].quantile(.05)
    max_limit = totals_df[col].quantile(.95)
    limit = max_limit - min_limit
    scales.append(limit)
    if col in inverse_cols:
      min_limits.append(min_limit)
      ticks = [((limit/num_ticks)*(num_ticks - i))+min_limit for i in range(num_ticks + 1)]
    else:
      min_limits.append(min_limit)
      ticks = [((limit/num_ticks)*i) + min_limit for i in range(num_ticks + 1)]
    tick_labels = [get_tick_label(tick, i, col, pct_cols) for i, tick in enumerate(ticks)]
    ax.set_rgrids(
      ticks,
      angle=angle,
      labels=tick_labels,
      horizontalalignment='center',
      verticalalignment='center',
      fontsize=8,
    )
    ax.spines["polar"].set_visible(False)
    if col in inverse_cols:
      ax.set_ylim(max_limit, min_limit)
    else:
      ax.set_ylim(min_limit, max_limit)
  
  radii = []
  for col in cols:
    if col in inverse_cols:
      max_limit = totals_df[col].quantile(.95)
      if (stats_to_graph[col] > max_limit):
        radii.append(0)
      elif (stats_to_graph[col] < totals_df[col].quantile(.05)):
        radii.append(totals_df[col].max() - totals_df[col].quantile(.05))
      else:
        dist_from_min = stats_to_graph[col] - totals_df[col].quantile(.05)
        radii.append(totals_df[col].quantile(.95) - dist_from_min)
    else:
      if (stats_to_graph[col] > totals_df[col].quantile(.95)):
        radii.append(totals_df[col].quantile(.95))
      elif (stats_to_graph[col] < totals_df[col].quantile(.05)):
        radii.append(totals_df[col].quantile(.05))
      else:
        radii.append(stats_to_graph[col])
  thetas = np.deg2rad(np.r_[angles, angles[0]])
  values = np.r_[radii, radii[0]]
  scales = np.r_[scales, scales[0]]
  min_limits = np.r_[min_limits, min_limits[0]]
  # scaling all values by first limit so they graph properly
  values[1:] = ((values[1:]-min_limits[1:])/scales[1:]) * scales[0] + min_limits[0]
  mainAx.xaxis.set_visible(True)
  mainAx.plot(thetas, values, color=team_info['Secondary'])
  mainAx.fill(thetas, values, color=team_info['Primary'], alpha=0.7)
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