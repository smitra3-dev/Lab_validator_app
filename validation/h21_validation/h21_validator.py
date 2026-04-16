#validation/h21/h21_validator.py
import numpy as np
from validation.h21_validation.h21_config import H21_CONFIG
from validation.h21_validation.h21_check import check_h21_range, check_h21_rolloff


def validate_h21(freq, h21_db, config=None):
    cfg = dict(H21_CONFIG)
    if config:
        cfg.update(config)

    freq = np.array(freq)
    h21_db = np.array(h21_db)

    result = check_h21_range(
        h21_db,
        min_db=cfg["min_db"],
        max_db=cfg["max_db"]
    )
    if result:
        return result

    result = check_h21_rolloff(
        freq,
        h21_db,
        slope_tolerance=cfg["slope_tolerance"]
    )
    if result:
        return result

    return "The data is good to go!!", "green"
