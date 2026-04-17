##sweep_checks/cap_vs_id_check.py

from validation.capacitance_validation.utility.numeric_utils.statistic_utils import relative_span
from validation.capacitance_validation.utility.numeric_utils.oscillating_check_utils import oscillation_score
from validation.capacitance_validation.utility.numeric_utils.tag_utils import noise_tag
from validation.capacitance_validation.utility.cap_result_utils import append_cap_result

def validate_one_vs_id(keys, cap, arr, results, cfg):
    rel_span = relative_span(arr, eps=cfg["small_eps"])
    osc = oscillation_score(arr)

    if rel_span <= cfg["id_rel_span_flat_warn"]:
        append_cap_result(
            results, cap, keys,
            status="Warning",
            comment=f"{cap} is nearly flat vs Id",
            color="orange",
            noise=noise_tag(arr),
        )
    else:
        append_cap_result(
            results, cap, keys,
            status="Pass",
            comment=f"{cap} shows measurable variation vs Id",
            color="green",
            noise=noise_tag(arr),
        )

    if osc > cfg["id_osc_warn"]:
        append_cap_result(
            results, cap, keys,
            status="Warning",
            comment=f"{cap} is oscillatory / noisy vs Id",
            color="orange",
            noise="High",
        )
    else:
        append_cap_result(
            results, cap, keys,
            status="Pass",
            comment=f"{cap} is reasonably smooth vs Id",
            color="green",
            noise="Low",
        )
