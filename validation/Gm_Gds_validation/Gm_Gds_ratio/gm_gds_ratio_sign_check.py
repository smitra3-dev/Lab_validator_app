
import numpy as np
from validation.common_utils.result_df.result_utils import add_result
from .gm_gds_ratio_check import compute_gm_gds_ratio

def check_gm_gds_ratio_in_sign_block(keys, group, gds, results, cfg):
    gm_col = cfg["gm_col"]
    if gm_col not in group.columns:
        return

    gm = group[gm_col].to_numpy(dtype=float)
    ratio = compute_gm_gds_ratio(gm, gds, cfg["eps"])

    if not np.isfinite(ratio):
        return

    if ratio < cfg["gm_gds_bad"]:
        add_result(
            results, "gds", keys,
            "gds is too large compared to gm.", "red",
            "Sign & Magnitude",
            f"Median gm/gds ≈ {ratio:.2f}."
        )
    elif ratio >= cfg["gm_gds_good"]:
        add_result(
            results, "gds", keys,
            "gds is suitably smaller than gm.", "green",
            "Sign & Magnitude",
            f"Median gm/gds ≈ {ratio:.2f}."
        )

    check_gm_gds_ratio_in_sign_block(keys, group, gds, results, cfg)

