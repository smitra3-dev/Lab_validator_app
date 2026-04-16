#anomaly_residuals
import numpy as np


def compute_residual_error(y_true, y_pred, eps=1e-9):
    """
    Compute normalized residual error.
    """
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)

    residual = np.abs(y_true - y_pred)
    scale = np.max(np.abs(y_true)) + eps

    return residual / scale
