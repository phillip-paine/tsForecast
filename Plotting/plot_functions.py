import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def tsPlot(df: pd.DataFrame, tsCols = ['y'] : list(str)):
    # Find date column:
    date_colname = [c for c in df.columns if c in df.select_dtypes(include=[np.datetime64]).columns]
    # Create plot object:

    # write plot object:


