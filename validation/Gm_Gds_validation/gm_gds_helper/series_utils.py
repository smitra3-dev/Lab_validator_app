# series utils 
import numpy as np
import pandas as pd


def get_numeric_series(df, column_name):
    if column_name not in df.columns:
        return None
    return pd.to_numeric(df[column_name], errors="coerce")


def get_sorted_xy(df, x_col, y_col, abs_y=False, min_points=4):
    if x_col not in df.columns or y_col not in df.columns:
        return None, None

    temp = df[[x_col, y_col]].copy()
    temp[x_col] = pd.to_numeric(temp[x_col], errors="coerce")
    temp[y_col] = pd.to_numeric(temp[y_col], errors="coerce")
    temp = temp.dropna(subset=[x_col, y_col]).sort_values(x_col)

    if len(temp) < min_points:
        return None, None

    x = temp[x_col].to_numpy(dtype=float)
    y = temp[y_col].to_numpy(dtype=float)

    if abs_y:
        y = np.abs(y)

    return x, y
