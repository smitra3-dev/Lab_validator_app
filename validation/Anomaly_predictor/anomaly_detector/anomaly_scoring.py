#anomaly_scoring
import numpy as np


def combine_anomaly_errors(slope_error, residual_error, slope_weight=0.6, residual_weight=0.4):
    """
    Combine slope-based and residual-based errors into one score.
    """
    slope_error = np.asarray(slope_error, dtype=float)
    residual_error = np.asarray(residual_error, dtype=float)

    return slope_weight * slope_error + residual_weight * residual_error
