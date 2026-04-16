#Vth estimator 
import numpy as np

from validation.Gm_Gds_validation.gm_gds_helper.series_utils import get_sorted_xy


def estimate_vth_from_id_vg(df, cfg):
    x, y = get_sorted_xy(
        df=df,
        x_col=cfg["vg_col"],
        y_col=cfg["id_col"],
        abs_y=True,
        min_points=cfg.get("min_points_axis", 4),
    )

    if x is None or y is None:
        return np.nan

    ymax = np.nanmax(y)
    if not np.isfinite(ymax) or ymax <= 0:
        return np.nan

    threshold_current = cfg["vth_current_fraction"] * ymax
    hit_indices = np.where(y >= threshold_current)[0]

    if len(hit_indices) == 0:
        return np.nan

    return float(x[hit_indices[0]])
