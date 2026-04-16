import numpy as np
from rf_core.rf_column_identifiers.rf_constants import RF_TINY
from rf_core.rf_helper.rf_math_utils import safe_db

#updated 13/06/26 subfolder access

def calculate_h21_metrics(work):
    work = work.copy()

    Y11 = work["Y11_comp"].to_numpy()
    Y21 = work["Y21_comp"].to_numpy()

    Y11_safe = np.where(np.abs(Y11) < RF_TINY, np.nan + 0j, Y11)
    h21 = -Y21 / Y11_safe
    h21_mag = np.abs(h21)

    work["h21_mag"] = h21_mag
    work["h21_dB"] = safe_db(h21_mag)

    return work
