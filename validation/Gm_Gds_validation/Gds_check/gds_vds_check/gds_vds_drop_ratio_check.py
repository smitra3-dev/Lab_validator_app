#gds_vds_drop_ratio_check.py
import numpy as np

from validation.common_utils.result_df.result_utils import add_result


def check_gds_vds_drop_ratio(keys, vg_val, drop_ratio, results, cfg):
    if not np.isfinite(drop_ratio):
        return

    if drop_ratio >= cfg["gds_sat_drop_ratio_min"]:
        add_result(
            results, "gds", keys,
            f"gds shows clear saturation reduction at Vg={vg_val}.", "green",
            "gds vs Vd",
            f"gds(low Vd)/gds(high Vd) ≈ {drop_ratio:.2f}."
        )
        return

    add_result(
        results, "gds", keys,
        f"gds does not drop enough from low Vd to high Vd at Vg={vg_val}.", "orange",
        "gds vs Vd",
        f"Observed ratio ≈ {drop_ratio:.2f}."
    )
