#gds_lf_frequency_check.py
import numpy as np

from validation.common_utils.numeric_utils.scaling_check import relative_variation
from validation.common_utils.result_df.result_utils import add_result

def check_gds_lf_behavior(keys, lf, results, cfg):
    gds_col = cfg["gds_col"]

    if lf is None or len(lf) < cfg["min_points_freq"]:
        return

    y = lf[gds_col].to_numpy(dtype=float)
    rel = relative_variation(y)

    if not np.isfinite(rel):
        return

    if rel <= cfg["lf_rel_var_gds"]:
        add_result(
            results, "gds", keys,
            "gds is reasonably stable in LF region.", "green",
            "Frequency Check",
            "Consistent with quasi-static output conductance."
        )
        return

    add_result(
        results, "gds", keys,
        "gds varies too much in LF region.", "orange",
        "Frequency Check",
        f"Relative LF variation ≈ {rel:.2f}."
    )
