#trend_predictor
import numpy as np


def predict_linear(x, coef):
    return np.polyval(coef, x)


def predict_log(x, coef):
    return np.polyval(coef, np.log(x))


def predict_exp(x, coef):
    return np.exp(np.polyval(coef, x))


def predict_trend(x, trend_type, coef):
    if trend_type == "linear":
        return predict_linear(x, coef)
    if trend_type == "log":
        return predict_log(x, coef)
    if trend_type == "exp":
        return predict_exp(x, coef)

    raise ValueError(f"Unsupported trend_type: {trend_type}")
