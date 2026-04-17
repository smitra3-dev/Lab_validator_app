###cap_sweep_dispatcher.py

from .sweep_checks import (
    validate_one_vs_frequency,
    validate_one_vs_vg,
    validate_one_vs_vd,
    validate_one_vs_id,
)


def run_sweep_checks(keys, sweep_col, selected_caps, cap_data, results, cfg):
    for cap in selected_caps:
        arr = cap_data[cap]

        if sweep_col == "Fs":
            validate_one_vs_frequency(keys, cap, arr, results, cfg)
        elif sweep_col == "Vg":
            validate_one_vs_vg(keys, cap, arr, results, cfg)
        elif sweep_col == "Vd":
            validate_one_vs_vd(keys, cap, arr, results, cfg)
        elif sweep_col == "Id":
            validate_one_vs_id(keys, cap, arr, results, cfg)
