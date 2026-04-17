import numpy as np

def monotonic_score(arr, direction="up"):
    arr = arr[np.isfinite(arr)]
    if len(arr) < 2:
        return 1.0

    d = np.diff(arr)

    if direction == "up":
        good = np.sum(d >= 0)
    else:
        good = np.sum(d <= 0)

    return float(good / len(d))
