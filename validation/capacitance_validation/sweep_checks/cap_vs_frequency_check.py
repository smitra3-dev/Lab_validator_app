##sweep_checks/cap_vs_frequency_check.py
from validation.capacitance_validation.utility.numeric_utils.statistic_utils import relative_span
from validation.capacitance_validation.utility.numeric_utils.oscillating_check_utils import oscillation_score
from validation.capacitance_validation.utility.numeric_utils.tag_utils import noise_tag
from validation.capacitance_validation.utility.cap_result_utils import append_cap_result


def validate_one_vs_frequency(keys, cap, arr, results, cfg):
    rel_span = relative_span(arr, eps=cfg["small_eps"])
    osc = oscillation_score(arr)

    if rel_span > cfg["freq_rel_span_warn"]:
        append_cap_result(
            results, cap, keys,
            status="Warning",
            comment=f"{cap} varies strongly with frequency (relative span = {rel_span:.3f})",
            color="orange",
            noise=noise_tag(arr),
        )
    else:
        append_cap_result(
            results, cap, keys,
            status="Pass",
            comment=f"{cap} frequency dependence is acceptable (relative span = {rel_span:.3f})",
            color="green",
            noise=noise_tag(arr),
        )

    if osc > cfg["freq_osc_warn"]:
        append_cap_result(
            results, cap, keys,
            status="Warning",
            comment=f"{cap} shows ripple / oscillation vs frequency",
            color="orange",
            noise="High",
        )
    else:
        append_cap_result(
            results, cap, keys,
            status="Pass",
            comment=f"{cap} is reasonably smooth vs frequency",
            color="green",
            noise="Low",
        )
