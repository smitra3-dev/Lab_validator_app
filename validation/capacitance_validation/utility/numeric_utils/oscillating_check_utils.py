import numpy as np


def oscillation_score(arr):
    arr = arr[np.isfinite(arr)]
    if len(arr) < 4:
        return 0.0

    d = np.diff(arr)
    if len(d) < 2:
        return 0.0

    sign_changes = np.sum(np.diff(np.sign(d)) != 0)
    return float(sign_changes / max(1, len(d) - 1))
