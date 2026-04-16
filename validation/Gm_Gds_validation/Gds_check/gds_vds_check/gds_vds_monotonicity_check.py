
import numpy as np

from validation.common_utils.numeric_utils.monotonicity_check import monotonicity_score
from validation.common_utils.result_df.result_utils import add_result


def check_gds_vds_monotonicity(keys, vg_val, vd_values, y, results, cfg):
    score = monotonicity_score(vd_values, y, mode="decreasing")

    if np.isfinite(score) and score >= cfg["mono_good"]:
        add_result(
            results, "gds", keys,
            f"gds decreases properly with Vd at Vg={vg_val}.", "green",
            "gds vs Vd",
            "Expected transition toward saturation."
        )
    elif np.isfinite(score) and score <= cfg["mono_bad"]:
        add_result(
            results, "gds", keys,
            f"gds does not reduce properly with Vd at Vg={vg_val}.", "red",
            "gds vs Vd",
            "Could indicate wrong extraction or missing saturation."
        )
