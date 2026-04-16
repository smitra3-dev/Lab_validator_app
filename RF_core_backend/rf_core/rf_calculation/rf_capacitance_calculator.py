import numpy as np


def calculate_capacitance_metrics(work):
    work = work.copy()

    Y11 = work["Y11_comp"].to_numpy()
    Y12 = work["Y12_comp"].to_numpy()

    fs_ghz = work["Fs"].to_numpy(dtype=float)
    fs_hz = fs_ghz * 1e9
    fs_hz = np.where(fs_hz <= 0, np.nan, fs_hz)

    work["Cgd"] = -(np.imag(Y12)) / (2 * np.pi * fs_hz)
    work["Cgs"] = (np.imag(Y12) + np.imag(Y11)) / (2 * np.pi * fs_hz)
    work["Cgg"] = np.imag(Y11) / (2 * np.pi * fs_hz)

    return work
