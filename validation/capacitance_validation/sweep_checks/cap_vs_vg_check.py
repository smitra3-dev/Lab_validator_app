##sweep_checks/cap_vs_vg_check.py

from validation.capacitance_validation.utility.numeric_utils.statistic_utils import relative_span
from validation.capacitance_validation.utility.numeric_utils.monotonic_utils import monotonic_score
from validation.capacitance_validation.utility.numeric_utils.tag_utils import noise_tag
from validation.capacitance_validation.utility.cap_result_utils import append_cap_result


def validate_one_vs_vg(keys, cap, arr, results, cfg):
    score_up = monotonic_score(arr, direction="up")
    rel_span = relative_span(arr, eps=cfg["small_eps"])

    if cap == "Cgs":
        if score_up >= cfg["cgs_vg_mono_good"]:
            append_cap_result(
                results, cap, keys,
                status="Pass",
                comment=f"{cap} generally increases with Vg (score = {score_up:.3f})",
                color="green",
                noise=noise_tag(arr),
            )
        else:
            append_cap_result(
                results, cap, keys,
                status="Warning",
                comment=f"{cap} does not clearly increase with Vg (score = {score_up:.3f})",
                color="orange",
                noise=noise_tag(arr),
            )

    elif cap == "Cgg":
        if rel_span <= cfg["cgg_vg_flat_warn"]:
            append_cap_result(
                results, cap, keys,
                status="Warning",
                comment=f"{cap} is nearly flat vs Vg",
                color="orange",
                noise=noise_tag(arr),
            )
        else:
            append_cap_result(
                results, cap, keys,
                status="Pass",
                comment=f"{cap} shows visible dependence with Vg",
                color="green",
                noise=noise_tag(arr),
            )

    else: # Cgd
        if score_up > cfg["cgd_vg_rise_warn"]:
            append_cap_result(
                results, cap, keys,
                status="Warning",
                comment=f"{cap} rises strongly with Vg (score = {score_up:.3f})",
                color="orange",
                noise=noise_tag(arr),
            )
        else:
            append_cap_result(
                results, cap, keys,
                status="Pass",
                comment=f"{cap} remains relatively controlled with Vg",
                color="green",
                noise=noise_tag(arr),
            )
