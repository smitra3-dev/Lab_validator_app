import numpy as np


def calculate_transconductance_metrics(work):
    work = work.copy()

    Y21 = work["Y21_comp"].to_numpy()
    Y22 = work["Y22_comp"].to_numpy()

    work["gm"] = np.real(Y21)
    work["gds"] = np.real(Y22)

    return work
