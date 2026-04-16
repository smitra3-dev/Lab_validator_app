import pandas as pd

def is_complex_series(series):
    return pd.api.types.is_complex_dtype(series)
