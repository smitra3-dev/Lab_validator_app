#peak abnormal detect
import numpy as np
from validation.common_utils.noise_metrics_utils.smooth_check import moving_avg

#updated import 16/04/26

def count_peaks(y, window=5, threshold_ratio=0.08):
    y = np.asarray(y, dtype=float)

    if len(y) < 5:
        return 0

    y_sm = moving_avg(y, window)
    yr = np.nanmax(y_sm) - np.nanmin(y_sm)

    if not np.isfinite(yr) or yr <= 0:
        return 0

    threshold = threshold_ratio * yr
    peaks = 0

    for i in range(1, len(y_sm) - 1):
        if y_sm[i] > y_sm[i - 1] and y_sm[i] > y_sm[i + 1]:
            left_ref = y_sm[max(0, i - 2)]
            right_ref = y_sm[min(len(y_sm) - 1, i + 2)]
            local_ref = max(left_ref, right_ref)

            if abs(y_sm[i] - local_ref) >= threshold:
                peaks += 1

    return peaks
