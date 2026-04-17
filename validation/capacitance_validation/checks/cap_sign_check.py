##cap_sign_check.py
import numpy as np

from validation.capacitance_validation.utility.numeric_utils.tag_utils import noise_tag
from validation.capacitance_validation.utility.cap_result_utils import append_cap_result

#updated 17/04/26

def run_cap_sign_checks(keys, cap_data, selected_caps, results):
    for cap in selected_caps:
        arr = cap_data[cap]

        if np.any(arr < 0):
            append_cap_result(
                results, cap, keys,
                status="Fail",
                comment=f"{cap} contains negative values",
                color="red",
                noise="NA",
            )
        else:
            append_cap_result(
                results, cap, keys,
                status="Pass",
                comment=f"{cap} is non-negative",
                color="green",
                noise=noise_tag(arr),
            )
