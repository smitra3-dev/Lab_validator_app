import numpy as np
import pandas as pd


def ensure_required_columns(df: pd.DataFrame, required_cols):
    out = df.copy()
    for col in required_cols:
        if col not in out.columns:
            out[col] = np.nan
    return out
