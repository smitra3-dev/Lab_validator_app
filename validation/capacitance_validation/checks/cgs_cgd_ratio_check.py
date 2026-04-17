##cap_cross_checks.py
import numpy as np

from validation.capacitance_validation.utility.numeric_utils.statistic_utils import to_float_array
from validation.capacitance_validation.utility.numeric_utils.tag_utils import noise_tag
from validation.capacitance_validation.utility.cap_result_utils import append_cap_result

#updated 17/04/26

def run_cgs_cgd_ratio_check(keys, work, valid, cap_data, selected_caps, results, cfg):
    if "Cgs" not in selected_caps:
        return
    if "Cgd" not in work.columns:
        return

    cgs = cap_data["Cgs"]
    cgd = to_float_array(work["Cgd"].values)[valid]

    cgs_med = float(np.nanmedian(np.abs(cgs)))
    cgd_med = float(np.nanmedian(np.abs(cgd))) + cfg["small_eps"]
    ratio = cgs_med / cgd_med

    if ratio < cfg["cgs_cgd_fail_ratio"]:
        append_cap_result(
            results, "Cgs", keys,
            status="Fail",
            comment=f"Cgs/Cgd = {ratio:.3f}. Cgs is too small compared to Cgd",
            color="red",
        )
    elif ratio < cfg["cgs_cgd_warn_ratio"]:
        append_cap_result(
            results, "Cgs", keys,
            status="Warning",
            comment=f"Cgs/Cgd = {ratio:.3f}. Cgs dominance is weak",
            color="orange",
        )
    else:
        append_cap_result(
            results, "Cgs", keys,
            status="Pass",
            comment=f"Cgs/Cgd = {ratio:.3f}. Expected Cgs dominance observed",
            color="green",
        )
