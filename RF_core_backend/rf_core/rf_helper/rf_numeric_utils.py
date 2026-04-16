import pandas as pd


def safe_numeric(series):
    return pd.to_numeric(series, errors="coerce")
