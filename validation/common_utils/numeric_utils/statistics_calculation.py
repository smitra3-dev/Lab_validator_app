#validation/common/statistics.py

import numpy as np
import pandas as pd


def median_step(x):
    x = np.asarray(x, dtype=float)
    if len(x) < 2:
        return np.nan

    dx = np.diff(np.sort(np.unique(x)))
    dx = dx[np.isfinite(dx) & (dx > 0)]

    return np.median(dx) if len(dx) else np.nan


def rank_corr(x, y):
    if len(x) < 3 or len(y) < 3:
        return 0.0

    xr = pd.Series(x).rank().values
    yr = pd.Series(y).rank().values

    if np.std(xr) == 0 or np.std(yr) == 0:
        return 0.0

    return float(np.corrcoef(xr, yr)[0, 1])
