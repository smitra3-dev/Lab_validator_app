#metric 
import numpy as np
from validation.common_utils.noise_metrics_utils.smooth_check import moving_avg

#updated import 16/04/26

def noise_metric(y):
    y = np.asarray(y, dtype=float)

    if len(y) < 5:
        return 0.0

    ys = moving_avg(y, 5)
    resid = y - ys
    amp = np.nanmax(ys) - np.nanmin(ys)

    if not np.isfinite(amp) or amp <= 1e-18:
        return 0.0

    return float(np.nanstd(resid) / amp)
