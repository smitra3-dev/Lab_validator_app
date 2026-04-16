import numpy as np
from rf_core.rf_column_identifiers.rf_constants import RF_TINY


def calculate_stability_factor(work):
    work = work.copy()

    s11 = work["S11_comp"].to_numpy()
    s12 = work["S12_comp"].to_numpy()
    s21 = work["S21_comp"].to_numpy()
    s22 = work["S22_comp"].to_numpy()

    delta = (s11 * s22) - (s12 * s21)
    s12s21_abs = np.abs(s12 * s21)
    s12s21_abs = np.where(s12s21_abs < RF_TINY, np.nan, s12s21_abs)

    work["K_factor"] = (
        1 - (np.abs(s11) ** 2) - (np.abs(s22) ** 2) + (np.abs(delta) ** 2)
    ) / (2 * s12s21_abs)

    return work
