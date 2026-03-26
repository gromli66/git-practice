import pandas as pd
import numpy as np

# --- Data loading ---
def load_csv(path):
    return pd.read_csv(path, parse_dates=['timestamp'])

# --- Cleaning ---
def remove_duplicates(df):
    return df.drop_duplicates()

def fill_missing(df, column, method='ffill'):
    df[column] = df[column].fillna(method=method)
    return df

# --- Features ---
def add_lag(df, column, lag=1):
    df[f'{column}_lag_{lag}'] = df[column].shift(lag)
    return df

def add_rolling_mean(df, column, window=3):
    df[f'{column}_rolling_{window}'] = df[column].rolling(window).mean()
    return df

# --- Model ---
def train_model(X, y):
    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    model.fit(X, y)
    return model