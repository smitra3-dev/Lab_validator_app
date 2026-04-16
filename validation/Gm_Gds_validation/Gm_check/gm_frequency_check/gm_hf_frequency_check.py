
import numpy as np

from validation.common_utils.numeric_utils.scaling_check import relative_variation, normalized_change
from validation.common_utils.result_df.result_utils import add_result



def check_gm_hf_behavior(keys, hf, results, cfg, fnqs):
    gm_col = cfg["gm_col"]
    fs_col = cfg["fs_col"]

    if hf is None or len(hf) < cfg["min_points_freq"]:
        return

    temp = hf[[fs_col, gm_col]].dropna().sort_values(fs_col)
    if len(temp) < 2:
        return

    y = temp[gm_col].to_numpy(dtype=float)
    rise = normalized_change(y[0], y[-1])

    if rise > cfg["hf_gm_rise_limit"]:
        add_result(
            results, "gm", keys,
            "gm increases strongly in HF region.", "red",
            "Frequency Check",
            "Strong HF rise is suspicious."
        )
        return

    detail = "Mild roll-off or flattening at HF is acceptable."
    if np.isfinite(fnqs):
        detail += f" Dynamic LF/HF split used with fNQS ≈ {fnqs:.3g}."

    add_result(
        results, "gm", keys,
        "gm does not show abnormal HF rise.", "green",
        "Frequency Check",
        detail
    )
