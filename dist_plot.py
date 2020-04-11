import seaborn as sns

def dist_plot(totals, stats_to_graph, col, team, ax, is_pct_col):
    sns.distplot(
        totals[col],
        ax=ax,
        hist=False,
        kde_kws={"shade": True},
        color=team['Primary'],
    )
    ax.axvline(stats_to_graph[col], color=team['Secondary'])
    sns.despine(left=True)
    ax.set_xlabel('')
    ax.yaxis.set_visible(False)
    if (is_pct_col):
        value = '{:.1%}'.format(stats_to_graph[col])
    else:
        value = '{:.1f}'.format(stats_to_graph[col])
    percentile = stats_to_graph[f'{col}_pct']
    percentile_text = 'P: ' + '{:.0f}'.format(stats_to_graph[f'{col}_pct']*100)
    value_text = value + '\n' + percentile_text
    if (percentile > .8):
        text_color = 'g'
    elif (percentile > .4):
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
        fontsize=24,
        color=text_color
    )
    ax.text(
        -.1,
        0.5,
        col,
        transform=ax.transAxes,
        horizontalalignment='left',
        verticalalignment='center',
        fontsize=24,
    )