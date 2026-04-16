import numpy as np


def check_h21_range(h21_db, min_db=-40, max_db=60):
    h21_db = np.asarray(h21_db, dtype=float)

    if np.any(h21_db > max_db) or np.any(h21_db < min_db):
        return "Check the measurement technique", "red"

    return None

def check_h21_rolloff(freq, h21_db, slope_tolerance=0.05):
    freq = np.asarray(freq, dtype=float)
    h21_db = np.asarray(h21_db, dtype=float)

    slope = np.gradient(h21_db, freq)

    if np.any(slope > slope_tolerance):
        return "Noisy!! data please check the measurement technique", "red"

    return None
