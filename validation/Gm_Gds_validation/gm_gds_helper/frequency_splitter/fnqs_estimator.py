import numpy as np
import pandas as pd

from validation.common_utils.dataframe_operation.df_generalize_name import pick_existing_column


def get_valid_ft_values(df, ft_candidates):
    """
    Pick the first existing Ft-like column and return cleaned positive numeric values.
    """
    ft_col = pick_existing_column(df, ft_candidates)
    if ft_col is None:
        return None, np.array([])

    ft_vals = pd.to_numeric(df[ft_col], errors="coerce").dropna().to_numpy(dtype=float)
    ft_vals = ft_vals[np.isfinite(ft_vals) & (ft_vals > 0)]

    return ft_col, ft_vals


def estimate_fnqs_from_ft(df, ft_candidates):
    """
    Estimate frequency boundary using:
        fnqs = median(Ft) / 33
    """
    ft_col, ft_vals = get_valid_ft_values(df, ft_candidates)

    if len(ft_vals) == 0:
        return np.nan

    return float(np.nanmedian(ft_vals) / 33.0)
