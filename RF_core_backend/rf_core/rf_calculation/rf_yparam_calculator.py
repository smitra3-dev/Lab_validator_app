import numpy as np
from rf_core.rf_column_identifiers.rf_constants import RF_Z0, RF_TINY
from rf_core.rf_helper.rf_math_utils import safe_db

#updated 13/04/26 subfolder access

def calculate_yparameters(work):
    work = work.copy()

    s11 = work["S11_comp"].to_numpy()
    s12 = work["S12_comp"].to_numpy()
    s21 = work["S21_comp"].to_numpy()
    s22 = work["S22_comp"].to_numpy()

    denom = (1 + s11) * (1 + s22) - (s12 * s21)
    denom = np.where(np.abs(denom) < RF_TINY, np.nan + 0j, denom)

    Y11 = ((1 - s11) * (1 + s22) + s12 * s21) / (RF_Z0 * denom)
    Y12 = (-2 * s12) / (RF_Z0 * denom)
    Y21 = (-2 * s21) / (RF_Z0 * denom)
    Y22 = ((1 + s11) * (1 - s22) + s12 * s21) / (RF_Z0 * denom)

    work["Y11_comp"] = Y11
    work["Y12_comp"] = Y12
    work["Y21_comp"] = Y21
    work["Y22_comp"] = Y22

    for yname in ["Y11", "Y12", "Y21", "Y22"]:
        ymag = np.abs(work[f"{yname}_comp"].to_numpy())
        work[f"{yname}_mag"] = ymag
        work[f"{yname}_dB"] = safe_db(ymag)

    return work
