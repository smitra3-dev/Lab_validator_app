#reciprocity check

import numpy as np


def check_reciprocity(
    s12,
    s21,
    rel_tol: float = 0.02,
) -> tuple[str, str]:
    """
    Check reciprocity using element-wise relative tolerance.

    Parameters
    ----------
    s12 : array-like
        S12 values.
    s21 : array-like
        S21 values.
    rel_tol : float
        Relative tolerance.

    Returns
    -------
    tuple[str, str]
        (message, color)
    """
    s12_arr = np.asarray(s12, dtype=float)
    s21_arr = np.asarray(s21, dtype=float)

    diff = np.abs(s12_arr - s21_arr)
    tol = rel_tol * np.maximum(np.abs(s21_arr), 1e-9)

    if np.all(diff <= tol):
        return "Reciprocity proves: Passive device", "lightblue"
    return "Reciprocity fails: Active device", "purple"
