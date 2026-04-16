#gm_vds_check

import numpy as np

from validation.common_utils.result_df.result_utils import add_result
from validation.Gm_Gds_validation.gm_gds_helper.vth_estimator import estimate_vth_from_id_vg

from .gm_vds_prepare import prepare_gm_vds_dataframe
from .gm_vds_metrics import compute_gm_vds_change


def check_gm_vs_vds(keys, group, results, cfg):
    gm_col = cfg["gm_col"]
    vg_col = cfg["vg_col"]
    vd_col = cfg["vd_col"]

    if gm_col not in group.columns or vg_col not in group.columns or vd_col not in group.columns:
        return

    temp = prepare_gm_vds_dataframe(group, cfg)
    if temp is None:
        return

    vth = estimate_vth_from_id_vg(temp, cfg)

    for vg_val, vg_group in temp.groupby(vg_col):
        if len(vg_group) < cfg["min_points_axis"]:
            continue

        if np.isfinite(vth) and vg_val <= vth:
            continue

        vg_group = vg_group.sort_values(vd_col)
        y = vg_group[gm_col].to_numpy(dtype=float)

        change = compute_gm_vds_change(y)
        if change is None:
            continue

        if change > cfg["gm_vd_allowed_growth"]:
            add_result(results, "gm", keys,
                       f"gm rises too much with Vd at Vg={vg_val}.",
                       "red", "gm vs Vd", "Should saturate.")
        elif change < -cfg["gm_vd_allowed_drop"]:
            add_result(results, "gm", keys,
                       f"gm drops with Vd at Vg={vg_val}.",
                       "orange", "gm vs Vd", "Possible instability.")
        else:
            add_result(results, "gm", keys,
                       f"gm vs Vd is reasonable at Vg={vg_val}.",
                       "green", "gm vs Vd", "Expected saturation.")
