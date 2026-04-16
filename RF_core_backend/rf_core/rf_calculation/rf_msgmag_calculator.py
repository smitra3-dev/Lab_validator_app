import numpy as np
from rf_core.rf_column_identifiers.rf_constants import RF_TINY


def calculate_power_gain_metrics(work):
    work = work.copy()

    s12 = work["S12_comp"].to_numpy()
    s21 = work["S21_comp"].to_numpy()

    s12_safe = np.where(np.abs(s12) < RF_TINY, np.nan + 0j, s12)
    work["MSG"] = np.abs(s21 / s12_safe)

    k_sq_minus_1 = (work["K_factor"].to_numpy(dtype=float) ** 2) - 1
    k_sq_minus_1 = np.where(k_sq_minus_1 < 0, np.nan, k_sq_minus_1)

    work["MAG"] = work["MSG"].to_numpy(dtype=float) * (
        work["K_factor"].to_numpy(dtype=float) - np.sqrt(k_sq_minus_1)
    )

    return work
