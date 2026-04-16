#trend_selector
import numpy as np


def select_best_trend_model(models):
    """
    models: dict {name: (coef, error)}
    """
    valid_models = {
        k: v for k, v in models.items()
        if v is not None and np.isfinite(v[1])
    }

    if not valid_models:
        return None, None

    best = min(valid_models, key=lambda k: valid_models[k][1])
    return best, valid_models[best][0]
