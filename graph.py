import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from graph_comparison import graph_comparison
from graph_player import graph_player_distributions, graph_player_with_shot_chart
from graph_team import graph_team_distributions, graph_team_with_shot_chart
import json

totals_df = pd.read_csv('./data/nba_per_poss.csv')
totals_df['Name'] = totals_df['Player'].str.split('\\').str[0]
team_colors_df = pd.read_csv('./data/nba_team_colors.csv')
team_per_poss_df = pd.read_csv('./data/nba_team_per_poss.csv')
with open('./data/bulls_shots.json') as jsonFile:
  data = json.load(jsonFile)
  headers = data['resultSets'][0]['headers']
  shots = data['resultSets'][0]['rowSet']
  shot_df = pd.DataFrame(shots, columns=headers)

totals_df['FT Rate'] = totals_df['FTA'] / totals_df['FGA']
team_per_poss_df['FT Rate'] = team_per_poss_df['FTA'] / team_per_poss_df['FGA']

player = 'Zion Williamson'  # the player to graph
# whether or not the distributions should use only players of the same position, or all players
filter_by_position = False
# the position the player should be treated as (if None, just use default position from data)
position_to_use = None
cols = ['2P%', '2PA', '3P%', '3PA', 'FT%',
        'FTA', 'FT Rate']  # statistics to graph
# the statistics that should be rendered as percentages
pct_cols = ['2P%', '3P%', 'FT%', 'FT Rate']

graph_player_distributions(
    stats_df=totals_df,
    player_name=player,
    teams_df=team_colors_df,
    cols=cols,
    pct_cols=pct_cols,
    filter_by_position=filter_by_position,
    position_to_use=position_to_use,
)

shot_chart_player = 'Coby White'

graph_player_with_shot_chart(
    stats_df=totals_df,
    player_name=shot_chart_player,
    teams_df=team_colors_df,
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
# the statistics that should be rendered as percentages
pct_cols = ['2P%', '3P%', 'FT%', 'FT Rate']

graph_team_distributions(
  team_name='Chicago Bulls',
  stats_df=team_per_poss_df,
  teams_df=team_colors_df,
  pct_cols=pct_cols,
)

graph_team_with_shot_chart(
  team_name='Chicago Bulls',
  stats_df=team_per_poss_df,
  teams_df=team_colors_df,
  shots_df=shot_df,
  pct_cols=pct_cols,
)
