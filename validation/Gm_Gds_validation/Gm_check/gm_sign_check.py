# sign check 
import numpy as np

from validation.common_utils.result_df.result_utils import add_result


def check_gm_sign_magnitude(keys, group, results, cfg):
    gm_col = cfg["gm_col"]

    if gm_col not in group.columns:
        return

    gm = group[gm_col].dropna().to_numpy(dtype=float)
    if len(gm) == 0:
        return

    if np.nanmin(gm) <= cfg["neg_tol_gm"]:
        add_result(
            results=results,
            param="gm",
            keys=keys,
            message="gm becomes negative.",
            color="red",
            category="Sign & Magnitude",
            detail="For an RF MOSFET under normal bias, gm should stay positive.",
        )
        return

    add_result(
        results=results,
        param="gm",
        keys=keys,
        message="gm is positive across the sweep.",
        color="green",
        category="Sign & Magnitude",
        detail="Basic physical sanity is satisfied.",
    )
