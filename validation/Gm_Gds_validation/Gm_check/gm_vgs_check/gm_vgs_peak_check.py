#gm_vgs_peak_check
import numpy as np
from validation.common_utils.result_df.result_utils import add_result


def check_gm_peak_location(keys, vd_val, x, peak_vg, vth, results, cfg):
    x_min, x_max = np.nanmin(x), np.nanmax(x)
    span = x_max - x_min

    edge_lo = x_min + cfg["edge_fraction"] * span
    edge_hi = x_max - cfg["edge_fraction"] * span

    if peak_vg <= edge_lo or peak_vg >= edge_hi:
        add_result(
            results, "gm", keys,
            f"gm peak occurs at edge of Vg sweep (Vd={vd_val}).",
            "orange", "gm Peak Location",
            "Peak may not be fully captured."
        )
        return

    detail = "gm peak lies inside Vg range."
    if np.isfinite(vth):
        detail += f" Estimated Vth ≈ {vth:.3g}."

    add_result(
        results, "gm", keys,
        f"gm peak location looks reasonable at Vd={vd_val}.",
        "green", "gm Peak Location",
        detail
    )
