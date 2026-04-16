#validation/common/conversions.py

import numpy as np
import pandas as pd


def safe_num(series):
    return pd.to_numeric(series, errors="coerce")


def as_float_array(series):
    arr = pd.to_numeric(series, errors="coerce").to_numpy(dtype=float)
    return arr[np.isfinite(arr)]

