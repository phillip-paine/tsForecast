"""Class for the time series object"""
import pandas as pd


class TimeSeriesDataFrame:
    """Basic class for time series objects from a pandas dataframe"""
    def __init__(self, df_: pd.DataFrame, dict_columns: dict[str, list[str]], freq: str):
        self.df_ = df_
        self.date = dict_columns['date']
        self.y_ts = dict_columns['tsY']
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
