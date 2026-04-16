#gds_intrinsic_gain_check.py

import numpy as np

from validation.common_utils.result_df.result_utils import add_result
from validation.Gm_Gds_validation.Gm_Gds_ratio.gm_gds_ratio_check import compute_gm_gds_ratio


def check_intrinsic_gain(keys, vd_val, gm, gds, results, cfg):
    ratio = compute_gm_gds_ratio(gm, gds, cfg["eps"])
    if not np.isfinite(ratio):
        return

    if ratio < cfg["gm_gds_bad"]:
        add_result(
            results, "gds", keys,
            f"gm/gds is too low at Vd={vd_val}.", "red",
            "Intrinsic Gain",
            f"Median gm/gds ≈ {ratio:.2f}."
        )
    elif ratio >= cfg["gm_gds_excellent"]:
        add_result(
            results, "gds", keys,
            f"gm/gds is excellent at Vd={vd_val}.", "green",
            "Intrinsic Gain",
            f"Median gm/gds ≈ {ratio:.2f}."
        )
    elif ratio >= cfg["gm_gds_good"]:
        add_result(
            results, "gds", keys,
            f"gm/gds is acceptable at Vd={vd_val}.", "green",
            "Intrinsic Gain",
            f"Median gm/gds ≈ {ratio:.2f}."
        )
    else:
        add_result(
            results, "gds", keys,
            f"gm/gds is only marginal at Vd={vd_val}.", "orange",
            "Intrinsic Gain",
            f"Median gm/gds ≈ {ratio:.2f}."
        )
