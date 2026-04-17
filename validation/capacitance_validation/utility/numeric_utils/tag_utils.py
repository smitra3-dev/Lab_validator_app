
import numpy as np
from .oscillating_check_utils import oscillation_score

def noise_tag(arr):
    arr = arr[np.isfinite(arr)]
    if len(arr) < 4:
        return "Low"

    score = oscillation_score(arr)
    if score > 0.50:
        return "High"
    if score > 0.25:
        return "Medium"
    return "Low"
