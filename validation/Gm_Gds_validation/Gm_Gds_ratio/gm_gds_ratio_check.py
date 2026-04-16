#gds ratio check 
import numpy as np


def compute_gm_gds_ratio(gm, gds, eps):
    """
    Compute median absolute gm/gds ratio over valid finite points.
    """
    gm = np.asarray(gm, dtype=float)
    gds = np.asarray(gds, dtype=float)

    mask = np.isfinite(gm) & np.isfinite(gds) & (np.abs(gds) > eps)
    if not np.any(mask):
        return np.nan

    return float(np.nanmedian(np.abs(gm[mask] / gds[mask])))
