#trend_metrics
import numpy as np


def mean_squared_error(y_true, y_pred):
    """
    Compute mean squared error.
    """
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)

    if len(y_true) == 0:
        return np.nan

    return float(np.mean((y_true - y_pred) ** 2))
