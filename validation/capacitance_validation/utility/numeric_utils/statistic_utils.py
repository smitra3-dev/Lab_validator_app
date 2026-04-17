import numpy as np


def to_float_array(arr):
    return np.asarray(arr, dtype=float)


def relative_span(arr, eps=1e-18):
    arr = arr[np.isfinite(arr)]
    if len(arr) == 0:
        return 0.0
    return float((np.max(arr) - np.min(arr)) / (np.mean(np.abs(arr)) + eps))
