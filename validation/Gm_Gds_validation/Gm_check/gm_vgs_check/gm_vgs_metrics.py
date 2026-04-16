#gm_vgs_metrics
import numpy as np
from validation.common_utils.numeric_utils.monotonicity_check import monotonicity_score


def compute_gm_vgs_monotonicity(x, y):
    return monotonicity_score(x, y, mode="increasing")


def compute_gm_peak(x, y):
    peak_idx = int(np.nanargmax(y))
    return x[peak_idx]
