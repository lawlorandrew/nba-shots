import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from graph_comparison import graph_comparison
from graph_player import graph_player
from graph_team import graph_team

totals_df = pd.read_csv('./data/nba_per_poss.csv')
totals_df['Name'] = totals_df['Player'].str.split('\\').str[0]
team_colors_df = pd.read_csv('./data/nba_team_colors.csv')

totals_df['FT Rate'] = totals_df['FTA'] / totals_df['FGA']

player = 'DeMar DeRozan' # the player to graph
filter_by_position= False # whether or not the distributions should use only players of the same position, or all players
position_to_use = None # the position the player should be treated as (if None, just use default position from data)
team = totals_df.loc[totals_df['Name']==player, ['Tm']].squeeze()
colors=team_colors_df.loc[team_colors_df['Team'] == team].squeeze() # team colors to use
cols = ['2P%', '2PA', '3P%', '3PA', 'FT%', 'FTA', 'FT Rate'] # statistics to graph
pct_cols = ['2P%', '3P%', 'FT%', 'FT Rate'] # the statistics that should be rendered as percentages

graph_player(
    stats_df=totals_df,
    player=player,
    team=colors,
    cols=cols,
    pct_cols=pct_cols,
    filter_by_position=filter_by_position,
    position_to_use=position_to_use,
)

player = 'Jayson Tatum' # the player to graph
filter_by_position= False # whether or not the distributions should use only players of the same position, or all players
position_to_use = None # the position the player should be treated as (if None, just use default position from data)
team = totals_df.loc[totals_df['Name']==player, ['Tm']].squeeze()
colors=team_colors_df.loc[team_colors_df['Team'] == team].squeeze() # team colors to use
cols = ['2P%', '2PA', '3P%', '3PA', 'FT%', 'FTA', 'FT Rate'] # statistics to graph
pct_cols = ['2P%', '3P%', 'FT%', 'FT Rate'] # the statistics that should be rendered as percentages

graph_player(
    stats_df=totals_df,
    player=player,
    team=colors,
    cols=cols,
    pct_cols=pct_cols,
    filter_by_position=filter_by_position,
    position_to_use=position_to_use,
)

cols = ['2P%', '2PA', '3P%', '3PA', 'FT%', 'FTA', 'FT Rate'] # statistics to graph
pct_cols = ['2P%', '3P%', 'FT%', 'FT Rate'] # the statistics that should be rendered as percentages
players = pd.DataFrame([['Jayson Tatum', 'green'], ['LeBron James', 'purple']], columns=['Name', 'Color'])
graph_comparison(
    stats_df=totals_df,
    players=players,
    cols=cols,
    pct_cols=pct_cols,
    filter_by_position=False,
)