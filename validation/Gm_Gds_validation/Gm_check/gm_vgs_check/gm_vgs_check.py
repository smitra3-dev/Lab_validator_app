#gm_vgs_check
import numpy as np

from validation.common_utils.result_df.result_utils import add_result
from validation.Gm_Gds_validation.gm_gds_helper.vth_estimator import estimate_vth_from_id_vg

from .gm_vgs_prepare import prepare_gm_vgs_dataframe
from .gm_vgs_metrics import compute_gm_vgs_monotonicity, compute_gm_peak
from .gm_vgs_peak_check import check_gm_peak_location


def check_gm_vs_vgs(keys, group, results, cfg):
    gm_col = cfg["gm_col"]
    vg_col = cfg["vg_col"]
    vd_col = cfg["vd_col"]

    if gm_col not in group.columns or vg_col not in group.columns or vd_col not in group.columns:
        return

    temp = prepare_gm_vgs_dataframe(group, cfg)
    if temp is None:
        return

    for vd_val, vd_group in temp.groupby(vd_col):
        if len(vd_group) < cfg["min_points_axis"]:
            continue

        vd_group = vd_group.sort_values(vg_col)

        x = vd_group[vg_col].to_numpy(dtype=float)
        y = vd_group[gm_col].to_numpy(dtype=float)

        score = compute_gm_vgs_monotonicity(x, y)

        if np.isfinite(score) and score >= cfg["mono_good"]:
            add_result(results, "gm", keys,
                       f"gm rises properly with Vg at Vd={vd_val}.",
                       "green", "gm vs Vg", "Expected behavior.")
        elif np.isfinite(score) and score <= cfg["mono_bad"]:
            add_result(results, "gm", keys,
                       f"gm does not rise properly with Vg at Vd={vd_val}.",
                       "red", "gm vs Vg", "Check extraction.")

        peak_vg = compute_gm_peak(x, y)
        vth = estimate_vth_from_id_vg(vd_group, cfg)

        check_gm_peak_location(keys, vd_val, x, peak_vg, vth, results, cfg)
