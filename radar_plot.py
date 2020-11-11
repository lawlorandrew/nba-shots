import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from math import pi


def get_tick_label(tick, index, col, pct_cols):
    if index == 0:
        return ''
    if col in pct_cols:
        return '{:.0%}'.format(tick)
    else:
        return '{:.1f}'.format(tick)


def radar_plot(totals_df, stats_to_graph, player_name, team_info, cols, pct_cols, season, fig, gs=None, inverse_cols=[], label_font_size=12, tick_font_size=6, label_padding=15):
    num_ticks = 5
    N = len(cols)
    angles = np.arange(0, 360, 360.0/N)
    if gs is None:
        gs = [0.15, 0.1, 0.65, 0.65]
        axes = [fig.add_axes(gs, projection="polar", label="axes%d" % i)
                for i in range(N)]
    else:
        axes = [fig.add_subplot(gs, projection="polar", label="axes%d" % i)
                for i in range(N)]
    mainAx = axes[0]
    mainAx.set_thetagrids(angles, labels=cols, fontsize=label_font_size)
    mainAx.tick_params(pad=label_padding)
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
            ticks = [((limit/num_ticks)*(num_ticks - i)) +
                     min_limit for i in range(num_ticks + 1)]
        else:
            min_limits.append(min_limit)
            ticks = [((limit/num_ticks)*i) +
                     min_limit for i in range(num_ticks + 1)]
        tick_labels = [get_tick_label(tick, i, col, pct_cols)
                       for i, tick in enumerate(ticks)]
        ax.set_rgrids(
            ticks,
            angle=angle,
            labels=tick_labels,
            horizontalalignment='center',
            verticalalignment='center',
            fontsize=tick_font_size,
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
            if (stats_to_graph[col] >= max_limit):
                radii.append(totals_df[col].quantile(.05))
            elif (stats_to_graph[col] <= totals_df[col].quantile(.05)):
                radii.append(totals_df[col].quantile(.95))
            else:
                dist_from_min = stats_to_graph[col] - \
                    totals_df[col].quantile(.05)
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
    values[1:] = ((values[1:]-min_limits[1:])/scales[1:]) * \
        scales[0] + min_limits[0]
    mainAx.xaxis.set_visible(True)
    mainAx.plot(thetas, values, color=team_info['Secondary'])
    mainAx.fill(thetas, values, color=team_info['Primary'], alpha=0.7)
    fig.suptitle(
        player_name,
        fontsize=20,
        fontweight='bold',
        y=.92,
        x=.02,
        horizontalalignment='left',
        verticalalignment='bottom'
    )
    fig.text(
        x=.02,
        y=.92,
        s=f'{team_info["Full"]}, {season - 1}-{season % 100} Regular Season',
        horizontalalignment='left',
        verticalalignment='top',
        fontsize=12,
        style='italic'
    )
    fig.text(
        x=.02,
        y=.88,
        s=f'Position: Guard',
        horizontalalignment='left',
        verticalalignment='top',
        fontsize=12,
        style='italic'
    )
    fig.text(
        x=.02,
        y=.03,
        s='By Andrew Lawlor, Twitter: @lawlorpalooza',
        horizontalalignment='left',
        verticalalignment='top',
        fontsize=8,
        style='italic'
    )
    fig.text(
        x=.02,
        y=.06,
        s='Data from Basketball Reference',
        horizontalalignment='left',
        verticalalignment='top',
        fontsize=8,
        style='italic'
    )
