#validation/common/monotonicity.py
import numpy as np


def monotonicity_score(x, y, mode="increasing"):
    """
    Returns score in [0, 1].
    Score is the fraction of finite slope steps obeying expected sign.
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    mask = np.isfinite(x) & np.isfinite(y)
    x = x[mask]
    y = y[mask]

    if len(x) < 3:
        return np.nan

    idx = np.argsort(x)
    x = x[idx]
    y = y[idx]

    dx = np.diff(x)
    dy = np.diff(y)

    valid = np.abs(dx) > 0
    dx = dx[valid]
    dy = dy[valid]

    if len(dx) == 0:
        return np.nan

    if mode == "increasing":
        good = dy >= 0
    elif mode == "decreasing":
        good = dy <= 0
    else:
        raise ValueError("mode must be 'increasing' or 'decreasing'")

    return float(np.mean(good))
