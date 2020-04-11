from matplotlib.patches import Circle, Rectangle, Arc
import matplotlib.pyplot as plt

# Adapted from code found here: http://savvastjortjoglou.com/nba-shot-sharts.html


def draw_court(ax=None, color='black', outer_lines=False):
    outer_lw = 4
    inner_lw = 4
    # If an axes object isn't provided to plot onto, just get current one
    if ax is None:
        ax = plt.gca()

    # Create the various parts of an NBA basketball court

    # Create the basketball hoop
    # Diameter of a hoop is 18" so it has a radius of 9", which is a value
    # 7.5 in our coordinate system
    hoop = Circle((0, 0), radius=7.5, linewidth=inner_lw,
                  color=color, fill=False, zorder=25)

    # Create backboard
    backboard = Rectangle((-30, -7.5), 60, -1,
                          linewidth=inner_lw, color=color, zorder=0)

    # The paint
    # Create the outer box 0f the paint, width=16ft, height=19ft
    left_paint = Rectangle((-80, -47.5), 0, 190, linewidth=inner_lw, color=color,
                          fill=False, zorder=0)
        # Create the outer box 0f the paint, width=16ft, height=19ft
    right_paint = Rectangle((80, 142.5), 0, -190, linewidth=inner_lw, color=color,
                          fill=False, zorder=0)
        # Create the outer box 0f the paint, width=16ft, height=19ft
    free_throw_line = Rectangle((-80, 142.5), 160, 0, linewidth=inner_lw, color=color,
                          fill=False, zorder=0)

    # Create free throw top arc
    top_free_throw = Arc((0, 142.5), 120, 120, theta1=0, theta2=180,
                         linewidth=inner_lw, color=color, fill=False, zorder=0)

    # Restricted Zone, it is an arc with 4ft radius from center of the hoop
    restricted = Arc((0, 0), 80, 80, theta1=0, theta2=180, linewidth=inner_lw,
                     color=color, zorder=0)

    # Three point line
    # Create the side 3pt lines, they are 14ft long before they begin to arc
    corner_three_a = Rectangle((-220, -47.5), 0, 140, linewidth=inner_lw,
                               color=color, zorder=0)
    corner_three_b = Rectangle(
        (220, -47.5), 0, 140, linewidth=inner_lw, color=color)
    # 3pt arc - center of arc will be the hoop, arc is 23'9" away from hoop
    # I just played around with the theta values until they lined up with the
    # threes
    three_arc = Arc((0, 0), 475, 475, theta1=22, theta2=158, linewidth=inner_lw,
                    color=color, zorder=0)

    # List of the court elements to be plotted onto the axes
    court_elements = [hoop, backboard, left_paint, right_paint, free_throw_line, top_free_throw,
                      corner_three_a, corner_three_b, three_arc, restricted]

    if outer_lines:
        # Draw the half court line, baseline and side out bound lines
        outer_lines = Rectangle((-250, -47.5), 500, 470, linewidth=outer_lw,
                                color=color, fill=False, zorder=0)
        court_elements.append(outer_lines)

    # Add the court elements onto the axes
    for element in court_elements:
        ax.add_patch(element)

    return ax
