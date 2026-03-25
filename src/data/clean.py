import pandas as pd
def remove_duplicates(df):
    return df.drop_duplicates()

def fill_missing(df, column, method='ffill'):
    df[column] = df[column].fillna(method=method)
    return df