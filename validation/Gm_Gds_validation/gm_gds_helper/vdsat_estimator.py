## vds sat 
import numpy as np


def estimate_vdsat(vgs, vth):
    if not np.isfinite(vgs) or not np.isfinite(vth):
        return np.nan
    return float(max(vgs - vth, 0.0))
