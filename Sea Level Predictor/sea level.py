import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x, y)

    # Create first line of best fit
    line_one = linregress(x, y)
    x1 = np.arange(x.min(),2050,1)
    y1 = x1*line_one.slope + line_one.intercept
    plt.plot(x1,y1)

    # Create second line of best fit
    df_2000 = df[x >= 2000]

    line_two = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x1 = np.arange(2000,2050,1)
    y1 = x1*line_two.slope + line_two.intercept

    plt.plot(x1,y1)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
draw_plot()