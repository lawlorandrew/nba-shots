def shot_chart(shot_df, ax, ylim=(-47.5,442.5)):
  ax.set_xlim(250, -250)
  ax.set_ylim(ylim)
  ax.axis('off')
  made_shots = shot_df[shot_df['EVENT_TYPE'] == 'Made Shot']
  missed_shots = shot_df[shot_df['EVENT_TYPE'] == 'Missed Shot']
  ax.scatter(made_shots.LOC_X, made_shots.LOC_Y, c='#7986CB', label='Makes', s=160, zorder=5, alpha = 1)
  ax.scatter(missed_shots.LOC_X, missed_shots.LOC_Y, c='#F44336', label='Misses', s=160, zorder=10, alpha = 0.3)
  ax.legend(loc='upper left', bbox_to_anchor=(0.02,.98), fontsize=32)
