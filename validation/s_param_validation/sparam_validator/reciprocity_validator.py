#reciprocity_validator.py

from validation.s_param_validation.sparam_check.reciprocity_check import check_reciprocity
from .result_builder import build_validation_result


def should_run_reciprocity(params):
    """
    Reciprocity requires both S12_dB and S21_dB.
    """
    return "S12_dB" in params and "S21_dB" in params


def validate_reciprocity_group(keys, group, cfg):
    """
    Validate reciprocity for one grouped dataframe.

    Parameters
    ----------
    keys : any
        Group identifiers.
    group : DataFrame-like
        Grouped subset.
    cfg : dict
        Validation configuration.

    Returns
    -------
    dict | None
        Reciprocity result dictionary, or None if skipped.
    """
    if "S12_dB" not in group or "S21_dB" not in group:
        return None

    s12 = group["S12_dB"].values
    s21 = group["S21_dB"].values

    if len(s12) == 0 or len(s21) == 0:
        return None

    msg, color = check_reciprocity(
        s12,
        s21,
        rel_tol=cfg["reciprocity_rel_tol"],
    )

    return build_validation_result("Reciprocity", keys, msg, color)
