import numpy as np


def safe_db(arr):
    arr = np.asarray(arr, dtype=float)
    return 20 * np.log10(np.clip(arr, 1e-30, None))


def safe_complex_divide(num, den, tiny=1e-30):
    den_safe = np.where(np.abs(den) < tiny, np.nan + 0j, den)
    return num / den_safe
