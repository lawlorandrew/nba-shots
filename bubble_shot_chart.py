import matplotlib.pyplot as plt
import pandas as pd
from shot_chart import shot_hex_chart
from draw_court import draw_court

shot_df = pd.read_csv('./data/all_shots.csv')
bubble_shots = shot_df[shot_df['GAME_DATE'] > 20200701]
bubble_teams = bubble_shots['TEAM_NAME'].unique()
pre_bubble_shots = shot_df[
  (shot_df['GAME_DATE'] < 20200701) &
  (shot_df['TEAM_NAME'].isin(bubble_teams)) &
  (shot_df['OPPONENT'].isin(bubble_teams))
]

fig, ax = plt.subplots(figsize=(33.3333, 28))
fig.text(
    s='Shot Locations in the Bubble',
    x=.5,
    y=.9,
    fontsize=80,
    fontweight='bold',
    verticalalignment='bottom',
    horizontalalignment='center'
)
fig.text(
    x=0,
    y=0.1,
    s='By Andrew Lawlor',
    horizontalalignment='left',
    verticalalignment='top',
    fontsize=40,
    style='italic'
)
fig.text(
  x=0,
  y=.075,
  s='All games in set featuring only bubble teams',
  fontsize=40,
  style='italic',
  verticalalignment='top',
  horizontalalignment='left'
)
fig.text(
    x=0,
    y=.05,
    s='Data from stats.nba.com',
    horizontalalignment='left',
    verticalalignment='top',
    fontsize=40,
    style='italic'
)
fig.text(
    x=0,
    y=.025,
    s='Updated 8/15/20',
    horizontalalignment='left',
    verticalalignment='top',
    fontsize=40,
    style='italic'
)
ax = draw_court(ax=ax, outer_lines=False)
teaminfo = pd.Series(['#17408B'], ['Primary'])
shot_hex_chart(all_shot_df=pre_bubble_shots,
               team_shot_df=bubble_shots, ax=ax, team_info=teaminfo)
plt.savefig('./output/bubble_shot_locations.png')
