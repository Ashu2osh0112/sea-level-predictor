import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x_axis = df['Year']
    y_axis = df['CSIRO Adjusted Sea Level']

    plt.scatter(x_axis, y_axis)

    # Create first line of best fit
    res = linregress(x_axis, y_axis)
    x_fit = pd.Series([i for i in range(1880, 2051)])
    y_fit = res.slope * x_fit + res.intercept
    plt.plot(x_fit, y_fit, 'r', label='Best fit: 1880–2050')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_recent = pd.Series(range(2000, 2051))
    y_recent = res_recent.slope * x_recent + res_recent.intercept
    plt.plot(x_recent, y_recent, 'g', label='Best fit: 2000–2050')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()


    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
