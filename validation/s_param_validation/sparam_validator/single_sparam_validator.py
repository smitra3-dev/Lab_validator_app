#single_param_validator.py
import numpy as np

from validation.s_param_validation.sparam_check import (
    check_extreme,
    classify_s21,
    classify_s11_s22,
    classify_s12,
)
from .result_builder import build_validation_result


def is_supported_sparam(param):
    """
    Return True only for supported S-parameter dB columns.
    """
    return param in {"S11_dB", "S12_dB", "S21_dB", "S22_dB"}


def validate_single_sparam_group(param, keys, group, cfg):
    """
    Validate one S-parameter for one grouped dataframe.

    Parameters
    ----------
    param : str
        S-parameter column name.
    keys : any
        Group keys / identifiers.
    group : DataFrame-like
        Grouped subset containing parameter values.
    cfg : dict
        Validation configuration.

    Returns
    -------
    dict | None
        Validation result dictionary, or None if skipped.
    """
    if param not in group:
        return None

    values = group[param].values
    if len(values) == 0:
        return None

    extreme = check_extreme(
        values,
        high_db=cfg["extreme_high_db"],
        low_db=cfg["extreme_low_db"],
    )
    if extreme:
        msg, color = extreme
        return build_validation_result(param, keys, msg, color)

    avg_val = np.mean(values)

    if param == "S21_dB":
        msg, color = classify_s21(avg_val)

    elif param in {"S11_dB", "S22_dB"}:
        msg, color = classify_s11_s22(
            avg_val,
            good_match_db=cfg["s11_s22_good_match_db"],
            acceptable_match_db=cfg["s11_s22_acceptable_match_db"],
        )

    elif param == "S12_dB":
        msg, color = classify_s12(
            avg_val,
            good_isolation_db=cfg["s12_good_isolation_db"],
        )

    else:
        return None

    return build_validation_result(param, keys, msg, color)
