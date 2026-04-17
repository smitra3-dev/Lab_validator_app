 #cap_group_prepare.py
import numpy as np

from validation.capacitance_validation.utility.numeric_utils.statistic_utils import to_float_array


def find_missing_columns(group, sweep_col, selected_caps):
    needed_cols = [sweep_col] + selected_caps
    return [c for c in needed_cols if c not in group.columns]


def prepare_capacitance_group(group, sweep_col, selected_caps):
    work = group.copy().sort_values(sweep_col)

    x = to_float_array(work[sweep_col].values)
    cap_data = {}

    valid = np.isfinite(x)

    for cap in selected_caps:
        arr = to_float_array(work[cap].values)
        cap_data[cap] = arr
        valid = valid & np.isfinite(arr)

    x = x[valid]
    for cap in selected_caps:
        cap_data[cap] = cap_data[cap][valid]

    return work, x, cap_data, valid
