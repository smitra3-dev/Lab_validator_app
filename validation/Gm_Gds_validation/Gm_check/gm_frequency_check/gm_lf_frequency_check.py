import numpy as np

from validation.common_utils.numeric_utils.scaling_check import relative_variation, normalized_change
from validation.common_utils.result_df.result_utils import add_result




def check_gm_lf_behavior(keys, lf, results, cfg):
    gm_col = cfg["gm_col"]

    if lf is None or len(lf) < cfg["min_points_freq"]:
        return

    y = lf[gm_col].to_numpy(dtype=float)
    rel = relative_variation(y)

    if not np.isfinite(rel):
        return

    if rel <= cfg["lf_rel_var_gm"]:
        add_result(
            results, "gm", keys,
            "gm is nearly constant in LF region.", "green",
            "Frequency Check",
            "Consistent with quasi-static small-signal behavior."
        )
        return

    add_result(
        results, "gm", keys,
        "gm varies too much in LF region.", "orange",
        "Frequency Check",
        f"Relative LF variation ≈ {rel:.2f}."
    )
