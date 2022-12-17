"""Class for the time series object"""
import pandas as pd
import numpy as np
from scipy.stats import norm


class TimeSeriesDataFrame:
    """Basic class for time series objects from a pandas dataframe"""
    def __init__(self, df_: pd.DataFrame, dict_columns: dict[str, list[str]], freq: int):
        self.df_ = df_
        self.date = dict_columns['date']
        self.y_ts = dict_columns['ts_data']
        self._features = dict_columns['features']  # want to be able to change this after it is set
        self.freq = freq

    def frequency(self) -> str:
        """return the frequency of time series data as string"""
        if self.freq == 365:
            return 'daily'
        if self.freq == 52:
            return 'weekly'
        if self.freq == 12:
            return 'monthly'
        if self.freq == 4:
            return 'quarterly'
        return 'annual'

    @property
    def features(self):
        """getter for the features variable"""
        return self._features

    @features.setter
    def features(self, new_features):
        """setter for features"""
        self._features = new_features


# Test file:
# TODO Write unit tests using unittest class
if __name__ == '__main__':
    # create date column:
    ts_dates = pd.date_range(start='2010-01-01', end='2019-12-31', freq='M')
    # create time series column:
    N = len(ts_dates)
    ts_y = np.linspace(100, 500, N) + norm.rvs(loc=0, scale = 10, size = N)
    data_dict = {'ts_dates': ts_dates, 'ts_y': ts_y}
    df = pd.DataFrame(data_dict, columns=['ds', 'y'])
    # Create ts object
    df_ts = TimeSeriesDataFrame(df, {'date': 'ds', 'ts_data': 'y', 'features': []}, 12)
    print(df_ts.features)

