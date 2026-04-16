#smooth check

import numpy as np
import pandas as pd


def moving_avg(y, window=5):
    y = np.asarray(y, dtype=float)

    if len(y) < 3:
        return y

    return (
        pd.Series(y)
        .rolling(window=window, center=True, min_periods=1)
        .mean()
        .values
    )
