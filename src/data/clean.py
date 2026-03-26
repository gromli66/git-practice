import pandas as pd
import logging

logger = logging.getLogger(__name__)

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    before = len(df)
    df = df.drop_duplicates()
    removed = before - len(df)
    if removed > 0:
        logger.warning(f"Removed {removed} duplicate rows")
    else:
        logger.info("No duplicates found")
    return df

def fill_missing(df, column, method='ffill'):
    df[column] = df[column].fillna(method=method)
    return df