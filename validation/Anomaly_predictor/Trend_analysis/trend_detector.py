#trend_detector
import numpy as np

from .trend_models import (
    fit_linear_model,
    fit_log_model,
    fit_exp_model,
)
from .trend_metrics import mean_squared_error
from .trend_selector import select_best_trend_model


def detect_trend(x, y):
    """
    Detect best fitting trend among:
    - linear
    - log
    - exponential
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    models = {}

    # Linear
    coef_lin, y_lin = fit_linear_model(x, y)
    models["linear"] = (coef_lin, mean_squared_error(y, y_lin))

    # Log
    coef_log, y_log = fit_log_model(x, y)
    if coef_log is not None:
        models["log"] = (coef_log, mean_squared_error(y, y_log))

    # Exponential
    coef_exp, y_exp = fit_exp_model(x, y)
    if coef_exp is not None:
        models["exp"] = (coef_exp, mean_squared_error(y, y_exp))

    return select_best_trend_model(models)
