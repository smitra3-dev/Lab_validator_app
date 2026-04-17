##capacitance_validator.py
from validation.capacitance_validation.config.capacitance_config import CAPACITANCE_CONFIG
from validation.capacitance_validation.group_selection.cap_selection import resolve_selected_capacitances
from validation.capacitance_validation.group_selection.cap_group_prepare import find_missing_columns, prepare_capacitance_group
from validation.capacitance_validation.utility.cap_result_utils import append_cap_result
from validation.capacitance_validation.checks.cap_sign_check import run_cap_sign_checks
from validation.capacitance_validation.checks.cgg_sum_check import run_cgg_sum_check
from validation.capacitance_validation.checks.cgs_cgd_ratio_check import run_cgs_cgd_ratio_check
from .cap_sweep_dispatcher import run_sweep_checks


def validate_capacitances(groups, sweep_col, params=None, config=None):
    cfg = dict(CAPACITANCE_CONFIG)
    if config:
        cfg.update(config)

    results = []
    selected_caps = resolve_selected_capacitances(params, cfg["supported_caps"])

    if not selected_caps:
        return results

    for keys, group in groups:
        if group is None or len(group) == 0:
            continue

        missing = find_missing_columns(group, sweep_col, selected_caps)
        if missing:
            for cap in selected_caps:
                append_cap_result(
                    results, cap, keys,
                    status="Missing columns",
                    comment=f"Missing required columns: {', '.join(missing)}",
                    color="red",
                    noise="NA",
                )
            continue

        work, x, cap_data, valid = prepare_capacitance_group(group, sweep_col, selected_caps)

        if len(x) < cfg["min_points"]:
            for cap in selected_caps:
                append_cap_result(
                    results, cap, keys,
                    status="Insufficient data",
                    comment=f"Not enough valid points for {cap} validation vs {sweep_col}",
                    color="orange",
                    noise="NA",
                )
            continue

        run_cap_sign_checks(keys, cap_data, selected_caps, results)

        run_cgg_sum_check(keys, work, valid, cap_data, selected_caps, results, cfg)
        run_cgs_cgd_ratio_check(keys, work, valid, cap_data, selected_caps, results, cfg)

        run_sweep_checks(keys, sweep_col, selected_caps, cap_data, results, cfg)

    return results
