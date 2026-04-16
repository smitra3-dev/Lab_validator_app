#anomaly_slopes

import numpy as np


def compute_slope(x_block, y_block, eps=1e-9):
    """
    Compute first-order slope.
    """
    x_block = np.asarray(x_block, dtype=float)
    y_block = np.asarray(y_block, dtype=float)

    dy = np.diff(y_block)
    dx = np.diff(x_block)

    return dy / (dx + eps)


def compute_slope_error(x_block, y_block, eps=1e-9):
    """
    Compute normalized slope-change error aligned to block length.
    """
    if len(x_block) < 3:
        return np.zeros(len(y_block), dtype=float)

    slope = compute_slope(x_block, y_block, eps=eps)
    slope_change = np.diff(slope)

    if len(slope_change) == 0:
        return np.zeros(len(y_block), dtype=float)

    slope_norm = np.max(np.abs(slope)) + eps
    slope_error_core = np.abs(slope_change) / slope_norm

    slope_error = np.zeros(len(y_block), dtype=float)
    slope_error[1:-1] = slope_error_core

    return slope_error
