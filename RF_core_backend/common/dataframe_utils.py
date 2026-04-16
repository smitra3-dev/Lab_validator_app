import numpy as np


def sanitize_columns(df):
    df = df.copy()
    df.columns = df.columns.str.strip()
    return df


def ensure_columns(df, columns):
    for col in columns:
        if col not in df.columns:
            df[col] = np.nan
    return df
