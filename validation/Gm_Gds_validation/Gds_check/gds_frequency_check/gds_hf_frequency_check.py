#gds_hf_frequency_check.py
import numpy as np

from validation.common_utils.numeric_utils.scaling_check import normalized_change
from validation.common_utils.result_df.result_utils import add_result


def check_gds_hf_behavior(keys, hf, results, cfg, fnqs):
    gds_col = cfg["gds_col"]
    fs_col = cfg["fs_col"]

    if hf is None or len(hf) < cfg["min_points_freq"]:
        return

    temp = hf[[fs_col, gds_col]].dropna().sort_values(fs_col)
    if len(temp) < 2:
        return

    y = temp[gds_col].to_numpy(dtype=float)
    rise = normalized_change(y[0], y[-1])

    if rise > cfg["hf_gds_rise_limit"]:
        add_result(
            results, "gds", keys,
            "gds increases strongly in HF region.", "red",
            "Frequency Check",
            "Strong HF rise suggests parasitic or de-embedding issues."
        )
        return

    detail = "No abnormal HF inflation of gds is observed."
    if np.isfinite(fnqs):
        detail += f" Dynamic LF/HF split used with fNQS ≈ {fnqs:.3g}."

    add_result(
        results, "gds", keys,
        "gds HF trend looks acceptable.", "green",
        "Frequency Check",
        detail
    )
