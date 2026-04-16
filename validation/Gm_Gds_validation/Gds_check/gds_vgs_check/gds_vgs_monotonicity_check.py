#gds_vgs_monotonicity_check.py

import numpy as np

from validation.common_utils.numeric_utils.monotonicity_check import monotonicity_score
from validation.common_utils.result_df.result_utils import add_result


def check_gds_vgs_monotonicity(keys, vd_val, x, y, results, cfg):
    score = monotonicity_score(x, y, mode="increasing")

    if np.isfinite(score) and score >= cfg["mono_good"]:
        add_result(
            results, "gds", keys,
            f"gds increases smoothly with Vg at Vd={vd_val}.", "green",
            "gds vs Vg",
            "Consistent with stronger channel conduction."
        )
    elif np.isfinite(score) and score <= cfg["mono_bad"]:
        add_result(
            results, "gds", keys,
            f"gds trend with Vg is irregular at Vd={vd_val}.", "orange",
            "gds vs Vg",
            "Often caused by derivative noise or bias mismatch."
        )
