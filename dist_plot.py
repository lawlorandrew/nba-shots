import seaborn as sns

def dist_plot(totals, stats_to_graph, col, team, ax, is_pct_col, show_colors = True, fontsize=24, label=None):
    if label is None:
      label = col
    sns.distplot(
        totals[col],
        ax=ax,
        hist=False,
        kde_kws={"shade": True},
        color=team['Primary'],
    )
    ax.axvline(stats_to_graph[col], color=team['Secondary'])
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlabel('')
    ax.yaxis.set_visible(False)
    if (is_pct_col):
        value = '{:.1%}'.format(stats_to_graph[col])
    else:
        value = '{:.1f}'.format(stats_to_graph[col])
    percentile = stats_to_graph[f'{col}_pct']
    percentile_text = 'P: ' + '{:.0f}'.format(stats_to_graph[f'{col}_pct']*100)
    value_text = value + '\n' + percentile_text
    text_color = 'black'
    if (show_colors == True):
      if (percentile > .67):
          text_color = 'g'
      elif (percentile > .33):
          text_color = 'y'
      else:
          text_color = 'r'
    ax.text(
        1.1,
        0.5,
        value_text,
        transform=ax.transAxes,
        horizontalalignment='right',
        verticalalignment='center',
        fontsize=fontsize,
        color=text_color,
    )
    ax.text(
        -.1,
        0.5,
        label,
        transform=ax.transAxes,
        horizontalalignment='left',
        verticalalignment='center',
        fontsize=fontsize,
    )
