import numpy as np
from rf_core.rf_helper.rf_math_utils import safe_db

#updated 13/04/26 subfolder access

def build_sparameters(work):
    work = work.copy()

    work["S11_comp"] = work["S11R"].to_numpy(dtype=float) + 1j * work["S11I"].to_numpy(dtype=float)
    work["S12_comp"] = work["S12R"].to_numpy(dtype=float) + 1j * work["S12I"].to_numpy(dtype=float)
    work["S21_comp"] = work["S21R"].to_numpy(dtype=float) + 1j * work["S21I"].to_numpy(dtype=float)
    work["S22_comp"] = work["S22R"].to_numpy(dtype=float) + 1j * work["S22I"].to_numpy(dtype=float)

    for s in ["S11", "S12", "S21", "S22"]:
        mag = np.abs(work[f"{s}_comp"].to_numpy())
        work[s] = mag
        work[f"{s}_dB"] = safe_db(mag)

    return work
