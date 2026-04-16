#gm_vds_metrics

from validation.common_utils.numeric_utils.scaling_check import normalized_change


def compute_gm_vds_change(y):
    if len(y) < 2:
        return None
    return normalized_change(y[0], y[-1])
