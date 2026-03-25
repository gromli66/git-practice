import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def describe_data(df):
    return df.describe()