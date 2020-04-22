import matplotlib.pyplot as plt

def shot_chart(shot_df, ax, ylim=(-47.5,442.5)):
  ax.set_xlim(250, -250)
  ax.set_ylim(ylim)
  ax.axis('off')
  made_shots = shot_df[shot_df['EVENT_TYPE'] == 'Made Shot']
  missed_shots = shot_df[shot_df['EVENT_TYPE'] == 'Missed Shot']
  ax.scatter(missed_shots.LOC_X, missed_shots.LOC_Y, c='#F44336', label='Misses', s=160, zorder=5, alpha = 0.5)
  ax.scatter(made_shots.LOC_X, made_shots.LOC_Y, c='#000080', label='Makes', s=160, zorder=5, alpha = .5)
  ax.legend(loc='upper left', bbox_to_anchor=(0.02,.98), fontsize=32)

def shot_hex_chart(shot_df, ax, ylim=(-47.5,442.5)):
  ax.set_xlim(250, -250)
  ax.set_ylim(ylim)
  ax.axis('off')
  hb = ax.hexbin(x=shot_df.LOC_X, y=shot_df.LOC_Y, gridsize=50, bins='log', mincnt=5, alpha=0.8, vmin=5, vmax=500, cmap='viridis')
  cb = plt.colorbar(hb, ax=ax, shrink=0.5, location='bottom')
  cb.set_label('Shot Frequency', fontsize=32)
  cb.set_ticks([5, 500])
  cb.ax.set_xticklabels(['Less', 'More'], fontsize=24)
