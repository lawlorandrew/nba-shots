import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.collections import PatchCollection
from matplotlib.path import Path
from matplotlib.patches import PathPatch, Circle
import numpy as np
import math
import pandas as pd

def shot_chart(shot_df, ax, ylim=(-47.5,442.5)):
  ax.set_xlim(250, -250)
  ax.set_ylim(ylim)
  ax.axis('off')
  made_shots = shot_df[shot_df['EVENT_TYPE'] == 'Made Shot']
  missed_shots = shot_df[shot_df['EVENT_TYPE'] == 'Missed Shot']
  ax.scatter(missed_shots.LOC_X, missed_shots.LOC_Y, c='#F44336', label='Misses', s=160, zorder=5, alpha = 0.5)
  ax.scatter(made_shots.LOC_X, made_shots.LOC_Y, c='#000080', label='Makes', s=160, zorder=5, alpha = .5)
  ax.legend(loc='upper left', bbox_to_anchor=(0.02,.98), fontsize=32)

def shot_hex_chart(all_shot_df, team_shot_df, ax, ylim=(-62.5,427.5)):
  ax.set_xlim(250, -250)
  ax.set_ylim(ylim)
  ax.axis('off')
  # team_shot_df['xbin'] = pd.cut(team_shot_df.LOC_X, 20)
  # team_shot_df['ybin'] = pd.cut(team_shot_df.LOC_Y, 40)
  # print(team_shot_df['xbin'])
  # team_shot_df['x']
  # all_shot_df["is_team_shot"] = -1/30
  # all_shot_df.loc[all_shot_df["TEAM_NAME"] == "Philadelphia 76ers",["is_team_shot"]] = 1
  # print(all_shot_df["TEAM_NAME"])
  #all_shot_df.loc[all_shot_df["TEAM_NAME"] != "Philadelphia 76ers",["is_team_shot"]] = -1
  # hb = ax.hexbin(x=all_shot_df.LOC_X, y=all_shot_df.LOC_Y, C=all_shot_df.is_team_shot, mincnt=1, gridsize=20, bins=5)
  hb = ax.hexbin(x=team_shot_df.LOC_X, y=team_shot_df.LOC_Y, gridsize=15, extent=[-250,250,-62.5,500-62.5])
  all_hb = ax.hexbin(x=all_shot_df.LOC_X, y=all_shot_df.LOC_Y, gridsize=15, extent=[-250,250,-62.5,500-62.5])
  verts = hb.get_offsets()
  vals = hb.get_array()
  # print(vals.shape)
  orgpath = hb.get_paths()[0]
  all_vals = all_hb.get_array()
  # print(all_vals.shape)
  patches = []
  tot = team_shot_df.shape[0]
  league_tot = all_shot_df.shape[0]
  legend_y = 400
  legend_offsets = [
    [100, legend_y],
    [50, legend_y],
    [0, legend_y],
    [-50, legend_y],
    [-100, legend_y]
  ]
  legend_alphas = [.2, .4, .6, .8, 1]
  for offset, alpha in zip(legend_offsets, legend_alphas):
    v1 = orgpath.vertices+offset
    path = Path(v1, orgpath.codes)
    patch = PathPatch(path, color='#006bb6',alpha=alpha)
    patches.append(patch)
  ax.text(x=125, y=400, s='A little more than average', horizontalalignment='right', fontsize=36)
  ax.text(x=-125, y=400, s='A lot more than average', horizontalalignment='left', fontsize=36)
  for offset, val, all_val in zip(verts, vals, all_vals):
    pct = val / tot
    league_pct = all_val / league_tot
    diff = pct - league_pct
    if (diff > .0005):
      alpha = .2
      if (diff > .0025):
        alpha=1
      elif (diff > .002):
        alpha=.8
      elif (diff > .0015):
        alpha=.6
      elif (diff > .001):
        alpha = .4
      v1 = orgpath.vertices+offset
      path = Path(v1, orgpath.codes)
      patch = PathPatch(path, color='#006bb6',alpha=alpha)
      patches.append(patch)
    # avg_val = all_val / 30
    # diff = max(val - avg_val, 0)
    # circle = Circle(offset, diff / 5, alpha=0.2)
    # patches.append(circle)

  pc = PatchCollection(patches, match_original=True)
  # # print(all_shot_df.head())
  # # print('vals')
  # # print(vals)
  # # print('all_vals')
  # # print(all_vals)
  # # print('diff')
  avgs = all_vals / 30
  diff = vals - avgs
  # diff[diff < 0] = 0
  # # with np.errstate(divide='ignore', invalid='ignore'):
  # #   result = np.true_divide(diff,avgs)
  # #   result[result == np.inf] = 0
  # #   result = np.nan_to_num(result)
  # # pc.set_array(result)
  ax.add_collection(pc)
  hb.remove()
  #hb.set_array(diff)
  all_hb.remove()
