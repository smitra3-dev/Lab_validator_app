#gds sign check 
import numpy as np

from validation.common_utils.result_df.result_utils import add_result

def _check_gds_sign(keys, gds, results, cfg):
    if np.nanmin(gds) <= cfg["neg_tol_gds"]:
        add_result(
            results, "gds", keys,
            "gds becomes negative.", "red",
            "Sign & Magnitude",
            "Negative gds is usually non-physical."
        )
        return

    add_result(
        results, "gds", keys,
        "gds stays positive.", "green",
        "Sign & Magnitude",
        "Basic output-conductance sanity is satisfied."
    )


def check_gds_sign_magnitude(keys, group, results, cfg):
    gds_col = cfg["gds_col"]

    if gds_col not in group.columns:
        return

    gds = group[gds_col].dropna().to_numpy(dtype=float)
    if len(gds) == 0:
        return

    _check_gds_sign(keys, gds, results, cfg)

