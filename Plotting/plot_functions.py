"""Plotting functions for time series:"""
import pandas as pd
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns
from Input.ts_input_data import TimeSeriesDataFrame

sns.set_style("darkgrid")

def tsPlot(tsObject: TimeSeriesDataFrame, plot_args):
    """Basic plotting of data against date/time"""
    # Create plot object:
    # write plot object:
    g = sns.relplot(data=tsObject.df_, x=tsObject.date, y=tsObject.y_ts, height=plot_args['height'],
                     aspect=plot_args['aspect'], kind='line')
    g.set(xlabel=plot_args['x_lab'], ylabel=plot_args['y_lab'], title=plot_args['title'])
    g.figure.savefig('Plot_files/test_line_plot.png')


if __name__ == '__main__':
    # Create Time Series object:
    # create date column:
    ts_dates = pd.date_range(start='2010-01-01', end='2019-12-31', freq='M')
    # create time series column:
    N = len(ts_dates)
    ts_y = np.linspace(100, 500, N) + norm.rvs(loc=0, scale = 10, size = N)
    data_dict = {'ts_dates': ts_dates, 'ts_y': ts_y}
    df = pd.DataFrame(data_dict)
    # Create ts object
    df_ts = TimeSeriesDataFrame(df, {'date': 'ts_dates', 'ts_data': 'ts_y', 'features': []}, 12)
    # Produce plot:
    tsPlot(df_ts, {'height': 8, 'aspect': 1.25, 'title': 'Plot of Time Series against Dates',
                   'x_lab': 'Date', 'y_lab': 'Value'})
