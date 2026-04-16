import numpy as np
from rf_core.rf_column_identifiers.rf_constants import RF_TINY


def calculate_ft_fmax_metrics(work):
    work = work.copy()

    Y11 = work["Y11_comp"].to_numpy()
    Y12 = work["Y12_comp"].to_numpy()
    Y21 = work["Y21_comp"].to_numpy()
    Y22 = work["Y22_comp"].to_numpy()

    h21_mag = work["h21_mag"].to_numpy(dtype=float)
    fs_ghz = work["Fs"].to_numpy(dtype=float)

    u_denom = 4 * (
        (np.real(Y11) * np.real(Y22)) -
        (np.real(Y12) * np.real(Y21))
    )
    u_denom = np.where(np.abs(u_denom) < RF_TINY, np.nan, u_denom)

    U = (np.abs(Y21 - Y12) ** 2) / u_denom

    work["Ft"] = fs_ghz * h21_mag
    work["Fmax"] = fs_ghz * np.sqrt(U)

    return work
