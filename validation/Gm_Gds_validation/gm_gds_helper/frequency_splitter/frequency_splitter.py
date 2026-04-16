import numpy as np

from .frequency_frame_builder import prepare_frequency_dataframe
from .fnqs_estimator import estimate_fnqs_from_ft
from .frequency_region_splitters import split_by_fnqs, split_by_absolute_limits


def split_lf_hf(df, cfg):
    """
    Split dataframe into LF and HF regions.

    Priority:
    1. Use fnqs estimated from Ft
    2. Otherwise, use absolute frequency thresholds
    """
    prepared = prepare_frequency_dataframe(df, cfg["fs_col"])
    if prepared is None:
        return None, None, np.nan

    fnqs = estimate_fnqs_from_ft(prepared, cfg["ft_candidates"])

    if np.isfinite(fnqs) and fnqs > 0:
        lf, hf = split_by_fnqs(prepared, fnqs)
        return lf, hf, fnqs

    lf, hf = split_by_absolute_limits(
        prepared,
        lf_fs_abs_max=cfg["lf_fs_abs_max"],
        hf_fs_abs_min=cfg["hf_fs_abs_min"],
    )
    return lf, hf, np.nan
