import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from graph_comparison import graph_comparison
from graph_player import graph_player
from graph_team import graph_team
import json

totals_df = pd.read_csv('./data/nba_per_poss.csv')
totals_df['Name'] = totals_df['Player'].str.split('\\').str[0]
team_colors_df = pd.read_csv('./data/nba_team_colors.csv')
with open('./data/zion_williamson_shots.json') as jsonFile:
  data = json.load(jsonFile)
  # Grab the headers to be used as column headers for our DataFrame
  headers = data['resultSets'][0]['headers']
  # Grab the shot chart data
  shots = data['resultSets'][0]['rowSet']
  shot_df = pd.DataFrame(shots, columns=headers)

totals_df['FT Rate'] = totals_df['FTA'] / totals_df['FGA']

player = 'Zion Williamson'  # the player to graph
# whether or not the distributions should use only players of the same position, or all players
filter_by_position = False
# the position the player should be treated as (if None, just use default position from data)
position_to_use = None
team = totals_df.loc[totals_df['Name'] == player, ['Tm']].squeeze()
colors = team_colors_df.loc[team_colors_df['Team']
                            == team].squeeze()  # team colors to use
cols = ['2P%', '2PA', '3P%', '3PA', 'FT%',
        'FTA', 'FT Rate']  # statistics to graph
# the statistics that should be rendered as percentages
pct_cols = ['2P%', '3P%', 'FT%', 'FT Rate']

graph_player(
    stats_df=totals_df,
    player=player,
    team=colors,
    cols=cols,
    pct_cols=pct_cols,
    shot_df=shot_df,
    filter_by_position=filter_by_position,
    position_to_use=position_to_use,
)

cols = ['2P%', '2PA', '3P%', '3PA', 'FT%',
        'FTA', 'FT Rate']  # statistics to graph
# the statistics that should be rendered as percentages
pct_cols = ['2P%', '3P%', 'FT%', 'FT Rate']
players = pd.DataFrame([['Jayson Tatum', '#00a55c'], [
                       'Jaylen Brown', '#bb9753']], columns=['Name', 'Color'])
graph_comparison(
    stats_df=totals_df,
    players=players,
    cols=cols,
    pct_cols=pct_cols,
    filter_by_position=False,
)

team = 'CHI'  # the team to graph
# whether or not the distributions should use only players of the same position, or all players
filter_by_position = False
# the position the player should be treated as (if None, just use default position from data)
position_to_use = None
colors = team_colors_df.loc[team_colors_df['Team']
                            == team].squeeze()  # team colors to use
cols = ['2P%', '2PA', '3P%', '3PA', 'FT%',
        'FTA', 'FT Rate']  # statistics to graph
# the statistics that should be rendered as percentages
pct_cols = ['2P%', '3P%', 'FT%', 'FT Rate']

#graph_team(
#   stats_df=totals_df,
#    team=team,
#    teamInfo=colors,
#    cols=cols,
#    pct_cols=pct_cols,
#    filter_by_position=filter_by_position,
#)
