import numpy as np

from validation.capacitance_validation.utility.numeric_utils.statistic_utils import to_float_array
from validation.capacitance_validation.utility.numeric_utils.tag_utils import noise_tag
from validation.capacitance_validation.utility.cap_result_utils import append_cap_result

#updated 17/04/26

def run_cgg_sum_check(keys, work, valid, cap_data, selected_caps, results, cfg):
    if "Cgg" not in selected_caps:
        return
    if "Cgs" not in work.columns or "Cgd" not in work.columns:
        return

    cgs = to_float_array(work["Cgs"].values)[valid]
    cgd = to_float_array(work["Cgd"].values)[valid]
    cgg = cap_data["Cgg"]

    sum_cap = cgs + cgd
    rel_err = np.abs(cgg - sum_cap) / (np.abs(sum_cap) + cfg["small_eps"])
    med_rel_err = float(np.nanmedian(rel_err))

    fail_fraction = np.mean(cgg < cfg["cgg_sum_fail_scale"] * sum_cap)

    if fail_fraction > cfg["cgg_sum_fail_fraction"]:
        append_cap_result(
            results, "Cgg", keys,
            status="Fail",
            comment="Cgg is frequently much smaller than Cgs + Cgd",
            color="red",
            noise=noise_tag(cgg),
        )
    elif med_rel_err > cfg["cgg_sum_warn_rel_err"]:
        append_cap_result(
            results, "Cgg", keys,
            status="Warning",
            comment=f"Cgg deviates from Cgs + Cgd (median rel. error = {med_rel_err:.3f})",
            color="orange",
            noise=noise_tag(rel_err),
        )
    else:
        append_cap_result(
            results, "Cgg", keys,
            status="Pass",
            comment=f"Cgg is reasonably consistent with Cgs + Cgd (median rel. error = {med_rel_err:.3f})",
            color="green",
            noise=noise_tag(rel_err),
        )
