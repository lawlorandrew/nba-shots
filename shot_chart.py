def shot_chart(shot_df, ax):
  ax.set_xlim(250, -250)
  ax.set_ylim(-47.5,442.5)
  ax.axis('off')
  made_shots = shot_df[shot_df['EVENT_TYPE'] == 'Made Shot']
  missed_shots = shot_df[shot_df['EVENT_TYPE'] == 'Missed Shot']
  ax.scatter(made_shots.LOC_X, made_shots.LOC_Y, c='#7986CB', label='Makes', s=80, zorder=5, alpha = 0.75)
  ax.scatter(missed_shots.LOC_X, missed_shots.LOC_Y, c='#F44336', label='Misses', s=80, zorder=10, alpha = 0.3)
  ax.legend(loc='upper left', bbox_to_anchor=(0.02,.98), fontsize=24)
