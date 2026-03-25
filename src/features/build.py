import pandas as pd
def add_lag(df, column, lag=1):
    df[f'{column}_lag_{lag}'] = df[column].shift(lag)
    return df

def add_rolling_mean(df, column, window=3):
    df[f'{column}_rolling_{window}'] = df[column].rolling(window).mean()
    return df