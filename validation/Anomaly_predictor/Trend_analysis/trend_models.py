#trend_models
import numpy as np


def fit_linear_model(x, y):
    coef = np.polyfit(x, y, 1)
    y_pred = np.polyval(coef, x)
    return coef, y_pred


def fit_log_model(x, y):
    if not np.all(x > 0):
        return None, None

    logx = np.log(x)
    coef = np.polyfit(logx, y, 1)
    y_pred = np.polyval(coef, logx)
    return coef, y_pred


def fit_exp_model(x, y):
    if not np.all(y > 0):
        return None, None

    logy = np.log(y)
    coef = np.polyfit(x, logy, 1)
    y_pred = np.exp(np.polyval(coef, x))
    return coef, y_pred
