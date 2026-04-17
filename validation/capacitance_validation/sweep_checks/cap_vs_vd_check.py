##sweep_checks/cap_vs_vd_check.py

from validation.capacitance_validation.utility.numeric_utils.statistic_utils import relative_span
from validation.capacitance_validation.utility.numeric_utils.monotonic_utils import monotonic_score
from validation.capacitance_validation.utility.numeric_utils.tag_utils import noise_tag
from validation.capacitance_validation.utility.cap_result_utils import append_cap_result

def validate_one_vs_vd(keys, cap, arr, results, cfg):
    rel_span = relative_span(arr, eps=cfg["small_eps"])
    score_down = monotonic_score(arr, direction="down")

    if cap == "Cgd":
        if score_down >= cfg["cgd_vd_mono_good"]:
            append_cap_result(
                results, cap, keys,
                status="Pass",
                comment=f"{cap} generally decreases with Vd (score = {score_down:.3f})",
                color="green",
                noise=noise_tag(arr),
            )
        else:
            append_cap_result(
                results, cap, keys,
                status="Warning",
                comment=f"{cap} does not clearly decrease with Vd (score = {score_down:.3f})",
                color="orange",
                noise=noise_tag(arr),
            )
    else:
        if rel_span <= cfg["vd_rel_span_warn"]:
            append_cap_result(
                results, cap, keys,
                status="Pass",
                comment=f"{cap} remains fairly controlled with Vd (relative span = {rel_span:.3f})",
                color="green",
                noise=noise_tag(arr),
            )
        else:
            append_cap_result(
                results, cap, keys,
                status="Warning",
                comment=f"{cap} shows strong dependence on Vd (relative span = {rel_span:.3f})",
                color="orange",
                noise=noise_tag(arr),
            )
