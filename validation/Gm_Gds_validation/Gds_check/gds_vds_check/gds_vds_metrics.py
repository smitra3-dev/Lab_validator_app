#gds_vds_metrics.py

import numpy as np


def compute_gds_drop_ratio(y, eps):
    if len(y) < 2:
        return np.nan

    if not (np.isfinite(y[0]) and np.isfinite(y[-1])):
        return np.nan

    if abs(y[-1]) <= eps:
        return np.nan

    return float(abs(y[0]) / abs(y[-1]))
